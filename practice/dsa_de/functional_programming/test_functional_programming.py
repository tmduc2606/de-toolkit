import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_001 = importlib.import_module('001_data_transformations_list_comprehensions')

data_transformations = mod_001.data_transformations

ORDERS = [
    {"item_id": "a", "quantity": 2, "unit_price": 10.0},
    {"item_id": "b", "quantity": 1, "unit_price": 5.0},
    {"item_id": "c", "quantity": -3, "unit_price": 10.0},
    {"item_id": "d", "quantity": 0, "unit_price": 7.0},
    None,
]


class TestDataTransformations:
    def test_filters_and_projects(self):
        result = data_transformations(ORDERS)
        assert result["valid_records"] == [
            {"item_id": "a", "quantity": 2, "unit_price": 10.0},
            {"item_id": "b", "quantity": 1, "unit_price": 5.0},
        ]
        assert result["transformed"] == [
            {"item_id": "a", "total": 20.0},
            {"item_id": "b", "total": 5.0},
        ]

    def test_aggregate(self):
        assert data_transformations(ORDERS)["grand_total"] == 25.0

    def test_normal_like_concept_ordering(self):
        rows = [{"quantity": 4, "unit_price": 2.5}]
        assert data_transformations(rows)["grand_total"] == 10.0

    def test_empty(self):
        result = data_transformations([])
        assert result == {"valid_records": [], "transformed": [], "grand_total": 0}