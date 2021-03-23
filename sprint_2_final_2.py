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
    return int(eval(f'{operand_1}{op}{operand_2}'))


if __name__ == '__main__':
    stack = Stack()
    symbol = ''
    with open('input.txt', 'r') as reader:
        byte = reader.read(1)
        while byte:
            if byte == ' ':
                if symbol.replace(' ', '') in '+*/-':
                    symbol = solve(stack, symbol)
                stack.push(symbol)
                symbol = ''
            symbol += byte
            byte = reader.read(1)
        symbol = symbol.replace('\n', '').replace(' ', '')
        if symbol.replace('\n', '') in '+*/-':
            stack.push(solve(stack, symbol))
        else:
            stack.push(symbol)

    with open('output.txt', 'w') as writer:
        writer.write(f'{stack.pop()}')
