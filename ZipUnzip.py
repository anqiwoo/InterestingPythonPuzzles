lst = ['Alice', 'Bob', 'Frank']
salaries = [9999, 8888, 7777]
check_salaries = [1, 1, 0]

# Zip
zipped = list(zip(lst, salaries, check_salaries))
print(zipped)

# Unzip
un_zipped = list(zip(*zipped))
print(un_zipped)
