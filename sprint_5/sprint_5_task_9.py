def num_trees(n: int) -> int:
    num = 1

    for i in range((n*2 - (n*2-(n+1))) + 1, n*2 + 1):
        num *= i

    for i in range(1, n+1):
        num /= i

    return int(num)


if __name__ == '__main__':
    with open('../input.txt', 'r') as fr, open('../output.txt', 'w') as fw:
        fw.write(str(num_trees(int(fr.readline()))))
