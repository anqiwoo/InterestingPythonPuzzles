def bubblesort(lst):
    for passes_left in range(len(lst)-1, 0, -1):
        for index in range(passes_left):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]


l = [27, 0, 85, 23, 100]
print(f'\nUnsorted list:{l}\n')
bubblesort(l)
print(f'Sorted list: {l}')
