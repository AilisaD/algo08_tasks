def reverse_numeric(num1, num2):
    return int(num1+num2) - int(num2+num1)


def cmp_to_key(mycmp):
    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def main():
    with open('../input.txt') as reader:
        next(reader)
        numbers = reader.readline().rstrip().split(' ')
    numbers = sorted(numbers,
                     key=cmp_to_key(reverse_numeric),
                     reverse=True)
    answer = ''.join(str(i) for i in numbers)
    count_zero = numbers.count('0')
    if count_zero == len(numbers):
        answer = '0'
    with open('../output.txt', 'w') as writer:
        writer.write(answer)


if __name__ == '__main__':
    main()
