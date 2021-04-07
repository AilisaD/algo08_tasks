def find_day(arr, x, left, right, answer=None):
    if answer is None:
        answer = []
    if len(answer) == 2:
        return
    if right <= left:
        if len(answer) == 1:
            answer.append('-1')
        if len(answer) == 0:
            answer.append('-1 -1')
        return
    mid = (right + left) // 2
    if x <= arr[mid]:
        if (mid == 0 and arr[mid] == x) or arr[mid-1] < x:
            answer.append(f'{mid + 1}')
            find_day(arr, 2 * x, mid + 1, len(arr), answer)
        else:
            find_day(arr, x, left, mid, answer)
    else:
        find_day(arr, x, mid + 1, right, answer)
    return answer


def main():
    with open("input.txt", "r") as reader:
        next(reader)
        money_box = list(map(int, reader.readline().rstrip().split()))
        price = int(reader.readline())
    answer = find_day(money_box, price, 0, len(money_box))
    with open("output.txt", "w") as writer:
        writer.write(' '.join(answer))


if __name__ == "__main__":
    main()
