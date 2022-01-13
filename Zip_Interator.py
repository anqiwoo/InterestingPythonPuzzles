names = ['Amy', 'Bob', 'Cindy']
ages = [11, 22, 33]
countries = ['Argentina', 'Brazil', 'China']

values = zip(countries, ages)  # zip() function returns an iterator
print(list(values)[0])

# If you iterate over the iterator once, it becomes empty.
names_dict = dict(zip(names, values))
# By converting it to a list in the first print() function, we've already emptied the iterator. Therefore, the resulting dictionary is empty.
print(len(names_dict))  # 0
