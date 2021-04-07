def main():
    with open('../input.txt') as reader:
        len_arr = int(reader.readline())
        str_arr = reader.readline()
        arr = [int(i) for i in str_arr.split()]
    f_sort = 0
    answer = ''
    for i in range(len_arr - 1):
        flag = 0
        for j in range(len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                f_sort = 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 0:
            continue
        answer += ' '.join([str(i) for i in arr]) + '\n'
    if f_sort == 0:
        answer = str_arr
    with open('../output.txt', 'w') as writer:
        writer.write(answer)


if __name__ == '__main__':
    main()
