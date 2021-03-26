def main():
    with open("input.txt", "r") as reader:
        next(reader)
        m = int(reader.readline())
        matrix = ['']*m
        if m != 0:
            for line in reader.readlines():
                for i, c in enumerate(line.rstrip().split(" ")):
                    matrix[i] += f'{c} '
    with open("output.txt", "w") as writer:
        writer.write("\n".join(matrix))


if __name__ == "__main__":
    main()
