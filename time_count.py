# Nie zrobie z tego funkcji bo trzeba by bylo przekazywac funkcje sortujace jako argument
# Zapisze tu algorytm dzialania liczenia czasu i  wylaczania garbage collectora, bedzie go
# mozna pozniej wkleic do maina i usunac plik z repo
import time
import gc

gc_old = gc.isenabled()
gc.disable()
start = time.process_time()
# Tutaj trzeba bedzie wrzucic wywolanie funkcji sortujacych dla odpowiednich list
# np. bubble_sort(read_words_from_file("pan-tadeusz.txt", 10000)) (sprawdzałem i działa XD)
stop = time.process_time()
sort_time = stop - start
if gc_old:
    gc.enable()
# Pozniej w main dodajemy do slownika na zasadzie:
# bubble_sort_times[10000] = sort_time
