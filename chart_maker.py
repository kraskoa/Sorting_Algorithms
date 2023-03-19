from matplotlib import pyplot as plt


def chart_maker(sort_times, sorting_name):
    plt.plot(list(sort_times.keys()), list(sort_times.values()))
    plt.legend()
    plt.title(label=sorting_name)
    figure = plt.gcf()
    plt.show()
    sorting_name += ".png"
    figure.savefig(sorting_name, format="png")


def main():
    test_sort_times = {
        1: 1,
        2: 4,
        20: 400,
        50: 2500,
    }
    chart_maker(test_sort_times, "test_sort")


if __name__ == "__main__":
    main()
