key_dict = {'2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}


def gen_binary(n, i,  seq, answer):
    if len(n) == i:
        answer.append(seq)
    else:
        for c in key_dict[n[i]]:
            gen_binary(n, i+1, seq + c, answer)


def main():
    with open("../input.txt", "r") as reader:
        keys = reader.readline().rstrip()
    ans = []
    gen_binary(keys, 0, '', ans)
    with open("../output.txt", "w") as writer:
        writer.write(" ".join(ans))


if __name__ == "__main__":
    main()
