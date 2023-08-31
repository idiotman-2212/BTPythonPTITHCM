# EX 2.5 Write a function get_k_largest to get top k largest numbers from a list
# Write a function get_k_largest to get top k largest numbers from a list; then write a code to check your function.
# For example,
# Input:
#     2
#     1, 2, 3, 3, 0, 1, -10
# Output:
#     3, 2
#
# Please note that:
#     2 as k
#     1, 2, 3, 3, 0, 1, -10 as a list
def get_k_largest(k, l):
    l = list(set(l))
    l = sorted(l, reverse=True)
    result = []
    for i in range(0, k):
        result.append(l[i])
    return result


k = int(input())
l = list(map(int, input().split(", ")))

x = get_k_largest(k, l)

print("{}".format(x[0]), end="")
for i in range(1, k):
    print(", {}".format(x[i]), end="")


