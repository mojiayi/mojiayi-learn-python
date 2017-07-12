#coding=utf-8
'''
插入排序算法1，对已排序列表从前向后遍历
'''
import random

def randomInt(length):
    arr = []
    while len(arr) < length:
        arr.append(random.randint(10, 99))
    return arr
    
length = 10
arr = []
while len(arr) < length:
    arr.append(random.randint(10, 99))
print('before sort=', arr)

i=1
while i < length:
    j = 0
    while j < i:
        if arr[j] > arr[i]:
            temp = arr[i]
            k = i
            while k > j:
                arr[k] = arr[k-1]
                k = k-1
            arr[j] = temp
        j = j + 1
    print('sort after cycle ', i, '=', arr)
    i = i + 1
print('final result=', arr)