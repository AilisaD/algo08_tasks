def main():
    ans = 'YES'
    dict_char = {}
    with open('input.txt', 'r') as fr:
        string_1 = fr.readline().strip()
        string_2 = fr.readline().strip()
    for i, c1 in enumerate(string_1):
        c2 = string_2[i]
        if c1 not in dict_char:
            if c2 in dict_char.values():
                ans = 'NO'
                break
            dict_char[c1] = c2
        if dict_char[c1] != c2:
            ans = 'NO'
            break

    with open('output.txt', 'w') as fw:
        fw.write(ans)


if __name__ == '__main__':
    main()
