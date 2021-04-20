def main():
    with open('input.txt', 'r') as fr:
        n = int(fr.readline())

        for i in range(n):
            line = fr.readline().rstrip().split()
    m = 92173
    with open('output.txt', 'w') as fw:
        fw.write('')


if __name__ == '__main__':
    main()
