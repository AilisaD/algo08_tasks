# 50948901

"""
-- ПРИНЦИП РАБОТЫ --
Для вывода топ-5 файлов по релевантности сначала создаем словарь слов.
Для каждого слова создаем словарь файлов (номеров, начиная с 1)
с количеством вхожений этого слова в название файла.
    Для файлов:
    1 - i love coffee
    2 - with coffee with milk
    получится словарь:
    {
     'i':{1: 1},
     'love': {1: 1},
     'coffee': {1: 1, 2: 1},
     'with': {2: 2},
     'milk': {2: 1}
    }

Далее, по каждому запросу (оставляем в нем только уникальные слова)
находим все файлы, в названии которых есть слова из запроса, и
суммируем релевантность для одинаковых номеров файлов.
Получем словарь с номерами файлов и их релевантностью.
Для запроса
 - like black coffee without milk
словарь будет выглядеть так:
    {1: 1, 2: 2}

Дальше сортируем словарь по релевантноти и номеру файла.
    2: 2, 1: 1

-- ДОКАЗАТЕЛЬСВО КОРРЕКТНОСТИ --
Идя по каждому слову в запросе, мы выбираем словари
    {файл: релевантность}
и как бы делаем операцию сложения для них,
т.е. у файлов с одним номером релевантность проссумируется.
И в итоге получим словарь с уникальными номерами файлов,
которые точно хотя бы одним словом походят запросу,
и их итоговой релевантность.
В этом случае достаточно отсортировать по 2-м ключам
и взять первые 5 элементов.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сначала мы составляем словарь слов за O(n*l),
где n - число файлов,
l - длина названий файлов.
Проход по каждому запросу и нахождению релевантных файлов
будет происходить за O(m*k*f), где m - число запросов,
k - число слов в запросе, f - число файлов, для каждого слова в запросе.
все операции
O(n*l) + O(m*k*f) = O((n*l)+(m*k*f))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В памяти хранится словарь слов O(n*l), список запросов O(m).
O(n*l) + O(m) = O((n*l)+m)

"""

from operator import itemgetter
from collections import defaultdict, Counter


def counting_word_inputs(dict_words_count: dict, file: list, i: int):
    """
    Функия заносит в словарь количество вхождений слов в название каждого файла.
    :param dict_words_count: словарь слов
    {word: {num_file_1: count, num_file_2: count}}
    :param file: название файла в виде списка слов
    :param i: номер файла
    """
    for word in file:
        dict_words_count[word][i + 1] = Counter(file)[word]


def counting_relevance_in_file(dict_word: dict, rel_files: dict):
    """
    Функция подсчета релевантности для каждого файла, для одинаковых суммируем.
    :param dict_word: словарь файлов для одного слова с их релевантностью.
    :param rel_files: словарь с номерами файлов и их релевантностью для запроса.
    """
    for file in dict_word:
        if file not in rel_files:
            rel_files[file] = 0

        rel_files[file] += dict_word[file]


def sorting(rel_files: dict) -> str:
    """
    Функция сортирует словарь релевантных файлов
    по их релевантности и номеру файла и преобразует топ-5 файлов к строке,
    содержащей только номер файла.
    :param rel_files: словарь с номерами файлов и их релевантностью.
    :return: строку номеров топ-5 релевантных файлов.
    """
    return " ".join((f'{x[0]}' for x in
                     sorted(
                         [(k, -v) for k, v in rel_files.items()],
                         key=itemgetter(1, 0)
                     )[:5]))


def counting_relevance_files(word_count: dict, request: set) -> dict:
    """
    Функция для нахождения всех файлов, в названии которых есть слова из запроса,
    и подсчета их релевантности.
    :param word_count: словарь файлов с их релевантностью.
    :param request: запрос очищенный от повторов.
    :return: словарь с номерами файлов и их релевантностью для запроса.
    """
    rel_files = {}
    for word in request:
        if word in word_count:
            counting_relevance_in_file(word_count[word], rel_files)
    return rel_files


def counting_relevance(dict_words_count: dict, requests: list) -> str:
    """
    Функция для нахождения топ-5 релевантных файлов для запросов.
    :param dict_words_count: словарь слов, содержащихся в названии файлов.
    :param requests: список запросов.
    :return: строка с номерами релевантных файлов на все запросы.
    """
    relevance = defaultdict()
    ans = ""

    for i, request in enumerate(requests):

        if request in relevance:
            ans += f'{relevance[request]}\n'
            continue

        rel = counting_relevance_files(dict_words_count, set(request.split()))

        if len(rel) != 0:
            relevance[request] = sorting(rel)
            ans += f'{relevance[request]}\n'

    return ans


def main():
    dict_words_count = defaultdict(defaultdict)
    requests = []
    with open("input.txt", "r") as fr:
        n = int(fr.readline())
        for i in range(n):
            file = fr.readline().split()
            counting_word_inputs(dict_words_count, file, i)

        m = int(fr.readline())
        for i in range(m):
            requests.append(fr.readline())

    ans = counting_relevance(dict_words_count, requests)

    with open("output.txt", "w") as fw:
        fw.write(ans)


if __name__ == "__main__":
    main()
