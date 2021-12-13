def matrixFind(matrix, value):
    '''In summary, the idea of this great algorithm from Keith Schwartz [1] reduces one row or one column in each iteration. The runtime is only O(2n) instead of O(n^2) for a squared matrix with n rows and columns.
    '''
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    if n == 0:
        return False
    i = 0
    j = n - 1
    while i < m and j >= 0:
        if matrix[i][j] < value:
            i += 1
        elif matrix[i][j] == value:
            return True
        else:
            j -= 1
    return False


M = [[i, i+1, i+2, i+3] for i in range(4)]
print(matrixFind(M, 4))
