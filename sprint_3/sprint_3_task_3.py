def check_exists(t: str, sub: str, i, j, l_t, l_sub):
    while i < l_sub:
        i += 1
        f_break = False
        while j < l_t:
            j += 1
            if t[j] == sub[i]:
                f_break = True
                break
        if not f_break:
            return False
    return True


def main():
    with open("../input.txt", "r") as reader:
        s = reader.readline().rstrip()
        t = reader.readline().rstrip()

    with open("../output.txt", "w") as writer:
        writer.write(f'{check_exists(t, s, -1, -1, len(t)-1, len(s)-1)}')


if __name__ == "__main__":
    main()
