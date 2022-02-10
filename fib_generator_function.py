def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


g = fib_generator(10)
print(type(g))
for i in g:
    print(i)
