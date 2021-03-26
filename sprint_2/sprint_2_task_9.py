class MyQueueSized:
    def __init__(self, max_size):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.items = [None] * max_size
        self.max_n = max_size

    def push(self, value):
        if self.size == self.max_n:
            return "error"
        self.size += 1
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        pop_elem, self.items[self.head] = self.items[self.head], None
        self.head = (self.head + 1) % self.max_n
        return pop_elem

    def peek(self):
        if self.size == 0:
            return None
        return self.items[self.head]


def main():
    with open("input.txt", "r") as reader, open("output.txt", "w") as writer:
        next(reader)
        dec = MyQueueSized(int(reader.readline()))
        for line in reader:
            if "push" in line:
                tmp = dec.push(int(line.split(" ")[1]))
                if tmp == "error":
                    writer.write(f"{tmp}\n")
            if "peek" in line:
                writer.write(f"{dec.peek()}\n")
            if "pop" in line:
                writer.write(f"{dec.pop()}\n")
            if "size" in line:
                writer.write(f"{dec.size}\n")


if __name__ == "__main__":
    main()
