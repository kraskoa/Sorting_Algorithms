def merge_sort(array):
    array2 = []
    begin = 0
    end = len(array) - 1
    mid = (begin + end) // 2
    if mid != begin:
        first_half = array[0:mid]
        second_half = array[mid + 1 : end - 1]
        merge_sort(first_half)
        merge_sort(second_half)

    first_begin = begin
    second_begin = mid + 1
    for i in range(begin, end):
        if (
            second_begin > end
            or first_begin <= mid
            and array[first_begin] < array[second_begin]
        ):
            array2.append(array[first_begin])
            first_begin += 1
        else:
            array2.append(array[second_begin])
            second_begin += 1
    return array2


def main():
    my_list = [23, 11, 2, 134, 8, 12]
    print(merge_sort(my_list))


if __name__ == "__main__":
    main()
