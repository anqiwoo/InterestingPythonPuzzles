expression = 1 < 2

assert expression
# equals
if not expression:
    raise AssertionError()

expression = 1 > 2
assert expression, 'Something went wrong!'
# equals
if not expression:
    raise AssertionError('Something went wrong!')
