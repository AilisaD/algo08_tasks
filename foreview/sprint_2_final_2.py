# 49802622

"""
-- ПРИНЦИП РАБОТЫ --
Я решила задачу на основе стека (используется deque из библиотеки collections),
т.к. он лучше всего подходит для решения выражений в польской нотации -
необходимо иметь доступ только к вершине списка.

По алгоритму: при встрече знака какой-либо операции произвести ее вычисление
с двумя предыдущими операндами.
Т.е. 3 2 + -> операция + над операндами 3 и 2 -> 5.
Результат так же надо хранить для возможных дальнейших операций.

Идем по строке и записываем каждое число в стек. Если встречается операция,
то извлекаем 2 числа из вершины стека (они и являются последними операндами,
брать числа необходимо в порядке их занесения,
поэтому сначала извлекается второй операнд, а затем первый).
Записываем результат вычислений в стек.
Результат по заданию необходимо округлять вниз,
для этого вызвалась функйия floor из библиотеки math.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
При использовании стека, сколько бы ни было операций,
ответ - результат последней операции - на вершине стека.

7 2 + 10 -
[в обычной записи: (7+2)-10 = 9-10 = -1]

Заполняем стек 7 2
Выполняется + над 7 и 2 -> 9 -> заносим в стек
Заносим в стек 10
Выполняется операция - над 9 и 10 -> -1 -> заносим в стек
Вывод результата -> -1

Если же в конце подается не операция, а число,
то ответом будет являться оно, что так же корректно сработает, т.к.
на вершине стека будет находиться уже оно.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление элементов в стек занимает O(1). Извлечение так же за O(1).
Поэтому временная сложность алгоритма зависит только от длины строки,
поданной на вход - O(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В стеке бедет храниться столько элементов, сколько чисел будет в строке.
Т.е. пространственная сложность - O(n).
"""
from math import floor
from collections import deque


OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
}


def solve(st, op):
    operand_2 = st.pop()
    operand_1 = st.pop()
    return floor(OPERATIONS[op](operand_1, operand_2))


def main():
    stack = deque()
    operand = ""

    with open("input.txt", "r") as reader:
        byte = reader.read(1)

        while byte:
            if byte == " ":
                operand = operand.lstrip()
                if operand in "+*/-":
                    operand = solve(stack, operand)
                stack.append(int(operand))
                operand = ""

            operand += byte
            byte = reader.read(1)

        operand = operand.strip()

        if operand in "+*/-":
            stack.append(solve(stack, operand))
        else:
            stack.append(operand)

    with open("output.txt", "w") as writer:
        writer.write(f"{stack.pop()}")


if __name__ == "__main__":
    main()
