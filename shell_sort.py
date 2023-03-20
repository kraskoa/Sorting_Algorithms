def shell_sort(lista):
    items_num = len(lista)
    interval = items_num // 2
    while interval > 0:
        for i in range(interval, items_num):
            temp = lista[i]
            j = i
            while j >= interval and lista[j - interval] > temp:
                lista[j] = lista[j - interval]
                j -= interval
            lista[j] = temp
        interval //= 2
    return lista
