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


def task_5():
    with open('input.txt', 'r') as reader:
        n = int(reader.readline())
        word, word_long = '', ''
        if n > 0:
            for c in reader.read():
                if c == ' ':
                    if len(word) > len(word_long):
                        word_long = word
                    word = ''
                    continue
                word += c
        with open('output.txt', 'w') as writer:
            writer.write(f'{word_long}\n{len(word_long)}')


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
        num_1 = reader.readline()
        num_2 = reader.readline()
        if len(num_2) > len(num_1):
            num_1, num_2 = num_2, num_1
        i = len(num_2) - 1
        answer = ''
        flag = False
        while i >= 0:
            if num_1[i] == num_2[i]:
                answer = '0' + answer
                if num_1[i] == '1':
                    flag = True
            
            i -= 1



def task_9():
    pass


def task_10():
    pass


def task_11():
    pass


def task_12():
    pass


time_start = time.time()
task_7()
time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')

