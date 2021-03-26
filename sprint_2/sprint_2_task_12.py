def fib(n, k):
    fib_pre = 0
    f = 1
    for _ in range(1, n+1):
        fib_old = f
        f = (f + fib_pre) % k
        fib_pre = fib_old
    return f


def main():
    with open("../input.txt", "r") as reader, open("../output.txt", "w") as writer:
        nums = reader.read().split(' ')
        k = 10**int(nums[1])
        writer.write(str(fib(int(nums[0]), k)))


if __name__ == "__main__":
    main()
