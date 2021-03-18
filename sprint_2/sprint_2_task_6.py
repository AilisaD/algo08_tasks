class StackMax:
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

    def get_max(self):
        if self.size == 0:
            return None
        max_item = self.items[0]
        for item in self.items:
            if item > max_item:
                max_item = item
        return max_item


def main():
    stack = StackMax()
    result = ''
    with open('input.txt', 'r') as reader:
        line = reader.readline()
        for line in reader:
            if 'get' in line:
                result += f'{stack.get_max()}\n'
            if 'push' in line:
                stack.push(int(line.split(' ')[1]))
            if 'pop' in line:
                tmp = stack.pop()
                result += tmp+'\n' if tmp == 'error' else ''
    with open('output.txt', 'w') as writer:
        writer.write(result)


main()
