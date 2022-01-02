def Hanoi(n, A, B, C):
    if n == 1:
        print(A, '->', C)
        return 1
    else:
        t1 = Hanoi(n-1, A, C, B)
        print(A, '->', C)
        t2 = Hanoi(n-1, B, A, C)
        return t1 + 1 + t2


n = 3
A = 'A'
B = 'B'
C = 'C'
print(f'The No. of Movement：{Hanoi(n, A, B, C)}')
