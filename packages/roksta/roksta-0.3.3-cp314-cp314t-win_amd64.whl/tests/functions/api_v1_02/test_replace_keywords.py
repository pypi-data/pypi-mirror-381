import os
import sys
import importlib.util
import types

# Ensure the functions/ directory is importable as a top-level module location
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FUNCTIONS_DIR = os.path.join(PROJECT_ROOT, 'functions')
if FUNCTIONS_DIR not in sys.path:
    sys.path.insert(0, FUNCTIONS_DIR)

# Load the keyword_map module from the v1_02 package
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
functions_root = os.path.join(repo_root, 'functions')
module_path = os.path.join(functions_root, 'api_v1_02', 'replace_keywords.py')
spec = importlib.util.spec_from_file_location('api_v1_02.replace_keywords', module_path)
_replace_keywords = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_replace_keywords)

replace_keywords = _replace_keywords.replace_keywords
KEYWORD_MAP = _replace_keywords.KEYWORD_MAP


def test_recursive_replacement_nested_structures():
    obj = {
        'input': 'Hello ' + list(KEYWORD_MAP.keys())[0] + ' world',
        'messages': [
            {'content': 'First ' + list(KEYWORD_MAP.keys())[0] + ' end'},
            {'content': 'no change'}
        ],
        'nested': {'list': ['prefix ' + list(KEYWORD_MAP.keys())[0] + ' suffix', 123]},
        'tuple': ('a ' + list(KEYWORD_MAP.keys())[0] + ' b',),
        'obj': types.SimpleNamespace(text=list(KEYWORD_MAP.keys())[0] + ' inside', number=7)
    }

    result = replace_keywords(obj)

    expected_replacement = list(KEYWORD_MAP.values())[0]
    assert expected_replacement in result['input']
    assert expected_replacement in result['messages'][0]['content']
    assert expected_replacement in result['nested']['list'][0]
    assert expected_replacement in result['tuple'][0]
    assert expected_replacement in result['obj'].text


def test_multiple_occurrences_replaced_everywhere():
    key = list(KEYWORD_MAP.keys())[0]
    val = list(KEYWORD_MAP.values())[0]
    s = f"{key} and {key} again"
    out = replace_keywords(s)
    assert out == f"{val} and {val} again"


def test_case_sensitivity_no_match_for_different_case():
    key = list(KEYWORD_MAP.keys())[0]
    lower_key = key.lower()
    s = f"This {lower_key} should remain"
    out = replace_keywords(s)
    assert out == s


def test_unknown_keywords_left_unchanged():
    s = 'This contains ==UNKNOWN_KEYWORD== and should remain.'
    out = replace_keywords(s)
    assert out == s


def test_non_string_values_unchanged():
    data = {'n': 42, 'f': 3.14, 'b': True, 'none': None}
    out = replace_keywords(data)
    assert out['n'] == 42
    assert out['f'] == 3.14
    assert out['b'] is True
    assert out['none'] is None
