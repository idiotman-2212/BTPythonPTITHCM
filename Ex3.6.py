# EX 3.6 Write a function to generate all sublists of a given list.
# Write a Python program to generate all sublists of a given list.
#
# Test data 1
#
# Input:
#
#     [1, 4, 6]
#
# Output:
#
#     [1], [4], [6], [1, 4], [1, 6], [4, 6], [1, 4, 6]
#
L = [int(x) for x in input().lstrip('[').rstrip(']').split(', ')]

n = len(L)
length = 2 ** len(L)

D = {}
for i in range(1, n + 1):
    D[i] = []

exist = {}
for i in range(1, length):
    str_bin = str(bin(i))[2:]
    str_bin = str_bin[::-1]
    t_res = []
    for j in range(len(str_bin)):
        if str_bin[j] == '1':
            t_res.append(L[j])
    my_tuple = tuple(t_res)
    if exist.get(my_tuple) == None:
        D[len(t_res)].append(t_res)
        exist[my_tuple] = 1

for i in range(1, n + 1):
    for j in range(len(D[i])):
        print(D[i][j], end= '')
        if j < len(D[i]) - 1:
            print(', ', end= '')
    if i < n:
        print(', ', end= '')

