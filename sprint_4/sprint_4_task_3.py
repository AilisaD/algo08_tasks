def poly_hash_table(a, m, s):
    table = [[0, 1]]
    for i, c in enumerate(s):
        p = (table[i][1] * a) % m
        t = (table[i][0] * a + ord(c)) % m
        table.append([t, p])
    return table


def hash_substring(m, table, left, right):
    h = (table[right][0] - table[left - 1][0] * table[right-left + 1][1]) % m
    return f'{h}\n'


def main():
    with open('../input.txt') as fr, open('../output.txt', 'w') as fw:
        a = int(fr.readline())
        m = int(fr.readline())
        s = fr.readline().rstrip()

        table = poly_hash_table(a, m, s)
        del(s)
        n = int(fr.readline())

        for _ in range(n):
            l, r = fr.readline().split()
            fw.write(hash_substring(m, table, int(l), int(r)))


if __name__ == '__main__':
    # main()
    a = 1000
    m = 1000009
    q = 1
    for i in range(10000):
        print(q)
        q = (q * a) % m