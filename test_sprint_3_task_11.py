import pytest

from sprint_3_task_11 import merge_sort


@pytest.mark.parametrize(
    "test_input, expected_result, s, n",
    [
        ([], [], 0, 0),

        ([1], [1], 0, 1),
        ([-1], [-1], 0, 1),

        ([1, 2], [1, 2], 0, 2),
        ([2, 1], [2, 1], 0, 1),
        ([1, -2], [-2, 1], 0, 2),

        ([2, 1, 3], [1, 2, 3], 0, 3),
        ([-2, 1, -3], [-2, 1, -3], 0, 2),
        ([3, 3, 3, 3], [3, 3, 3, 3], 0, 2),

        ([0, 1, 0, 1, 4, 3], [0, 0, 1, 1, 4, 3], 0, 4),
        ([0, 1, 0, 1, 4, 3], [0, 1, 0, 1, 4, 3], 2, 5),
    ],
)
def test_merge_sort(test_input, expected_result, s, n):
    merge_sort(test_input, s, n)
    assert test_input == expected_result
