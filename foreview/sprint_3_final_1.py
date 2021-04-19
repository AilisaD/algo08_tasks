# 50443919

"""
-- ПРИНЦИП РАБОТЫ --
Для решения задачи поиска за время O(log(n)) подходит бинарный поиск.
Но для этого нужен полностью отсортированный массив.

По задаче, массив отсортирован, но со сдвигом.
Т.е. состоит из 2-х отсортированных частей: [4, 5, 6, 1, 2].

При считывании массива из файла я нахожу индекс элемента,
с которого начинается вторая отсортированная часть (idx_shift).

Если таковой не нашлось, то ищу бинарным поиском по всему массиву.
Если есть сдвиг, то смотрю,
в какой из частей масива лежит искомый элемент
и запускаю бинарный поиск по ней.

-- ДОКАЗАТЕЛЬСВО КОРРЕКТНОСТИ --
Когда мы знаем индекс сдвига, то можем говорить о двух отсортированных массивах
в диапазонах: [0; idx_shift) и [idx_shift; n).
Т.е. бинарный поиск будет корректно работать для каждого массива
по отдельности.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Считывание массива и нахождение индекса сдвига происходит за O(n).
Операция бинарного поиска выполняется за O(log(n)).


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Т.к. мы храним все элементы в массиве размером n и храним индекс сдвига,
то пространственная сложность будет O(n).
"""


def binary_search(arr: list, x: int, left: int, right: int):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def run_search(array: list, idx_shift: int, x: int):
    if idx_shift == -1:
        return binary_search(array, x, 0, len(array))
    elif array[0] <= x <= array[idx_shift - 1]:
        return binary_search(array, x, 0, idx_shift)

    return binary_search(array, x, idx_shift, len(array))


def read_from_file():
    array = []
    idx_shift = -1
    num = ""

    with open('input.txt') as reader:
        next(reader)
        x = int(reader.readline())
        byte = reader.read(1)

        while byte:
            if byte != " ":
                num += byte
                byte = reader.read(1)
                continue

            array.append(int(num))
            num = ""
            if array[len(array) - 1] < array[len(array) - 2]:
                idx_shift = len(array) - 1
            byte = reader.read(1)

        array.append(int(num))
        if array[len(array) - 1] < array[len(array) - 2]:
            idx_shift = len(array) - 1

    return array, idx_shift, x


def main():
    array, idx_shift, x = read_from_file()
    idx_x = run_search(array, idx_shift, x)

    with open('output.txt', 'w') as writer:
        writer.write(str(idx_x))


if __name__ == "__main__":
    main()
