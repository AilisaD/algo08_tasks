
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
Т.е. бинарный поиск будет корректно работать для каждого массива по отдельности.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Считывание массива и нахождение индекса сдвига происходит за O(n).
Операция бинарного поиска выполняется за O(log(n)).


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Т.к. мы храним все элементы в массиве размером n и храним индекс сдвига,
то пространственная сложность будет O(n+1) => O(n).
"""


def binary_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def main():
    array = []
    idx_shift = -1
    num = ""
    with open('input.txt') as reader:
        next(reader)
        x = int(reader.readline())
        byte = reader.read(1)

        while byte:
            if byte == " ":
                array.append(int(num))
                num = ""
                if array[len(array) - 1] < array[len(array) - 2]:
                    idx_shift = len(array) - 1
            num += byte
            byte = reader.read(1)
        array.append(int(num))

        if array[len(array) - 1] < array[len(array) - 2]:
            idx_shift = len(array) - 1

    idx_x = -1

    if idx_shift == -1:
        idx_x = binary_search(array, x,  0, len(array))
    elif array[0] <= x <= array[idx_shift - 1]:
        idx_x = binary_search(array, x, 0, idx_shift)
    elif array[idx_shift] <= x:
        idx_x = binary_search(array, x, idx_shift, len(array))

    with open('output.txt', 'w') as writer:
        writer.write(str(idx_x))


if __name__ == "__main__":
    main()
