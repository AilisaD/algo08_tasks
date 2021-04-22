from operator import itemgetter


def create_dict_words(list_files: list):
    dict_words = {}
    for i, file in enumerate(list_files):
        for word in file:
            if word not in dict_words:
                dict_words[word] = {}

            if i + 1 not in dict_words[word]:
                dict_words[word][i + 1] = 0

            dict_words[word][i + 1] += 1

    return dict_words


def counting_relevance_in_file(count_word_in_file: dict, list_inputs: dict):
    for file in count_word_in_file:
        if file not in list_inputs:
            list_inputs[file] = 0

        list_inputs[file] += count_word_in_file[file]


def sorting(list_inputs: list):
    return " ".join((f'{x[0]}' for x in
                     sorted(
                         list_inputs,
                         key=itemgetter(1, 0)
                     )[:5]))


def counting_inputs_word(count_words_inputs, request):
    list_inputs = {}
    for word in request:
        if word in count_words_inputs:
            counting_relevance_in_file(count_words_inputs[word], list_inputs)
    return sorted(
        [[k, -v] for k, v in list_inputs.items()],
        key=itemgetter(1)
    )[:7]


def counting_relevance(count_words_inputs: dict, list_requests: list):
    list_requests = map(set, list_requests)
    relevance = []
    for request in list_requests:
        relevance.append(counting_inputs_word(count_words_inputs, request))
    return "\n".join(list(map(sorting, relevance)))


def main():
    list_requests = []
    list_files = []

    with open("input.txt", "r") as fr:
        n = int(fr.readline())
        for i in range(n):
            list_files.append(fr.readline().split())

        m = int(fr.readline())
        for i in range(m):
            list_requests.append(fr.readline().split())

    count_words_inputs = create_dict_words(list_files)
    ans = counting_relevance(count_words_inputs, list_requests)

    with open("output.txt", "w") as fw:
        fw.write(ans)


if __name__ == "__main__":
    main()
