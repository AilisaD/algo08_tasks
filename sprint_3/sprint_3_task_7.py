def counting_sort(arr):
    counted = [0] * 3
    for color in arr:
        counted[int(color)] += 1

    count = 0
    for i in range(3):
        for k in range(counted[i]):
            arr[count] = f'{i}'
            count += 1
    return arr


def main():
    with open('../input.txt') as reader:
        next(reader)
        g = reader.readline().rstrip().split()

    with open('../output.txt', 'w') as writer:
        writer.write(' '.join(counting_sort(g)))


if __name__ == '__main__':
    main()
