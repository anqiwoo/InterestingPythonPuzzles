from tabnanny import check


def check_sudoku(sl):
    for i, row in enumerate(sl):
        for j, column in enumerate(row):
            pre_rows = [sl[num][j] for num in range(i)]
            pre_cols = [sl[i][num] for num in range(j)]
            if column not in range(1, 10):
                return False
            if column in pre_cols:
                return False
            if column in pre_rows:
                return False
    return True


test = [[1, 2, 3, 4, 5],
        [2, 3, 1, 5, 6],
        [4, 5, 2, 1, 3],
        [3, 4, 5, 2, 1],
        [5, 6, 4, 3, 2]]

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]
print(check_sudoku(test))
print(check_sudoku(correct))
print(check_sudoku(incorrect))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))
