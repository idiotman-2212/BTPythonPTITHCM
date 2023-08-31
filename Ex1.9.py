# EX 1.9 The most Frequently Occurring Items
# EX 1.9 Write a program that gets a list L and print the most Frequently Occurring Items in L.
# For example,
# Input: 1, 2, 3, 3, 0, 1
# Output: 1, 3
my_list = input().split(", ")

my_dict = {}
for u in my_list:
    if my_dict.get(u) == None:
        my_dict[u] = 1
    else:
        my_dict[u] += 1

max = 0
for (u, v) in my_dict.items():
    if v > max:
        max = v

my_list = []
for (u, v) in my_dict.items():
    if v == max:
        my_list.append(u)

for i in range(0, len(my_list)):
    print(my_list[i], end= "")
    if i < len(my_list) - 1:
        print(", ", end= "")



