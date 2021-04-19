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


def count_anagram2(hash8_list):
    tmp_ans = []
    hash8_list = sorted(hash8_list, key=lambda x: x[1])
    tmp_lst = [hash8_list[0]]
    for i, h in enumerate(hash8_list[1:]):
        if tmp_lst[len(tmp_lst)-1][1] != h[1] or i == len(hash8_list)-1:
            tmp_ans.append(tmp_lst)
            tmp_lst = [h]
            continue
        tmp_lst.append(h)
    tmp_ans.append(tmp_lst)
    tmp_ans = sorted(tmp_ans, key=lambda x: x[0][0])
    ans = ''
    for i in tmp_ans:
        for j in i:
            ans += f'{j[0]} '
        ans += '\n'
    return ans


def main():
    hash8_list = []
    with open('input.txt', 'r') as fr:
        next(fr)
        for i, word in enumerate(fr.readline().split()):
            hash8_list.append([i, hash8(word)])

    ans = count_anagram2(hash8_list)
    with open('output.txt', 'w') as fw:
        fw.write(ans)


if __name__ == '__main__':
    main()
