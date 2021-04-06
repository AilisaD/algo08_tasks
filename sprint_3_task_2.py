key_dict = {2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'}


def main():
    with open("input.txt", "r") as reader:
        keys = list(map(int, reader.readline().rstrip().split()))
    with open("output.txt", "w") as writer:
        pass


if __name__ == "__main__":
    main()