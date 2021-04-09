import pytest

from sprint_3_task_12 import find_day


@pytest.mark.parametrize(
    "test_input, x, expected_result",
    [
        ([0], 0, ['1 -1']),
        ([1], 0, ['1 -1']),
        ([1], 1, ['1', '-1']),
        ([1], 2, ['-1 -1']),

        ([1, 2], 0, ['1 2']),
        ([1, 2], 2, ['2', '-1']),
        ([1, 2], 3, ['-1 -1']),
        ([1, 2], 3, ['-1 -1']),

        ([1, 2, 3, 4, 5], 0, ['1 2']),

        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, ['3', '6']),
        ([1, 2, 3, 4, 4, 4, 7, 8, 9], 3, ['3', '7']),
        ([1, 2, 3, 4, 4, 4, 7, 8, 9], 2, ['2', '4']),

        ([0, 0, 0, 2, 3, 4], 0, ['1 2']),
        ([0, 0, 0, 0, 0, 0], 1, ['-1 -1']),
        ([4, 4, 4, 4, 4, 4], 4, ['1', '-1']),

        ([1, 2, 3, 4, 5, 6], 7, ['-1 -1']),

        ([4, 5, 7, 10, 20, 21], 2, ['1', '1']),
        ([4, 6, 7, 10, 20, 21], 3, ['1', '2']),
        ([4, 4, 6, 10, 20, 21], 3, ['1', '3']),
    ],
)
def test_find_day(test_input, x, expected_result):
    test_out = find_day(test_input, x,  0, len(test_input))
    assert test_out == expected_result
