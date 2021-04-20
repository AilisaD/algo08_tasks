def create_dict_words(dict_words: dict, i: int, line: list):
    for word in line:
        if word not in dict_words:
            dict_words[word] = {}
        if i not in dict_words[word]:
            dict_words[word][i] = 0
        dict_words[word][i] += 1


def counting_relevance_in_file(count_word_in_file, list_inputs):
    for file in count_word_in_file:
        if file not in list_inputs:
            list_inputs[file] = 0
        list_inputs[file] += count_word_in_file[file]


def counting_relevance(count_words_inputs, line):
    list_inputs = {}
    for word in line:
        if word in count_words_inputs:
            counting_relevance_in_file(count_words_inputs[word], list_inputs)

    for k, _ in sorted(list_inputs.items(),
                       key=lambda item: item[1],
                       reverse=True)[:5]:
        yield f'{k}'


def main():
    count_words_inputs = {}
    list_requests = []

    with open('input.txt', 'r') as fr:
        n = int(fr.readline())

        for i in range(n):
            line = fr.readline().rstrip().split()
            create_dict_words(count_words_inputs, i+1, line)

        m = int(fr.readline())

        for i in range(m):
            list_requests.append(fr.readline().rstrip().split())

    ans = ''
    for request in list_requests:
        relevance = " ".join(counting_relevance(count_words_inputs, request))

        if len(relevance) != 0:
            ans += f'{relevance}\n'

    with open('output.txt', 'w') as fw:
        fw.write(ans)


if __name__ == '__main__':
    main()
