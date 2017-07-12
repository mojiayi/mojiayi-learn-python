import random
#定义随机数生成函数
def randomInt(length, startNumber, endNumber):
    arr = []
    while len(arr) < length:
        arr.append(random.randint(startNumber, endNumber))
    return arr