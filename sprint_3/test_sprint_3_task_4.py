import pytest

from sprint_3_task_4 import greedy, counting


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected_result",
    [
        ([0], [0], 1),
        ([1], [0], 0),
        ([1], [1], 1),

        ([1, 2], [1], 1),
        ([1, 2], [1, 1], 1),

        ([1, 2], [1, 2, 3], 2),
        ([1, 2, 2], [1, 2, 3], 3),

        ([1, 2, 4], [1, 2, 3], 2),
        ([1, 3, 4], [1, 2, 3], 2),

        ([1, 4, 4], [2, 3], 1),
        ([1, 2, 3], [1, 1], 1),
    ],
)
def test_greedy(test_input_1, test_input_2, expected_result):
    test_out = greedy(test_input_1, test_input_2)
    assert test_out == expected_result


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected_result_1, expected_result_2",
    [
        ([0], [0], [0], [0]),
        ([1], [0], [1], [0]),
        ([1], [1], [1], [1]),

        ([1, 2], [2, 1], [1, 2], [1, 2]),
        ([3, 2, 1], [2, 1], [1, 2, 3], [1, 2]),
        ([2, 3, 1], [1, 2], [1, 2, 3], [1, 2]),
        ([2, 1, 3], [1, 1], [1, 2, 3], [1, 1]),
    ],
)
def test_counting(test_input_1, test_input_2, expected_result_1, expected_result_2):
    counting(test_input_1, test_input_2)
    assert test_input_1 == expected_result_1 and test_input_2 == expected_result_2
