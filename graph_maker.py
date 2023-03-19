from matplotlib import pyplot as plt


def graph_maker(sort_times, sorting_name):
    plt.plot(
        list(sort_times.keys()),
        list(sort_times.values()),
        label=sorting_name,
        markersize=3,
    )
    plt.legend()
    plt.title(label=sorting_name)
    figure = plt.gcf()
    plt.show()
    sorting_name += ".png"
    figure.savefig(sorting_name, format="png")


def combined_graph_maker(
    sort_1_times,
    sort_1_name,
    sort_2_times,
    sort_2_name,
    sort_3_times,
    sort_3_name,
    sort_4_times,
    sort_4_name,
):
    plt.plot(
        list(sort_1_times.keys()),
        list(sort_1_times.values()),
        label=sort_1_name,
        markersize=3,
    )
    plt.plot(
        list(sort_2_times.keys()),
        list(sort_2_times.values()),
        label=sort_2_name,
        markersize=3,
    )
    plt.plot(
        list(sort_3_times.keys()),
        list(sort_3_times.values()),
        label=sort_3_name,
        markersize=3,
    )
    plt.plot(
        list(sort_4_times.keys()),
        list(sort_4_times.values()),
        label=sort_4_name,
        markersize=3,
    )
    plt.legend()
    plt.title(label="All sorts")
    figure = plt.gcf()
    plt.show()
    figure.savefig("all_sorts.png", format="png")


def main():
    test_sort_times = {
        1: 1,
        2: 4,
        20: 400,
        50: 2500,
    }
    graph_maker(test_sort_times, "test_sort")


if __name__ == "__main__":
    main()
