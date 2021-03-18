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


def is_correct_bracket_seq():
    seq = Stack()



if __name__ == '__main__':
    pass