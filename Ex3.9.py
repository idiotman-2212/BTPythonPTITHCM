# EX 3.9 Write a function to cyclically rotate a given array clockwise by k.
# Write a function rotate(k, tmp_list) to cyclically rotate a given array clockwise by k.
# Test data 1
# Input:
#     1
#     1 3 2 5 7
# Output:
#     7 1 3 2 5
# Test data 2
# Input:
#     3
#     1 3 2 5 7
# Output:
#     2 5 7 1 3
k = int(input())
list1 = [int(x) for x in input().split(' ')]

def rotate(k, L):
    res = L[len(L) - k:]
    res.extend(L[:len(L) - k])
    return res

res = rotate(k, list1)
for i in range(len(res)):
    print(res[i], end= '')
    if i < len(res) - 1:
        print(' ', end= '')


