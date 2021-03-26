class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.items = None
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, value):
        prev_elem = self.tail
        self.tail = Node(value)
        if self.size == 0:
            self.head = self.tail
        else:
            prev_elem.next = self.tail
        self.size += 1

    def get(self):
        if self.size == 0:
            return 'error'
        pop_elem = self.head
        self.head = self.head.next
        self.size -= 1
        return pop_elem.value

    def print(self):
        while self.items:
            print(self.items.value, end=" -> ")
            self.items = self.items.next
        print("None")


def main():
    with open("../input.txt", "r") as reader, open("../output.txt", "w") as writer:
        next(reader)
        dec = Queue()
        for line in reader:
            if "put" in line:
                dec.put(int(line.split(" ")[1]))
            if "get" in line:
                writer.write(f"{dec.get()}\n")
            if "size" in line:
                writer.write(f"{dec.size}\n")


if __name__ == "__main__":
    main()

