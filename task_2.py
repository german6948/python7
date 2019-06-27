from random import random
N = 6
array = [0]*N
even = []
for i in range(N):
    array[i] = int(random() * 6) + 10
    if array[i] % 2 == 0:
        even.append(i)
print(array)
print('Индексы четных элементов: ', even)
