def main():
    hobby_list = []
    with open('../input.txt', 'r') as fr:
        next(fr)
        for line in fr.readlines():
            if line in hobby_list:
                continue
            hobby_list.append(line)
    with open('../output.txt', 'w') as fw:
        fw.write(''.join(hobby_list))


if __name__ == '__main__':
    main()
