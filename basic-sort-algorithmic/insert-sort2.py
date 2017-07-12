#coding=utf-8
'''
插入排序算法2，对已排序列表从后向前遍历
'''
import random

def randomInt(length):
    arr = []
    while len(arr) < length:
        arr.append(random.randint(10, 99))
    return arr

length = 10
arr = randomInt(length)
print('before sort=', arr)

i=1
while i < length:
    j = i -1
    temp = arr[i]
    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = temp
    print('sort after cycle ', i, '=', arr)
    i = i + 1
print('final result=', arr)


    