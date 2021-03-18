# 49319462
def main():
    counter_number = [0] * 9

    with open('input.txt', 'r') as reader:
        possible_num_click = int(reader.readline()) * 2

        for c in reader.read():
            if c.isdigit():
                counter_number[int(c) - 1] += 1

    result = str(sum([1 for count in counter_number if 0 < count <= possible_num_click]))
    with open('output.txt', 'w') as writer:
        writer.write(result)


main()
