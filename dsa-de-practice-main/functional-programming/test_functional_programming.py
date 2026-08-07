import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_data = importlib.import_module('data_transformations_list_comprehensions')

data_transformations = mod_data.data_transformations


class TestDataTransformations:
    def test_placeholder_raises(self):
        with pytest.raises(NotImplementedError):
            data_transformations([{'id': 1, 'value': 10}])

    def test_placeholder_docstring(self):
        assert 'DE reframing' in data_transformations.__doc__