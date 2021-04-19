# 50444244

"""
-- ПРИНЦИП РАБОТЫ --
По заданию необходиом реализовать быструю сортиировку
с ограничением на пространственную сложность O(n) - модификация in-place.
Т.е. не создаем массивы для элементов меньше, больше и равные опорному.

Сортировать необходимо элементы массива, состоящие из строки и 2-х чисел:
    ('asc', 1, 2)

Сначала сортировка идет по arr[1] (по убыванию),
если по нему элементы равны, то смотрим на arr[2] (сортируем по возрастанию),
если оба числа у сравниваемых элементов равны, то ставим элементы
в лексикографическом порядке по строке в arr[0].

-- ДОКАЗАТЕЛЬСВО КОРРЕКТНОСТИ --
В функции partition() нет создания дополнительных списков,
что отвечает требованию по памяти O(n).

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность быстрой сортировки O(n*log(n)).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Т.к. мы храним все элементы в массиве размером n,
то пространственная сложность будет O(n).
"""


def partition(arr: list, left: int, right: int):
    pivot = left

    for i in range(left + 1, right + 1):
        if arr[i][1] > arr[left][1]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

        if arr[i][1] == arr[left][1]:
            if arr[i][2] < arr[left][2]:
                arr[i], arr[left] = arr[left], arr[i]

            elif arr[i][2] == arr[left][2] and arr[i][0] < arr[left][0]:
                arr[left], arr[i] = arr[i], arr[left]

    arr[pivot], arr[left] = arr[left], arr[pivot]
    return pivot


def quicksort(array: list, left: int = 0, right: int = None):
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    pivot = partition(array, left, right)
    quicksort(array, left, pivot - 1)
    quicksort(array, pivot + 1, right)


def main():
    table_student = []

    with open("input.txt") as reader:
        n = int(reader.readline())
        for i in range(n):
            name, tasks, penalty = reader.readline().strip().split()
            table_student.append((name, int(tasks), int(penalty)))

    quicksort(table_student)

    with open("output.txt", "w") as writer:
        writer.write("\n".join((name for name, _, _ in table_student)))


if __name__ == "__main__":
    main()
