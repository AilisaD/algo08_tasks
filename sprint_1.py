import time
import utility


def task_1():
    with open('input.txt', 'r') as reader:
        a, x, b, c = map(int, reader.readline().split())
        with open('output.txt', 'w') as writer:
            writer.write(f'{a * x * x + b * x + c}')


def task_2():
    with open('input.txt', 'r') as reader:
        a, b, c = map(int, reader.readline().split())
        out_string = 'FAIL'
        if a & 1 == b & 1 == c & 1:
            out_string = 'WIN'
        with open('output.txt', 'w') as writer:
            writer.write(out_string)


def task_3():
    with open('input.txt', 'r') as reader:
        n = int(reader.readline())
        m = int(reader.readline())
        i = 0
        mas = []
        while i < n:
            mas.append([int(x) for x in reader.readline().split()])
            i += 1
        x = int(reader.readline())
        y = int(reader.readline())
        res = []
        if x > 0:
            res.append(mas[x-1][y])
        if x < n-1:
            res.append(mas[x+1][y])
        if y > 0:
            res.append(mas[x][y-1])
        if y < m-1:
            res.append(mas[x][y+1])
        res.sort()
        with open('output.txt', 'w') as writer:
            writer.write(f'{" ".join([str(i) for i in res])}')


def task_4():
    with open('input.txt', 'r') as reader:
        n = int(reader.readline())
        count = 0
        if n != 1:
            i = 0
            mas = [int(j) for j in reader.readline().split(' ')]
            while i < n:
                if i == 0 and mas[i] > mas[i+1]:
                    count += 1
                if 0 < i < n-1 and mas[i - 1] < mas[i] > mas[i + 1]:
                    count += 1
                if i == n-1 and mas[i] > mas[i-1]:
                    count += 1
                i += 1
        if n == 1:
            count = 1
        with open('output.txt', 'w') as writer:
            writer.write(f'{count}')


def choose_long(word1, word2):
    return word1 if len(word1) > len(word2) else word2


def task_5():
    with open('input.txt', 'r') as reader:
        len_string = reader.readline()
        word, word_long = '', ''
        for c in reader.read():
            if c == ' ':
                word_long = choose_long(word, word_long)
                word = ''
                continue
            word += c
    word_long = choose_long(word, word_long)
    answer = f'{word_long}\n{len(word_long)}'
    if len(word_long) < 1:
        answer = '0'
    with open('output.txt', 'w') as writer:
        writer.write(answer)


def task_6():
    with open('input.txt', 'r') as reader:
        string = ''
        for c in reader.read().lower():
            if c.isalpha() or c.isdigit():
                string += c
        i = 0
        flag = True
        while i < len(string)/2:
            if string[i] != string[len(string) - i-1]:
                flag = False
            i += 1
        with open('output.txt', 'w') as writer:
            writer.write(f'{flag}')


def task_7():
    with open('input.txt', 'r') as reader:
        answer = ''
        dec_num = int(reader.read())
        print(bin(dec_num))
        while dec_num >= 1:
            answer = str(dec_num % 2) + answer
            dec_num //= 2
        with open('output.txt', 'w') as writer:
            writer.write(answer)


def task_8():
    with open('input.txt', 'r') as reader:
        num_1 = reader.readline().rstrip()
        num_2 = reader.readline().rstrip()
    if len(num_2) != len(num_1):
        if len(num_2) > len(num_1):
            num_1, num_2 = num_2, num_1
        num_2 = '0'*(len(num_1)-len(num_2)) + num_2
    answer = ''
    flag = False
    for n1, n2 in zip(num_1[::-1], num_2[::-1]):
        if n1 == n2:
            if flag:
                answer = '1' + answer
            else:
                answer = '0' + answer
            flag = False
            if n1 == '1':
                flag = True
        else:
            if flag:
                answer = '0' + answer
                flag = True
            else:
                answer = '1' + answer
                flag = False
    if flag:
        answer = '1' + answer
    with open('output.txt', 'w') as writer:
        writer.write(answer)


def task_9():
    with open('input.txt', 'r') as reader:
        num = int(reader.read())
    while num % 1 == 0:
        num = num/4
    answer = 'False'
    if num == 0.25:
        answer = 'True'
    with open('output.txt', 'w') as writer:
        writer.write(answer)


def factorize(x):
    for i in range(2, int(x ** 0.5)+1):
        while x % i == 0:
            x /= i
            yield f'{i}'

    if x != 1:
        yield f'{int(x)}'


def task_10():
    with open('input.txt', 'r') as reader:
        num = int(reader.read())
    with open('output.txt', 'w') as writer:
        writer.write(' '.join(factorize(num)))


def task_11():
    with open('input.txt', 'r') as reader:
        length_num_1 = int(reader.readline())
        num_1 = int(reader.readline().replace(' ', ''))
        num_2 = int(reader.readline())
    with open('output.txt', 'w') as writer:
        writer.write(' '.join(str(num_1 + num_2)))


def task_12():
    with open('input.txt', 'r') as reader:
        string_1 = ' '.join(reader.readline()).split()
        string_2 = ' '.join(reader.readline()).split()
    string_1.sort()
    string_2.sort()
    answer = ''

    for i, c in enumerate(string_2):
        answer = c
        if c != string_1[i]:
            break
        if i + 1 == len(string_1):
            answer = string_2[i+1]
            break
    with open('output.txt', 'w') as writer:
        writer.write(answer)


time_start = time.time()
task_12()
time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')

