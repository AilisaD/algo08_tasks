import utility
import time


def diff_before_i_zero(i, diff_to_zero, i_zero):
    while i < i_zero:
        diff_to_zero[i] = str(i_zero - i)
        i += 1


def task_1():
    with open('input.txt', 'r') as reader:
        len_street = int(reader.readline())
        diff_to_zero = ['0'] * len_street
        i_zero, pre_i_zero = None, None
        num_house = ''
        i = 0
        for c in reader.read():
            num_house += c
            if c == ' ' or i + 1 == len_street:
                num = int(num_house)
                num_house = ''
                if num == 0:
                    pre_i_zero = i_zero
                    i_zero = i
                    diff_to_zero[i_zero] = str(0)
                    if i != 0 and pre_i_zero is None:
                        diff_before_i_zero(0, diff_to_zero, i_zero)
                    if pre_i_zero is not None:
                        diff_before_i_zero(
                            pre_i_zero + (i_zero - pre_i_zero) // 2 + 1,
                            diff_to_zero,
                            i_zero
                        )
                if num != 0 and i_zero is not None:
                    diff_to_zero[i] = str(i - i_zero)
                i += 1
    with open('output.txt', 'w') as writer:
        writer.write(' '.join(diff_to_zero))


def task_2():
    table = [0] * 9
    with open('input.txt', 'r') as reader:
        possible_num = int(reader.readline())*2
        for c in reader.read():
            if c.isdigit():
                table[int(c)-1] += 1
    a = str(sum([1 for i in table if 0 < i <= possible_num]))
    with open('output.txt', 'w') as writer:
        writer.write(a)


time_start = time.time()
task_1()
time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')
