
#coding=utf-8
'''
计数排序
'''
import random

#定义随机数生成函数
def randomInt(length):
    arr = []
    while len(arr) < length:
        arr.append(random.randint(0,9))
    return arr

#程序入口
length = 15
arr = randomInt(length)
print('before sort=', arr)

count = [0 for x in range(0, max(arr)+1)]
for item in arr:
    count[item] = count[item] + 1
print('count=', count)

index = 1
while index < len(count):
    count[index] = count[index] + count[index - 1]
    index = index + 1
print('count result=', count)

result = [0 for x in range(0, length)]
index = length - 1
while index >= 0:
    result[count[arr[index]]-1] = arr[index]
    count[arr[index]] = count[arr[index]] - 1
    index = index - 1
print('after sort=', result)