def solution(s1, s2):
    first = 0
    max_slice = 0
    i = 0
    while i < len(s1):
        if ' '.join(s1[first:i+1]) not in ' '.join(s2):
            if len(s1[first:i+1]) > max_slice:
                max_slice = len(s1[first:i])
            first += 1
        i += 1
    if len(s1[first:i + 1]) > max_slice:
        max_slice = len(s1[first:i])
    return str(max_slice)


def main():
    with open('input.txt', 'r') as fr:
        next(fr)
        s1 = fr.readline().rstrip().split()

        next(fr)
        s2 = fr.readline().rstrip().split()

    ans = solution(s1, s2)

    with open('output.txt', 'w') as fw:
        fw.write(ans)


if __name__ == '__main__':
    main()
