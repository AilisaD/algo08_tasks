def solution(s: str):
    max_len = 0
    i = 0
    first = 0
    while i < len(s):
        if s[i] in s[first:i]:
            if len(s[first:i]) > max_len:
                max_len = len(s[first:i])
            pre_first = first
            first = s[first:i].index(s[i]) + 1 + pre_first

        i += 1
    if len(s[first:i]) > max_len:
        max_len = len(s[first:i])

    return max_len


def main():
    with open('../input.txt', 'r') as fr:
        s = fr.readline().rstrip()
    ans = solution(s)

    with open('../output.txt', 'w') as fw:
        fw.write(str(ans))


if __name__ == '__main__':
    main()
