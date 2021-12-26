import pandas as pd

xs = pd.Series([5, 1, 3, 2, 4, ])
print(xs, '\n')

xs.sort_values(inplace=True)
print(xs)

print(xs[0] == xs.iloc[0])  # Imagine the i in iloc is index.
print(xs[0] == xs.loc[0])  # Imagine the l in loc is label.
# If you omit the iloc or loc, you actually go with the loc method.
