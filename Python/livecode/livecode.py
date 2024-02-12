# # Есть массив с числами 0, 1, 2,..., 9. где есть нули

# # Нам нужно найти нули и добавить их в конец


# Линейный подход
def masssiv(int_list):
    new_list = []
    counter = 0
    for i in int_list:
        if i == 0:
            counter += 1
        else:
            new_list.append(i)
    for i in range(counter):
        new_list.append(0)
    return new_list

print(*masssiv(int_list = [1,2,3,-1,0,4,5,0,0,6,1,2,3,4,5]))


import timeit
import numpy
def loop1() -> int:
        values = numpy.arange(1, 100_100_100_0)
        result = numpy.sum(values ** 2)
        return result
print(f"zxc1: {(timeit.timeit(loop1, number=1))}")
print(loop1())
import os
os.system("pause")

