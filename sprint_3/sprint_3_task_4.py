def counting(child, cookies):
    counted_child = [0] * 1001
    counted_cookies = [0] * 1001
    len_ch = len(child)
    len_cook = len(cookies)
    len_max = len_ch if len_ch > len_cook else len_cook
    for i in range(len_max):
        if i < len_ch:
            counted_child[child[i]] += 1
        if i < len_cook:
            counted_cookies[cookies[i]] += 1
    count0 = count1 = 0
    for i in range(1001):
        for k in range(counted_child[i]):
            child[count0] = i
            count0 += 1

        for k in range(counted_cookies[i]):
            cookies[count1] = i
            count1 += 1
    return greedy(child, cookies)


def greedy(child, cookies):
    happy_children = 0
    i = 0
    for cook in cookies:
        if cook >= child[i]:
            happy_children += 1
            i += 1
        if i >= len(child):
            break
    return happy_children


def main():
    with open('../input.txt') as reader:
        next(reader)
        child = [int(c) for c in reader.readline().rstrip().split()]
        next(reader)
        cookies = [int(c) for c in reader.readline().rstrip().split()]

    ans = counting(child, cookies)
    with open('../output.txt', 'w') as writer:
        writer.write(f'{ans}')


if __name__ == '__main__':
    main()
