"""DuckDB-free pytest suite for the digit-math concept.

Normal / edge / empty cases per docs/OVERHAUL_BLUEPRINT.md §4 Flow A.
"""
import csv
import importlib
import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_3622 = importlib.import_module(
    "3622_check_divisibility_by_digit_sum_and_product_digit_checksum"
)
passes_digit_checksum = mod_3622.passes_digit_checksum
valid_checksum_ids = mod_3622.valid_checksum_ids

SAMPLE_DATA = pathlib.Path(__file__).parent / "data" / "record_ids.csv"


class TestPassesDigitChecksum:
    # --- normal ---
    def test_leetcode_example_true(self):
        # 99: digit_sum 18 + digit_prod 81 = 99 -> 99 % 99 == 0
        assert passes_digit_checksum(99)

    def test_leetcode_example_false(self):
        # 23: digit_sum 5 + digit_prod 6 = 11 -> 23 % 11 != 0
        assert not passes_digit_checksum(23)

    # --- edge ---
    def test_single_digit_id(self):
        # 5: digit_sum 5 + digit_prod 5 = 10 -> 5 % 10 != 0
        assert not passes_digit_checksum(5)

    def test_zero_digit_collapses_product(self):
        # 10: digit_prod becomes 0, so the divisor is digit_sum alone (1);
        # any n % 1 == 0 -> True. Guards against a 0-seeded product bug.
        assert passes_digit_checksum(10)

    def test_smallest_input(self):
        # 1: digit_sum 1 + digit_prod 1 = 2 -> 1 % 2 != 0
        assert not passes_digit_checksum(1)


class TestValidChecksumIds:
    def test_normal_batch(self):
        assert valid_checksum_ids([99, 23]) == [99]

    def test_mixed_batch_preserves_order(self):
        assert valid_checksum_ids([5, 10, 23, 99, 108]) == [10, 99, 108]

    # --- empty ---
    def test_empty_batch(self):
        assert valid_checksum_ids([]) == []

    def test_sample_data_batch(self):
        with open(SAMPLE_DATA, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            ids = [int(row["record_id"]) for row in reader]
        assert valid_checksum_ids(ids) == [99, 10, 108]