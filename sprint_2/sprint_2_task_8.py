from collections import deque

BOUND = {'}': '{', ')': '(', ']': '['}


def is_correct_bracket_seq(seq):
    stack = deque()
    if len(seq) % 2 != 0:
        return False
    for c in seq:
        if c in '{[(':
            stack.append(c)
        if c in '}])':
            if len(stack) == 0:
                return False
            if stack.pop() != BOUND[c]:
                return False
    return True


if __name__ == '__main__':
    with open("input.txt") as reader:
        seq_bound = reader.readline().rstrip()
    with open("output.txt", "w") as writer:
        writer.write(str(is_correct_bracket_seq(seq_bound)))
