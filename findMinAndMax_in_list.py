def findMinAndMax(L):
    if not L:
        return None, None
    else:
        min = max = L[0]
        for item in L[1:]:
            if item < min:
                min = item
            if item > max:
                max = item
        return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
