def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)


def main():
    with open("input1.txt", "r") as reader, open("output1.txt", "w") as writer:
        writer.write(str(fib(int(reader.read()))))


if __name__ == "__main__":
    main()
