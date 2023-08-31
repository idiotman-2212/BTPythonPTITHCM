# EX 3.8 Write a function to find all combination of n elements of a given array whose sum is equal to a given value k.
# Write a function find_combinations(n, k, tmp_list) to find all combination of n elements of a given array whose sum is equal to a given value k.
#
# Test data
# Input:
#     4
#
#     53
#
#     [10, 20, 30, 40, 1, 2]
# Output:
#     [10, 50, 1, 2]
#     [20, 30, 1, 2]
from itertools import combinations
def find_combinations(n, k, tmp_list):
    subs = []
    temp = [list(x) for x in combinations(tmp_list, n)]
    for ele in temp:
        if sum(ele) == k:
            subs.append(ele)
    return subs

n = int(input())
k = int(input())
tmp_list = list(map(int, input().strip("[]").split(", ")))

result = find_combinations(n, k, tmp_list)
for i in range(0, len(result)):
    print(result[i], end = "")
    if i != len(result) - 1:
        print('', end='\n')


