# 49779537

"""

"""
from math import floor


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size == 0:
            return 'error'
        return self.items.pop()

    @property
    def size(self):
        return len(self.items)


def solve(st, op):
    operand_2 = st.pop()
    operand_1 = st.pop()
    return floor(float(eval(f'{operand_1}{op}{operand_2}')))


if __name__ == '__main__':
    stack = Stack()
    operand = ''
    with open('input.txt', 'r') as reader:
        byte = reader.read(1)
        while byte:
            if byte == ' ':
                if operand.replace(' ', '') in '+*/-':
                    operand = solve(stack, operand)
                stack.push(operand)
                operand = ''
            operand += byte
            byte = reader.read(1)
        operand = operand.replace('\n', '').replace(' ', '')
        if operand.replace('\n', '') in '+*/-':
            stack.push(solve(stack, operand))
        else:
            stack.push(operand)

    with open('output.txt', 'w') as writer:
        writer.write(f'{stack.pop()}')
