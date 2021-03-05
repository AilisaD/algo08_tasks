with open('input.txt', 'r') as reader:
    len_street = int(reader.readline())
    street = reader.readline().split()
    diff_to_zero = [0]*len(street)
    i = 0
    i_zero = None
    while i < len_street:
        street[i] = int(street[i])
        if street[i] == 0:
            i_zero = i
            diff_to_zero[i] = 0
        if i_zero and street[i]!:


        i += 1
