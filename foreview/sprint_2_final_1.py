# 49765449

"""
Я реализовала дек на циклическом массиве константной длины - по заданию надо выводить ошибку связанную с переполнением.
И не хотелось держать массив в 2n элементов.

Доказательство корректности.
Дек - двусторонняя очередь - извлекать элементы и добавлять их можно как спереди, так и в конец.
Хранятся индексы головы и хвоста дека, по которым можно провести все нужные операции извлечения и вставки за O(1).
Для проверки на переполнение запоминаем максимальный размер max_n и число заполненных элементов size. Сравнивая size с 0
или с max_n, можно понять пустой или переполненный дек и корректно обработать вставку/извлечение.

Временная сложность.
Все операции производятся за O(1), т.к. мы обращаемся по индексу при любом извлечении/вставке.

Пространственная сложность.
Т.к. мы храним все элементы в массиве размером n, то пространственная сложность будет O(n).
"""


class Deque:
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.items = [None]*n
        self.max_n = n

    def push_back(self, value):
        if self.size == self.max_n:
            return 'error'
        self.size += 1
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n

    def pop_back(self):
        if self.size == 0:
            return 'error'
        self.size -= 1
        self.tail = (self.tail - 1 + self.max_n) % self.max_n
        pop_elem, self.items[self.tail] = self.items[self.tail], None
        return pop_elem

    def push_front(self, value):
        if self.size == self.max_n:
            return 'error'
        self.size += 1
        self.head = (self.head - 1 + self.max_n) % self.max_n
        self.items[self.head] = value

    def pop_front(self):
        if self.size == 0:
            return 'error'
        self.size -= 1
        pop_elem, self.items[self.head] = self.items[self.head], None
        self.head = (self.head + 1) % self.max_n
        return pop_elem


if __name__ == '__main__':
    result = ''
    with open('../input.txt', 'r') as reader:
        next(reader)
        dec = Deque(int(reader.readline()))
        for line in reader:
            if 'push_front' in line:
                tmp = dec.push_front(int(line.split(' ')[1]))
                result += f'{tmp}\n' if tmp == 'error' else ''
            if 'push_back' in line:
                tmp = dec.push_back(int(line.split(' ')[1]))
                result += f'{tmp}\n' if tmp == 'error' else ''
            if 'pop_back' in line:
                result += f'{dec.pop_back()}\n'
            if 'pop_front' in line:
                result += f'{dec.pop_front()}\n'
    with open('../output.txt', 'w') as writer:
        writer.write(result)
