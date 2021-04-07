answer = ''


def gen_bracket_sequence(n, s='', left=0, right=0):
    if left == n and right == n:
        global answer
        answer += s + '\n'
    else:
        if left < n:
            gen_bracket_sequence(n, s + '(', left+1, right)
        if right < left:
            gen_bracket_sequence(n, s + ')', left, right+1)


if __name__ == '__main__':
    with open('../input.txt') as reader:
        num = int(reader.readline())
    gen_bracket_sequence(num)
    with open('../output.txt', "w") as writer:
        writer.write(answer)
