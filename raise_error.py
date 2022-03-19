'''
We can use raise error to catch exceptions and end the execution right away when catching an error.
'''


def take_an_integer(n):
    if not isinstance(n, int):
        raise ValueError('Invalid input! Please pass an integer.')
    # functionally same as:
    # assert isinstance(n, int), 'Invalid input! Please pass an integer.'
    print(n)


if __name__ == '__main__':
    take_an_integer('a')
    take_an_integer(1)
    print('End!')
