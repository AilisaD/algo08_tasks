def hash8(message):
    table_a = {
        'a': 2,
        'b': 3,
        'c': 5,
        'd': 7,
        'e': 11,
        'f': 13,
        'g': 17,
        'h': 19,
        'i': 23,
        'j': 29,
        'k': 31,
        'l': 37,
        'm': 41,
        'n': 43,
        'o': 47,
        'p': 53,
        'q': 59,
        'r': 61,
        's': 67,
        't': 71,
        'u': 73,
        'v': 79,
        'w': 83,
        'x': 89,
        'y': 97,
        'z': 101
    }
    h = 1
    for i in message:
        h *= table_a[i]
    return h


def main():
    hash8_list = []
    with open('input.txt', 'r') as fr:
        next(fr)
        for i, word in enumerate(fr.readline().rstrip().split()):
            hash8_list.append([i, hash8(word)])

    ans = []
    i_del = []
    i_ans = 0
    i = 0
    for h in hash8_list:
        if len(ans)+len(i_del) == len(hash8_list):
            break
        ans.append(f'{h[0]} ')
        for h2 in hash8_list[h[0]+1:]:
            if h[1] == h2[1]:
                ans[i_ans] += f'{h2[0]} '
                i_del.append(h2[0])
        i_ans += 1

    with open('output.txt', 'w') as fw:
        fw.write('\n'.join(ans))


if __name__ == '__main__':
    main()
