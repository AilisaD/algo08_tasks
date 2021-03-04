import random
import string


def create_file_for_task_3():
    with open('input1.txt', 'w') as w:
        n, m = 1000, 1000
        w.write(f'{n}\n')
        w.write(f'{m}\n')
        for i in range(n):
            a = ' '.join([str(random.randint(-1000, 1000)) for _ in range(m)])
            w.write(f'{a}\n')
        w.write(f'{30}\n')
        w.write(f'{0}\n')


def create_file_for_task_4():
    with open('input1.txt', 'w') as w:
        n = 100000
        w.write(f'{n}\n')
        a = ' '.join([str(random.randint(-273, 273)) for _ in range(n)])
        w.write(f'{a}\n')


def create_file_for_task_4():
    with open('input1.txt', 'w') as w:
        n = 100000
        w.write(f'{n}\n')
        a = ' '.join([str(random.randint(-273, 273)) for _ in range(n)])
        w.write(f'{a}\n')


def create_file_for_task_5():
    with open('input1.txt', 'w') as w:
        n = 100000
        w.write(f'{n}\n')
        a = ''.join([random.choice(string.ascii_lowercase+' ') for _ in range(n)])
        w.write(a)
