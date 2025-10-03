import os
import sys
import json
import types
import importlib
import importlib.util
from unittest.mock import patch

# Ensure the functions/ directory is importable as a top-level module location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)


# Helper: Fake firebase_functions.Response used to capture returned data
class FakeResponse:
    def __init__(self, response=None, mimetype=None, status=200, **kwargs):
        self.status_code = status
        if isinstance(response, (dict, list)):
            self._body_text = json.dumps(response)
        else:
            self._body_text = '' if response is None else response
        self.headers = kwargs.get('headers', {})

    def get_data(self, as_text=False):
        if as_text:
            return self._body_text
        return self._body_text.encode('utf-8')


class DummyRequest:
    def __init__(self, headers=None, method='POST', json_data=None, raise_on_get_json=False):
        self.headers = headers or {}
        self.method = method
        self._json_data = json_data
        self._raise = raise_on_get_json

    def get_json(self, silent=False):
        if self._raise:
            raise Exception('Malformed JSON')
        return self._json_data


def _parse_response(resp):
    data = resp.get_data(as_text=True)
    return json.loads(data)


# -----------------------------
# Tests for OpenAI proxy (v1_02)
# -----------------------------


def test_openai_create_replacement_applied_to_input():
    # Prepare fake modules to satisfy imports inside _openai_proxy
    _orig_sys_modules = {}
    names_to_fake = ['firebase_functions', 'utils', 'auth', 'openai', 'firebase_admin', 'billing']
    for name in names_to_fake:
        _orig_sys_modules[name] = sys.modules.get(name)

    # Fake firebase_functions
    firebase_functions = types.ModuleType('firebase_functions')
    firebase_functions.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
    sys.modules['firebase_functions'] = firebase_functions

    # Fake utils (create_json_response etc.)
    utils_mod = types.ModuleType('utils')

    def _fake_create_json_response(success: bool, payload: any, status_code: int):
        response_body = {"success": success, "payload": payload}
        return FakeResponse(response=json.dumps(response_body), status=status_code, headers={'Content-Type': 'application/json'})

    def _fake_get_api_key(llm_family=None):
        return 'DUMMY_KEY'

    def _fake_verify_firebase_token(req):
        return {}

    def _fake_get_request_json(req, strict=False):
        return req.get_json(silent=not strict)

    utils_mod.create_json_response = _fake_create_json_response
    utils_mod.get_api_key = _fake_get_api_key
    utils_mod.verify_firebase_token = _fake_verify_firebase_token
    utils_mod.get_request_json = _fake_get_request_json
    sys.modules['utils'] = utils_mod

    # Fake auth
    auth_mod = types.ModuleType('auth')
    auth_mod.validate_auth_key = lambda v: True
    sys.modules['auth'] = auth_mod

    # Fake openai module - will be patched into module under test
    openai_mod = types.ModuleType('openai')
    class DummyOpenAI:
        def __init__(self, api_key=None, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self
        def create(self, **params):
            raise NotImplementedError()
        def parse(self, **params):
            raise NotImplementedError()
    openai_mod.OpenAI = DummyOpenAI
    openai_mod.APIError = Exception
    sys.modules['openai'] = openai_mod

    # Fake billing
    billing_mod = types.ModuleType('billing')
    billing_mod.ensure_balance_positive = lambda db, user_id: (True, 100.0)
    billing_mod.calculate_cost = lambda model_id, in_t, out_t: 0.0
    billing_mod.bill_with_retry = lambda db, user_id, model_id, usage, cost, reason='usage': ("ok", 100.0)
    sys.modules['billing'] = billing_mod

    # Fake firebase_admin
    firebase_admin_mod = types.ModuleType('firebase_admin')
    firebase_admin_mod.firestore = types.SimpleNamespace(client=lambda: types.SimpleNamespace(), Client=type('Client', (), {}))
    sys.modules['firebase_admin'] = firebase_admin_mod

    # Import the package and module under test
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    functions_root = os.path.join(repo_root, 'functions')
    pkg_init = os.path.join(functions_root, 'api_v1_02', '__init__.py')
    spec_pkg = importlib.util.spec_from_file_location('api_v1_02', pkg_init)
    pkg = importlib.util.module_from_spec(spec_pkg)
    spec_pkg.loader.exec_module(pkg)
    sys.modules['api_v1_02'] = pkg

    module_path = os.path.join(functions_root, 'api_v1_02', '_openai_proxy.py')
    spec = importlib.util.spec_from_file_location('api_v1_02._openai_proxy', module_path)
    _openai = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_openai)

    # Cleanup sys.modules fakes after import
    for name, orig in _orig_sys_modules.items():
        if orig is None:
            try:
                del sys.modules[name]
            except KeyError:
                pass
        else:
            sys.modules[name] = orig

    # Prepare request with keyword in input
    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'call_type': 'create', 'call_params': {'model': 'gem-model', 'input': 'Hello ==SELECT_FILE_INSTRUCTIONS== world'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    # Fake client to capture params passed to create
    class FakeClient:
        last_create_params = None
        def __init__(self, api_key, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self
        def create(self, **params):
            FakeClient.last_create_params = params
            class FakeResp:
                def model_dump(self_inner, mode='json'):
                    return {'result': 'ok', 'received_model': params.get('model'), 'usage': {'input_tokens': 1, 'output_tokens': 2}}
            return FakeResp()

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='OPENAI-KEY'), \
         patch.object(_openai.openai, 'OpenAI', FakeClient):
        resp = _openai._openai_proxy(req)

    payload = _parse_response(resp)
    assert resp.status_code == 200
    assert payload['success'] is True
    assert FakeClient.last_create_params is not None
    inp = str(FakeClient.last_create_params.get('input', ''))
    assert ('Some instructions for selecting files' in inp) or ('files in my codebase' in inp)


def test_openai_parse_replacement_applied_to_input():
    # Similar setup as create test
    _orig_sys_modules = {}
    names_to_fake = ['firebase_functions', 'utils', 'auth', 'openai', 'firebase_admin', 'billing']
    for name in names_to_fake:
        _orig_sys_modules[name] = sys.modules.get(name)

    firebase_functions = types.ModuleType('firebase_functions')
    firebase_functions.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
    sys.modules['firebase_functions'] = firebase_functions

    utils_mod = types.ModuleType('utils')
    def _fake_create_json_response(success: bool, payload: any, status_code: int):
        response_body = {"success": success, "payload": payload}
        return FakeResponse(response=json.dumps(response_body), status=status_code, headers={'Content-Type': 'application/json'})
    def _fake_get_api_key(llm_family=None):
        return 'DUMMY_KEY'
    def _fake_verify_firebase_token(req):
        return {}
    def _fake_get_request_json(req, strict=False):
        return req.get_json(silent=not strict)
    utils_mod.create_json_response = _fake_create_json_response
    utils_mod.get_api_key = _fake_get_api_key
    utils_mod.verify_firebase_token = _fake_verify_firebase_token
    utils_mod.get_request_json = _fake_get_request_json
    sys.modules['utils'] = utils_mod

    auth_mod = types.ModuleType('auth')
    auth_mod.validate_auth_key = lambda v: True
    sys.modules['auth'] = auth_mod

    openai_mod = types.ModuleType('openai')
    class DummyOpenAI:
        def __init__(self, api_key=None, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self
        def create(self, **params):
            raise NotImplementedError()
        def parse(self, **params):
            raise NotImplementedError()
    openai_mod.OpenAI = DummyOpenAI
    openai_mod.APIError = Exception
    sys.modules['openai'] = openai_mod

    billing_mod = types.ModuleType('billing')
    billing_mod.ensure_balance_positive = lambda db, user_id: (True, 100.0)
    billing_mod.calculate_cost = lambda model_id, in_t, out_t: 0.0
    billing_mod.bill_with_retry = lambda db, user_id, model_id, usage, cost, reason='usage': ("ok", 100.0)
    sys.modules['billing'] = billing_mod

    firebase_admin_mod = types.ModuleType('firebase_admin')
    firebase_admin_mod.firestore = types.SimpleNamespace(client=lambda: types.SimpleNamespace(), Client=type('Client', (), {}))
    sys.modules['firebase_admin'] = firebase_admin_mod

    # Import package and module
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    functions_root = os.path.join(repo_root, 'functions')
    pkg_init = os.path.join(functions_root, 'api_v1_02', '__init__.py')
    spec_pkg = importlib.util.spec_from_file_location('api_v1_02', pkg_init)
    pkg = importlib.util.module_from_spec(spec_pkg)
    spec_pkg.loader.exec_module(pkg)
    sys.modules['api_v1_02'] = pkg

    module_path = os.path.join(functions_root, 'api_v1_02', '_openai_proxy.py')
    spec = importlib.util.spec_from_file_location('api_v1_02._openai_proxy', module_path)
    _openai = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_openai)

    for name, orig in _orig_sys_modules.items():
        if orig is None:
            try:
                del sys.modules[name]
            except KeyError:
                pass
        else:
            sys.modules[name] = orig

    headers = {_openai.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'call_type': 'parse', 'call_params': {'model': 'gem-model', 'input': 'Hello ==SELECT_FILE_INSTRUCTIONS==', 'text_format': 'FileSummaryModel'}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient2:
        last_parse_params = None
        def __init__(self, api_key, timeout=None):
            self.api_key = api_key
            self.timeout = timeout
            self.responses = self
        def parse(self, **params):
            FakeClient2.last_parse_params = params
            class FakeOutputParsed:
                def __init__(self, data):
                    self._data = data
                def dict(self):
                    return self._data
            class FakeResp:
                def __init__(self, data):
                    self.output_parsed = FakeOutputParsed(data)
                def model_dump(self_inner, mode='json'):
                    return {'usage': {'input_tokens': 1, 'output_tokens': 2}}
            parsed = {'result': 'ok', 'received_model': params.get('model')}
            return FakeResp(parsed)

    with patch.object(_openai, 'validate_auth_key', return_value=True), \
         patch.object(_openai, 'verify_firebase_token', return_value={}), \
         patch.object(_openai, 'get_api_key', return_value='OPENAI-KEY'), \
         patch.object(_openai.openai, 'OpenAI', FakeClient2):
        resp = _openai._openai_proxy(req)

    payload = _parse_response(resp)
    assert resp.status_code == 200
    assert payload['success'] is True
    assert FakeClient2.last_parse_params is not None
    inp = str(FakeClient2.last_parse_params.get('input', ''))
    assert ('Some instructions for selecting files' in inp) or ('files in my codebase' in inp)


# -----------------------------
# Tests for Generic proxy (v1_02)
# -----------------------------


def test_generic_create_replacement_applied_to_input():
    _orig_sys_modules = {}
    names_to_fake = ['firebase_functions', 'utils', 'auth', 'openai', 'firebase_admin', 'billing']
    for name in names_to_fake:
        _orig_sys_modules[name] = sys.modules.get(name)

    firebase_functions = types.ModuleType('firebase_functions')
    firebase_functions.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
    sys.modules['firebase_functions'] = firebase_functions

    utils_mod = types.ModuleType('utils')
    def _fake_create_json_response(success: bool, payload: any, status_code: int):
        response_body = {"success": success, "payload": payload}
        return FakeResponse(response=json.dumps(response_body), status=status_code, headers={'Content-Type': 'application/json'})
    def _fake_get_api_key(llm_family=None):
        return 'DUMMY_KEY'
    def _fake_verify_firebase_token(req):
        return {}
    def _fake_get_request_json(req, strict=False):
        return req.get_json(silent=not strict)
    utils_mod.create_json_response = _fake_create_json_response
    utils_mod.get_api_key = _fake_get_api_key
    utils_mod.verify_firebase_token = _fake_verify_firebase_token
    utils_mod.get_request_json = _fake_get_request_json
    sys.modules['utils'] = utils_mod

    auth_mod = types.ModuleType('auth')
    auth_mod.validate_auth_key = lambda v: True
    sys.modules['auth'] = auth_mod

    # Fake openai client
    openai_mod = types.ModuleType('openai')
    class DummyOpenAI:
        def __init__(self, base_url=None, api_key=None, timeout=None):
            self.base_url = base_url
            self.api_key = api_key
            self.timeout = timeout
            class Completions:
                def create(self, **params):
                    raise NotImplementedError()
                def parse(self, **params):
                    raise NotImplementedError()
            class Chat:
                def __init__(self):
                    self.completions = Completions()
            self.chat = Chat()
    openai_mod.OpenAI = DummyOpenAI
    openai_mod.APIError = Exception
    sys.modules['openai'] = openai_mod

    # Fake billing
    billing_mod = types.ModuleType('billing')
    billing_mod.ensure_balance_positive = lambda db, user_id: (True, 100.0)
    billing_mod.calculate_cost = lambda model_id, in_t, out_t: 0.0
    billing_mod.bill_with_retry = lambda db, user_id, model_id, usage, cost, reason='usage': ("ok", 100.0)
    sys.modules['billing'] = billing_mod

    # Fake firebase_admin
    firebase_admin_mod = types.ModuleType('firebase_admin')
    firebase_admin_mod.firestore = types.SimpleNamespace(client=lambda: types.SimpleNamespace(), Client=type('Client', (), {}))
    sys.modules['firebase_admin'] = firebase_admin_mod

    # Import package and module
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    functions_root = os.path.join(repo_root, 'functions')
    pkg_init = os.path.join(functions_root, 'api_v1_02', '__init__.py')
    spec_pkg = importlib.util.spec_from_file_location('api_v1_02', pkg_init)
    pkg = importlib.util.module_from_spec(spec_pkg)
    spec_pkg.loader.exec_module(pkg)
    sys.modules['api_v1_02'] = pkg

    module_path = os.path.join(functions_root, 'api_v1_02', '_generic_proxy.py')
    spec = importlib.util.spec_from_file_location('api_v1_02._generic_proxy', module_path)
    _generic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_generic)

    for name, orig in _orig_sys_modules.items():
        if orig is None:
            try:
                del sys.modules[name]
            except KeyError:
                pass
        else:
            sys.modules[name] = orig

    headers = {_generic.AUTH_HEADER_NAME: 'ok'}
    req_payload = {'llm_family': 'openai', 'call_type': 'create', 'call_params': {'model': 'gem-model', 'input': 'Hello ==SELECT_FILE_INSTRUCTIONS=='}}
    req = DummyRequest(headers=headers, method='POST', json_data=req_payload)

    class FakeClient:
        last_create_params = None
        def __init__(self, base_url=None, api_key=None, timeout=None):
            self.base_url = base_url
            self.api_key = api_key
            class Completions:
                def create(self_inner, **params):
                    FakeClient.last_create_params = params
                    class FakeResp:
                        def model_dump(self_inner2, mode='json'):
                            return {'result': 'ok', 'received_model': params.get('model'), 'usage': {'prompt_tokens': 1, 'completion_tokens': 2}}
                    return FakeResp()
                def parse(self_inner, **params):
                    raise NotImplementedError()
            class Chat:
                def __init__(self):
                    self.completions = Completions()
            self.chat = Chat()

    with patch.object(_generic, 'validate_auth_key', return_value=True), \
         patch.object(_generic, 'verify_firebase_token', return_value={}), \
         patch.object(_generic, 'get_api_key', return_value='GENERIC-KEY'), \
         patch.object(_generic.openai, 'OpenAI', FakeClient):
        resp = _generic._generic_proxy(req)

    payload = _parse_response(resp)
    assert resp.status_code == 200
    assert payload['success'] is True
    assert FakeClient.last_create_params is not None
    inp = str(FakeClient.last_create_params.get('input', ''))
    assert ('Some instructions for selecting files' in inp) or ('files in my codebase' in inp)


# -----------------------------
# Tests for Gemini proxy (v1_02)
# -----------------------------


def test_gemini_generate_content_replacement_applied_to_contents():
    _orig_sys_modules = {}
    names_to_fake = ['firebase_functions', 'utils', 'auth', 'google', 'google.genai', 'google.genai.types', 'firebase_admin', 'billing']
    for name in names_to_fake:
        _orig_sys_modules[name] = sys.modules.get(name)

    firebase_functions = types.ModuleType('firebase_functions')
    firebase_functions.https_fn = types.SimpleNamespace(Request=object, Response=FakeResponse)
    sys.modules['firebase_functions'] = firebase_functions

    # Fake utils
    utils_mod = types.ModuleType('utils')
    def _fake_create_json_response(success: bool, payload: any, status_code: int):
        response_body = {"success": success, "payload": payload}
        return FakeResponse(response=json.dumps(response_body), status=status_code, headers={'Content-Type': 'application/json'})
    def _fake_get_api_key(llm_family=None):
        return 'DUMMY_KEY'
    def _fake_verify_firebase_token(req):
        return {}
    def _fake_get_request_json(req, strict=False):
        return req.get_json(silent=not strict)
    utils_mod.create_json_response = _fake_create_json_response
    utils_mod.get_api_key = _fake_get_api_key
    utils_mod.verify_firebase_token = _fake_verify_firebase_token
    utils_mod.get_request_json = _fake_get_request_json
    sys.modules['utils'] = utils_mod

    auth_mod = types.ModuleType('auth')
    auth_mod.validate_auth_key = lambda v: True
    sys.modules['auth'] = auth_mod

    # Fake google.genai types
    google_mod = types.ModuleType('google')
    genai_mod = types.ModuleType('google.genai')
    types_mod = types.ModuleType('google.genai.types')

    class DummyGenerateContentConfig:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    class DummyContent:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    types_mod.GenerateContentConfig = DummyGenerateContentConfig
    types_mod.Content = DummyContent

    class DummyClient:
        def __init__(self, api_key):
            self.api_key = api_key
            class Models:
                def generate_content(self_inner, **params):
                    raise NotImplementedError()
            self.models = Models()

    genai_mod.Client = DummyClient
    genai_mod.types = types_mod
    google_mod.genai = genai_mod

    sys.modules['google'] = google_mod
    sys.modules['google.genai'] = genai_mod
    sys.modules['google.genai.types'] = types_mod

    billing_mod = types.ModuleType('billing')
    billing_mod.ensure_balance_positive = lambda db, user_id: (True, 100.0)
    billing_mod.calculate_cost = lambda model_id, in_t, out_t: 0.0
    billing_mod.bill_with_retry = lambda db, user_id, model_id, usage, cost, reason='usage': ("ok", 100.0)
    sys.modules['billing'] = billing_mod

    firebase_admin_mod = types.ModuleType('firebase_admin')
    firebase_admin_mod.firestore = types.SimpleNamespace(client=lambda: types.SimpleNamespace(), Client=type('Client', (), {}))
    sys.modules['firebase_admin'] = firebase_admin_mod

    # Import package and module
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    functions_root = os.path.join(repo_root, 'functions')
    pkg_init = os.path.join(functions_root, 'api_v1_02', '__init__.py')
    spec_pkg = importlib.util.spec_from_file_location('api_v1_02', pkg_init)
    pkg = importlib.util.module_from_spec(spec_pkg)
    spec_pkg.loader.exec_module(pkg)
    sys.modules['api_v1_02'] = pkg

    module_path = os.path.join(functions_root, 'api_v1_02', '_gemini_proxy.py')
    spec = importlib.util.spec_from_file_location('api_v1_02._gemini_proxy', module_path)
    _gemini = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_gemini)

    # Restore sys.modules
    for name, orig in _orig_sys_modules.items():
        if orig is None:
            try:
                del sys.modules[name]
            except KeyError:
                pass
        else:
            sys.modules[name] = orig

    headers = {_gemini.AUTH_HEADER_NAME: 'ok'}
    json_params = {'model': 'gem-model', 'contents': 'Hello ==SELECT_FILE_INSTRUCTIONS==', 'config': {}}
    req = DummyRequest(headers=headers, method='POST', json_data=json_params)

    # Fake client to capture generate_content params
    class FakeModels:
        last_params = None
        def generate_content(self, **params):
            FakeModels.last_params = params
            class FakeResp:
                def to_json_dict(self_inner):
                    return {'result': 'ok'}
                @property
                def usage_metadata(self_inner):
                    return types.SimpleNamespace(prompt_token_count=1, total_token_count=2)
            return FakeResp()

    class FakeClient2:
        def __init__(self, api_key):
            self.api_key = api_key
            self.models = FakeModels()

    with patch.object(_gemini, 'validate_auth_key', return_value=True), \
         patch.object(_gemini, 'verify_firebase_token', return_value={}), \
         patch.object(_gemini, 'get_api_key', return_value='GEMINI-KEY'), \
         patch.object(_gemini.genai, 'Client', FakeClient2):
        resp = _gemini._gemini_proxy(req)

    payload = _parse_response(resp)
    assert resp.status_code == 200
    assert payload['success'] is True
    assert FakeModels.last_params is not None
    # contents might be passed as string or list depending on implementation; check string presence
    assert ('Some instructions for selecting files' in str(FakeModels.last_params.get('contents'))) or ('files in my codebase' in str(FakeModels.last_params.get('contents')))
