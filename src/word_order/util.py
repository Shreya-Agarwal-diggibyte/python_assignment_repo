def count_words(words):
    words_list = []
    counts_list = []

    for word in words:
        found = False
        for i in range(len(words_list)):
            if words_list[i] == word:
                counts_list[i] += 1
                found = True
                break

        if not found:
            words_list.append(word)
            counts_list.append(1)

    return words_list, counts_list
