import utility
import time


def task_1():
    with open('input.txt', 'r') as reader:
        len_street = int(reader.readline())
        street = reader.readline().split()
        diff_to_zero = [0]*len_street
        i = 0
        i_zero, pre_i_zero = None, None
        while i < len_street:
            street[i] = int(street[i])
            if street[i] == 0:
                pre_i_zero = i_zero
                i_zero = i
                diff_to_zero[i] = 0
                j = None
                if pre_i_zero is not None:
                    j = pre_i_zero + (i_zero - pre_i_zero) // 2 + 1
                if pre_i_zero is None and i != 0:
                    j = 0
                if j is not None:
                    while j < i_zero:
                        diff_to_zero[j] = i_zero - j
                        j += 1
                    j = None
            if i_zero is not None and street[i] != 0:
                diff_to_zero[i] = i - i_zero
            i += 1
        with open('output.txt', 'w') as writer:
            writer.write(f'{" ".join([str(i) for i in diff_to_zero])}')


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
task_2()
time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')