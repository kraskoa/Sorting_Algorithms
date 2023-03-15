def merge_sort(array):
    array2 = []
    begin = 0
    end = len(array)
    mid = (begin + end) // 2
    if mid != begin:
        first_half = array[0:mid]
        second_half = array[mid:end]
        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)
    if len(array) > 1:
        for i in range(end):
            if len(first_half) == 0 and len(second_half) == 0:
                return array2
            elif len(first_half) == 0:
                array2.append(second_half[0])
                second_half.pop(0)
            elif len(second_half) == 0:
                array2.append(first_half[0])
                first_half.pop
            elif first_half[0] <= second_half[0]:
                array2.append(first_half[0])
                first_half.pop(0)
            else:
                array2.append(second_half[0])
                second_half.pop(0)
        return array2
    else:
        return array


def main():
    my_list = [23, 11, 2, 134, 8, 12]
    print(merge_sort(my_list))


if __name__ == "__main__":
    main()
