import time
import gc
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from shell_sort import shell_sort
from chart_maker import chart_maker
from read_file import read_words_from_file

bubble_sort_times = {}
selection_sort_times = {}
merge_sort_times = {}
shell_sort_times = {}
number_list = [
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    9000,
    10000,
]


def main():
    for number_of_words in number_list:
        words_list = read_words_from_file("pan-tadeusz.txt", number_of_words)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        bubble_sort(words_list)
        stop = time.process_time()
        sort_time = stop - start
        if gc_old:
            gc.enable()
        bubble_sort_times[number_of_words] = sort_time
    chart_maker(bubble_sort_times, "bubble_sort")
    print(bubble_sort_times)

    for number_of_words in number_list:
        words_list = read_words_from_file("pan-tadeusz.txt", number_of_words)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        selection_sort(words_list)
        stop = time.process_time()
        sort_time = stop - start
        if gc_old:
            gc.enable()
        selection_sort_times[number_of_words] = sort_time
    chart_maker(selection_sort_times, "selection_sort")
    print(selection_sort_times)

    for number_of_words in number_list:
        words_list = read_words_from_file("pan-tadeusz.txt", number_of_words)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        merge_sort(words_list)
        stop = time.process_time()
        sort_time = stop - start
        if gc_old:
            gc.enable()
        merge_sort_times[number_of_words] = sort_time
    chart_maker(merge_sort_times, "merge_sort")
    print(merge_sort_times)

    for number_of_words in number_list:
        words_list = read_words_from_file("pan-tadeusz.txt", number_of_words)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        shell_sort(words_list)
        stop = time.process_time()
        sort_time = stop - start
        if gc_old:
            gc.enable()
        shell_sort_times[number_of_words] = sort_time
    chart_maker(shell_sort_times, "shell_sort")
    print(shell_sort_times)


if __name__ == "__main__":
    main()
