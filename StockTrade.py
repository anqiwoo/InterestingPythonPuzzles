import numpy as np

# simple regression model
w = np.array([0.7, 0.2, 0.1])

# Google stock prices (in US-$)
# [today, yesterday, 2 days ago]
x = np.array([1131, 1142, 1140])

y = np.dot(w, x)

# do we expect growing prices?
if y > x[0]:
    print('buy')
else:
    print('sell')
