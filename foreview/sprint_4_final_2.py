# 50908239

"""
-- ПРИНЦИП РАБОТЫ --
Для реализация хеш-таблицы создан класс HashTable.
Размерность таблицы равна простому числу m = 50329.
Сама таблица представляет собой список длины m, элементами которого
являются кортежи из двух списков.
    [
        ([], [],),
        ([], [],),
        ...
    ]

В одном списке хранятся ключи, в другом - значения.
([key_0, key_1, ...], [value_0, value_1, ...])
Эти два списка нужны для решения коллизий методом цепочек.

-- ДОКАЗАТЕЛЬСВО КОРРЕКТНОСТИ --
В начале каждой операции получаем значение хеш-функции по модулю m.
Далее проверяем есть значение переданного ключа в списке ключей
в элементе по расчитанному индексу.

Если есть, то находим индекс элемента в списке ключей.
Этот же индекс будет у элемента с нужным нам значением в списке значений.
Для операции put обновляем значение в списке значений.
Для операции get возвращаем значение из списка.
Для операции delete удаляем по индексу элементы из обоих списков
и возвращаем удаленное значение.

Если переданного ключа нет в списке ключей, то:
для операции put добавляем в конец обоих списков ключ и значение;
для операций get и delete возвращаем None.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В лучшем случае, операции будут выполнятся за O(1).
put - если нет ключа в списке,
      если есть такой ключ существует и он находится в первом элементе, то
      операция append или set равна O(1).
get и delete - ключ находится по индексу 0, операции выполнятся за O(1).

В худшем случае все операции будут выполняться за O(n), где n - это длина
списков ключей и значений.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В памяти всегда будет храниться массив на m элементов - O(m).
При коллизиях будет добавляться размер списков, т.е. O(k),
где k - число коллизий.
В итоге, пространственная сложность - O(m+k).
"""


class HashTable:
    m = 50329

    def __init__(self):
        self.table = [([], []) for _ in range(self.m)]

    def put(self, key, value):
        idx = hash(key - 1) % self.m

        if key in self.table[idx][0]:
            idx_key = self.table[idx][0].index(key)
            self.table[idx][1][idx_key] = value
            return

        self.table[idx][0].append(key)
        self.table[idx][1].append(value)

    def get(self, key):
        idx = hash(key-1) % self.m

        if key in self.table[idx][0]:
            idx_key = self.table[idx][0].index(key)
            return self.table[idx][1][idx_key]

        return None

    def delete(self, key):
        idx = hash(key-1) % self.m

        if key in self.table[idx][0]:
            idx_key = self.table[idx][0].index(key)
            val = self.table[idx][1][idx_key]

            self.table[idx][0].pop(idx_key)
            self.table[idx][1].pop(idx_key)

            return val

        return None


def main():
    table = HashTable()
    ans = ''
    with open('input.txt', 'r') as fr:
        n = int(fr.readline())

        for i in range(n):
            line = fr.readline().rstrip().split()

            if line[0] == 'get':
                ans += f'{table.get(int(line[1]))}\n'

            if line[0] == 'put':
                table.put(int(line[1]), int(line[2]))

            if line[0] == 'delete':
                ans += f'{table.delete(int(line[1]))}\n'

    with open('output.txt', 'w') as fw:
        fw.write(ans)


if __name__ == '__main__':
    main()
