def numbers_in_lists(string):
    # YOUR CODE
    if string == '':
        return []
    else:
        big = int(string[0])
        output = [big]
        sublist = []
        for i in range(1, len(string)):
            current = int(string[i])
            if current <= big:
                sublist.append(current)
            else:
                if sublist:
                    output.append(sublist)
                    sublist = []
                output.append(current)
                big = current
        if sublist:
            output.append(sublist)
        return output


# testcases
string = '543987'
result = [5, [4, 3], 9, [8, 7]]
# print(repr(string), numbers_in_lists(string) == result)
# string = '987654321'
# result = [9, [8, 7, 6, 5, 4, 3, 2, 1]]
# print(repr(string), numbers_in_lists(string) == result)
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
# print(numbers_in_lists(string))

print(repr(string), numbers_in_lists(string) == result)
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(repr(string), numbers_in_lists(string) == result)
