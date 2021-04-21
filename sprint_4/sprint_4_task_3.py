def hash_substring(m, a, table, left, right):
    h = (table[right] - table[left - 1] * pow(a, right - left + 1, m)) % m
    return f'{h}\n'


def main():
    ans = ''

    with open('input.txt') as fr:
        a = int(fr.readline())
        m = int(fr.readline())
        table = [0]
        i = 0
        byte = fr.read(1)
        while byte != '\n':
            table.append((table[i] * a + ord(byte)) % m)
            i += 1
            byte = fr.read(1)

        n = int(fr.readline())
        for _ in range(n):
            l, r = fr.readline().split()
            ans += hash_substring(m, a, table, int(l), int(r))

    with open('output.txt', 'w') as fw:
        fw.write(ans)


if __name__ == '__main__':
    main()


