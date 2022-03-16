'''
Create a Iterator Class Fib using __iter__ and __next__ methods.
'''


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # The instance itself is an iterator.

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:  # The termination condition of the iteration
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)
