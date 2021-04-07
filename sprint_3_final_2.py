
"""
-- ПРИНЦИП РАБОТЫ --
По заданию необходиом реализовать быструю сортиировку
с ограничением на пространственную сложность O(n) - модификация in-place.
Т.е. не создаем массивы для элементов меньше, больше и равные опорному.

Сортировать необходимо элементы массива, состоящие из строки и 2-х чисел:
    ['asc', 1, 2]

Сначала сортировка идет по arr[1] (по убыванию),
если по нему элементы равны, то смотрим на arr[2] (сортируем по возрастанию),
если оба числа у сравниваемых элементов равны, то ставим элементы
в лексикографическом порядке по строке в arr[0] (использовала встроеную sorted()).

-- ДОКАЗАТЕЛЬСВО КОРРЕКТНОСТИ --
В функции partition() нет создания дополнительных списков, что отвечает требованию
по памяти O(n).

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность быстрой сортировки O(n*log(n)).
Втренная функция sorted() работает за O(n*log(n)) - в нее всегда передается список
из 2-х элементов строк длинной m. Получается, что она работает за
O(2*m*(log(2) + log(m)) ) => O(m*log(m))
В итоге получается временная сложность O(n*log(n) + m*log(m))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Т.к. мы храним все элементы в массиве размером n,
то пространственная сложность будет O(n).
"""


def partition(array, left, right):
    pivot = left

    for i in range(left+1, right+1):
        if array[i][1] > array[left][1]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

        if array[i][1] == array[left][1]:
            if array[i][2] < array[left][2]:
                array[i], array[left] = array[left], array[i]

            elif array[i][2] == array[left][2]:
                array[left], array[i] = sorted([array[i], array[left]],
                                               key=lambda x: x[0])
    array[pivot], array[left] = array[left], array[pivot]
    return pivot


def quicksort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    pivot = partition(array, left, right)
    quicksort(array, left, pivot - 1)
    quicksort(array, pivot + 1, right)


def main():
    table_student = []

    with open('input.txt') as reader:
        n = int(reader.readline())
        for i in range(n):
            name, tasks, penalty = reader.readline().strip().split()
            table_student.append([name, int(tasks), int(penalty)])

    quicksort(table_student)

    with open('output.txt', 'w') as writer:
        writer.write('\n'.join([name for name, _, _ in table_student]))


if __name__ == "__main__":
    main()
