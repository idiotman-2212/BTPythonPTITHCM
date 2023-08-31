# EX 2.6 Write a function get_k_common_numbers to find the occurrences of top k most common numbers in a given list.
# Write a function get_k_common_numbers to find the occurrences of top k most common numbers in a given list.
# If there are numbers that have the same occurrences and the most common numbers are larger than k, then the smaller number is chosen.
# Please don't use Counter of collections library.
# Write a program to test your function.
# Test data 1:
# Input:
#     3  // as k
#     10, 90, 70, 80, 50, 10, 70, 90, 90  // as a list
# Output:
#     (90, 10, 70) // as k most common numbers
#     (3, 2, 2) // as corresponding occurrences of k most common numbers
# Test data 2:
# Input:
#     2
#     10, 90, 70, 80, 50, 10, 70, 90, 90
# Output:
#     (90, 10), (3, 2)
k = int(input())
l = list(map(int, input().split(", ")))

d = {key: 0 for key in l}

for x in l:
    value = d.get(x) + 1
    d.update({x: value})

occ = list(d.values())
occ = sorted(occ, reverse=True)

tup_value = list()
tup_occ = list()

start = 0
l_key = list(set(d.keys()))
l_key = sorted(l_key, reverse=True)

for key in l_key:
    if d.get(key) == occ[start]:
        tup_value.append(key)
        tup_occ.append(d.get(key))
        d.update({key: -1})
        start += 1
    if start == k:
        break

tup_value = tuple(tup_value)
tup_occ = tuple(tup_occ)
print("{}, {}".format(tup_value, tup_occ), end="")


