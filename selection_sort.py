def selection_sort(array):
    maks = array[0]
    for i in range(len(array)):
        for ii in range(len(array) - i):
            size = len(array) - i
            if array[ii] >= maks:
                maks = array[ii]
                maks_index = ii
        array[maks_index], array[size - 1] = array[size - 1], array[maks_index]
        maks = array[0]
