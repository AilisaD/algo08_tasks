def poly_hash(a, m, s):
    if len(s) > 0:
        p_hash = ord(s[0])
        for c in s[1:]:
            p_hash = (p_hash * a + ord(c)) % m
        return p_hash % m
    return 0


def main():
    with open("../input.txt", "r") as reader:
        a = int(reader.readline())
        m = int(reader.readline())
        s = reader.readline().rstrip()
    ans = poly_hash(a, m, s)
    with open('../output.txt', "w") as writer:
        writer.write(f'{ans}')


if __name__ == '__main__':
    main()
