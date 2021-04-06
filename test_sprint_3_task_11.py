import pytest
import random

from sprint_3_task_11 import merge_sort


@pytest.mark.parametrize(
    "test_input, expected_result, n",
    [
        ([], [], 0),
        ([1], [1], 1),
        ([-1], [-1], 1),
        ([1, 2], [1, 2], 2),
        ([2, 1], [2, 1], 1),
        ([1, -2], [-2, 1], 2),
        ([2, 1, 3], [1, 2, 3], 3),
        ([-2, 1, -3], [-2, 1, -3], 2),
        ([3, 3, 3, 3], [3, 3, 3, 3], 2),
        ([0, 1, 0, 1, 4, 3], [0, 0, 1, 1, 4, 3], 4),
    ],
)
def test_merge_sort(test_input, expected_result, n):
    merge_sort(test_input, 0, n)
    assert test_input == expected_result
