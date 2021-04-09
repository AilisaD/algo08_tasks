import pytest

from sprint_3_final_1 import search


@pytest.mark.parametrize(
    "test_input, x, expected_result",
    [
        ([1], 1, 0),
        ([2, 1], 1, 1),
        ([1, 2], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 3),
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 5, 6),
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 21, 1),
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 50, -1),
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 1, 4),

        ([19, 21, 100, 101, 103, 105, 106, 107, 1, 4, 5, 7, 12], 19, 0),
        ([19, 21, 100, 101, 103, 105, 106, 107, 1, 4, 5, 7, 12], 105, 5),
        ([19, 21, 100, 101, 103, 105, 106, 107, 1, 4, 5, 7, 12], 107, 7),
        ([19, 21, 100, 101, 103, 105, 106, 107, 1, 4, 5, 7, 12], 12, 12),
        ([19, 21, 100, 101, 103, 105, 106, 107, 1, 4, 5, 7, 12], 1, 8),

        ([19, 21, 100, 1, 4, 5, 7, 12, 13, 14, 15, 16], 105, -1),
        ([19, 21, 100, 1, 4, 5, 7, 12, 13, 14, 15, 16], 19, 0),
        ([19, 21, 100, 1, 4, 5, 7, 12, 13, 14, 15, 16], 100, 2),
        ([19, 21, 100, 1, 4, 5, 7, 12, 13, 14, 15, 16], 1, 3),
        ([19, 21, 100, 1, 4, 5, 7, 12, 13, 14, 15, 16], 13, 8),
        ([19, 21, 100, 1, 4, 5, 7, 12, 13, 14, 15, 16], 14, 9),
    ],
)
def test_search(test_input, x, expected_result):
    assert search(test_input, x, 0, len(test_input)) == expected_result
