def task_1():
    with open('input.txt', 'r') as reader:
        a, x, b, c = map(int, reader.readline().split())
        with open('output.txt', 'w') as writer:
            writer.write(f'{a*x*x+b*x+c}')


def task_2():
    with open('input.txt', 'r') as reader:
        a, x, b, c = map(int, reader.readline().split())
        with open('output.txt', 'w') as writer:
            writer.write(f'{a*x*x+b*x+c}')


task_1()
