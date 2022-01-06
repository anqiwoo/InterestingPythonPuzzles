import numpy as np

TOEFL_Score = np.array([100, 102, 99, 103, 106, 112, 118, 98])
name = np.array(['John', 'Bob', 'Alice', 'Adam',
                'Micky', 'Ricky', 'Vicky', 'Kate'])

top_3 = name[np.argsort(TOEFL_Score)][:-4:-1]
print(top_3[0])
print(top_3[1])
print(top_3[2])
