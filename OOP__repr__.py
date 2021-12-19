class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __repr__(self):
        return 'Tall ' * (self.height > 165) + self.name


# Instantiate
J = Person('Jack', 170)
M = Person('Mary', 160)
print(J, M)
print([J, M])

print('\n')

# Just String
J = 'Tall Jack'
M = 'Mary'
print(J, M)
print([J, M])  # Notice the difference between the outputs
