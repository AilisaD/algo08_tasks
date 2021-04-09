def solve(arr):
    i = len(arr) - 1

    while i > 0:
        if arr[i][1] >= arr[i-1][0]:
            if arr[i][1] < arr[i-1][1]:
                arr[i][1] = arr[i-1][1]
            arr.pop(i - 1)

        i -= 1
    return arr[::-1]


def main():
    flower_beds = []
    with open("../input.txt", "r") as reader:
        next(reader)
        for line in reader.readlines():
            l, r = line.rstrip().split()
            flower_beds.append([int(l), int(r)])
    ans = solve(sorted(flower_beds, reverse=True))
    with open("../output.txt", "w") as writer:
        writer.write('\n'.join((f'{i[0]} {i[1]}' for i in ans)))


if __name__ == "__main__":
    main()
