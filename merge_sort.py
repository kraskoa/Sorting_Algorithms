def merge_sort(array):
    if len(array) > 1:
        end = len(array)
        mid = end // 2
        first_half = array[:mid]
        second_half = array[mid:]
        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)
        j = k = 0
        for i in range(end):
            if j >= len(first_half) and k >= len(second_half):
                return array
            elif j >= len(first_half):
                array[i] = second_half[k]
                k += 1
            elif k >= len(second_half):
                array[i] = first_half[j]
                j += 1
            elif first_half[j] <= second_half[k]:
                array[i] = first_half[j]
                j += 1
            else:
                array[i] = second_half[k]
                k += 1
        return array
    else:
        return array
