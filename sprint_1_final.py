import utility
import time


def task_1():
    # разбить на функции
    with open('input.txt', 'r') as reader:
        len_street = int(reader.readline())
        street = reader.readline().split()  # пойти по байтам
    diff_to_zero = [0]*len_street
    i_zero, pre_i_zero = None, None
    for elem in enumerate(street):
        if elem[1] == '0':
            pre_i_zero = i_zero
            i_zero = elem[0]
            diff_to_zero[i_zero] = 0
            j = None
            if pre_i_zero is not None:
                j = pre_i_zero + (i_zero - pre_i_zero) // 2 + 1
            if pre_i_zero is None and elem[0] != 0:
                j = 0
            if j is not None:
                while j < i_zero:
                    diff_to_zero[j] = i_zero - j
                    j += 1
        if i_zero is not None and elem[1] != 0:
            diff_to_zero[elem[0]] = elem[0] - i_zero
    with open('output.txt', 'w') as writer:
        writer.write(" ".join([str(i) for i in diff_to_zero]))


def task_2():
    with open('input.txt', 'r') as reader:
        possible_num = int(reader.readline())*2
        table = [0]*9
        for c in reader.read():
            if c.isdigit():
                table[int(c)-1] += 1
        a = sum([1 for i in table if 0 < i <= possible_num])
    with open('output.txt', 'w') as writer:
        writer.write(f'{a}')


time_start = time.time()
task_1()
time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')
