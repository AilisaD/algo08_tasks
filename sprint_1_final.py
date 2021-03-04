with open('input.txt', 'r') as reader:
    len_street = reader.readline()
    street = [int(i) for i in reader.readline()]
    diff_to_zero = [0]*len(street)
    i = 0
    while i < len_street:
        if street[i] == 0:
            diff_to_zero[i] = 0

        i += 1
