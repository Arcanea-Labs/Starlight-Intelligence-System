import importlib
import pytest

@pytest.mark.parametrize('module', ['agents', 'connectors', 'core'])
def test_imports(module):
    """Ensure that project modules can be imported."""
    importlib.import_module(module)
