import pytest

from sprint_4_task_3 import hash_substring, poly_hash_table


@pytest.mark.parametrize(
    "a, m, s, left, right, expected_result",
    [
        (1000, 1000009, 'abcdefgh', 1, 1, '97\n'),
        (1000, 1000009, 'abcdefgh', 1, 5, '225076\n'),
        (1000, 1000009, 'abcdefgh', 2, 3, '98099\n'),
        (1000, 1000009, 'abcdefgh', 3, 4, '99100\n'),
        (1000, 1000009, 'abcdefgh', 4, 4, '100\n'),
    ],
)
def test_merge_sort(a, m, s, left, right, expected_result):
    table = poly_hash_table(a, m, s, len(s)+1)
    assert hash_substring(m, table, left, right) == expected_result
