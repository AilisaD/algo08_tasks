# 49275913
with open('input.txt', 'r') as reader:
    possible_num = int(reader.readline())*2
    table = [0]*9
    for c in reader.read():
        if c.isdigit():
            table[int(c)-1] += 1
    a = sum([1 for i in table if 0 < i <= possible_num])
    with open('output.txt', 'w') as writer:
        writer.write(f'{a}')
