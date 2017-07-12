
#coding=utf-8
'''
快速排序
'''
import random

def randomInt(length):
    arr = []
    while len(arr) < length:
        arr.append(random.randint(10, 99))
    return arr

def partition(arr, left, right):
    key = arr[left]
    start = left
    end = right
    
    while end > start:
        print('start=', start, 'end=', end)
        while start < end and key <= arr[end]:
            end = end - 1
        if arr[end] <= key:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp

        while start < end and key >= arr[start]:
            start = start + 1
        if arr[start] >= key:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
        
        print('after partition=', arr)

    if start > left:
        partition(arr, left, start-1)
    
    if end < right:
        partition(arr, end + 1, right)
    
length = 15
arr = randomInt(length)
print('before sort=', arr)

partition(arr, 0, len(arr) - 1)
print('final result=', arr)
