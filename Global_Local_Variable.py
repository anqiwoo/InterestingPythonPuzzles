count = 0


def increment(n):
    count += n


try:
    increment(5 // 2 ** 2)
    print(count)
except Exception as e:
    print(e)  # local variable 'count' referenced before assignment
