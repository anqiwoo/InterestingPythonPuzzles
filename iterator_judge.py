from collections.abc import Iterator

g = (i for i in range(10))
l = list(g)

print(isinstance(g, Iterator))
print(isinstance(l, Iterator))
print(isinstance(iter(l), Iterator))
