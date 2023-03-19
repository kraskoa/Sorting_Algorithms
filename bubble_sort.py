def bubble_sort(lista):
    items_num = len(lista)
    while items_num > 0:
        for item in range(items_num - 1):
            if lista[item] > lista[item + 1]:
                lista[item], lista[item + 1] = lista[item + 1], lista[item]
        items_num -= 1
    return lista
