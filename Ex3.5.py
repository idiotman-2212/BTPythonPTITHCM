# EX 3.5 Write a program to sort a dictionary by value.
# Write a function that sorts a dictionary by value.
#
# Write a program to test your function.
#
# Test data:
#
# Input: {"a": 90, "b": 30, "c": 10, "d": 70}
#
# Output: {"c": 10, "b": 30, "d": 70, "a": 90}
words = input().strip('{}')

if len(words) > 0:
    words = words.split(', ')
    my_dict = {}
    for x in words:
        tmp = x.split(': ')
        my_dict[tmp[0]] = int(tmp[1])

    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    keys = list(my_dict)
    values = list(my_dict.values())

    print('{', end='')
    for i in range(len(keys)):
        print('{key}: {value}'.format(key=keys[i], value=values[i]), end='')
        if i < len(keys) - 1:
            print(', ', end='')
    print('}', end='')

else:
    print('{}', end='')
