# 49303069
def diff_before_i_zero(num_ref_house, diff_to_zero, i_zero):
    i = num_ref_house
    while i < i_zero:
        diff_to_zero[i] = str(i_zero - i)
        i += 1


def main():
    with open('../input.txt', 'r') as reader:
        len_street = int(reader.readline())
        street = reader.readline().split()

    diff_to_zero = ['0'] * len_street
    i_zero, pre_i_zero = None, None

    for i, num in enumerate(street):
        num_house = int(num)

        if i_zero is not None and num_house != 0:
            diff_to_zero[i] = str(i - i_zero)

        if num_house == 0:
            pre_i_zero = i_zero
            i_zero = i
            diff_to_zero[i_zero] = '0'

            if pre_i_zero is not None:
                diff_before_i_zero(
                    pre_i_zero + (i_zero - pre_i_zero) // 2 + 1,
                    diff_to_zero,
                    i_zero
                )

            if pre_i_zero is None and i != 0:
                diff_before_i_zero(0, diff_to_zero, i_zero)

    with open('../output.txt', 'w') as writer:
        writer.write(' '.join(diff_to_zero))


if __name__ == '__main__':
    main()
