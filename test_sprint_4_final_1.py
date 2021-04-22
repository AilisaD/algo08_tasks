import pytest

from sprint_4_final_1 import create_dict_words, counting_relevance


@pytest.mark.parametrize(
    "files, requests, answer",
    [
        (
            [
                'i love coffee',
                'coffee with milk and sugar',
                'free tea for everyone'
            ],
            [
                'i like black coffee without milk',
                'everyone loves new year',
                'mary likes black coffee without milk',
            ],
            [['1', '2'], ['3'], ['2', '1']]
        ),
        (
            [
                'i love coffee',
                'coffee with milk and sugar',
                'free tea for everyone'
            ],
            [
                'i like black coffee without milk',
                'true',
                'everyone loves new year',
                'mary likes black coffee without milk',
            ],
            [['1', '2'], ['3'], ['2', '1']]
        ),
        (
            [
                'buy flat in moscow',
                'rent flat in moscow',
                'sell flat in moscow',
                'want flat in moscow like crazy',
                'clean flat in moscow on weekends',
                'renovate flat in moscow',
            ],
            [
                'flat in moscow for crazy weekends'
            ],
            [['4', '5', '1', '2', '3']]
        ),
        (
            [
                'i love coffee',
                'crazy moscow',
                'coffee with milk and sugar',
                'free tea for everyone',
                'false is true'
            ],
            [
                'rent flat in moscow',
                'sell flat in moscow',
                'false',
                'true',
                'coffee in moscow'
            ],
            [['2'], ['2'], ['5'], ['5'], ['1', '2', '3']]
        )
    ],
)
def test_merge_sort(files, requests, answer):
    count_words_inputs = {}
    for i, f in enumerate(files):
        line = f.split()
        create_dict_words(count_words_inputs, i + 1, line)
    ans = []
    for request in requests:
        relevance = counting_relevance(count_words_inputs, request.split())
        ans.append(relevance)
    assert ans == answer
