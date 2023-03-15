def read_words_from_file(path, n):
    words_list = []
    final_list = []
    with open(path, "r") as file_handle:
        for line in file_handle:
            for word in line.split():
                words_list.append(word)
        for index in range(0, n):
            final_list.append(words_list[index])
        file_handle.close()
    return final_list
