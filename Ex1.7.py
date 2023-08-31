# EX 1.7 List of unique elements
# Write a code that takes a list and returns a new list with only the unique elements from the original.
# For example,
# Input: 1, 2, 3, 4, 3
# Output: 1, 2, 3, 4
my_list = input().split(", ")

my_dict = {}
for i in range(0, len(my_list), 1):
    if (my_dict.get(my_list[i]) == None):
        my_dict[my_list[i]] = 1

my_list = []
for u in my_dict:
    my_list.append(u)

my_list.sort()

for i in range(0, len(my_list)):
    print(my_list[i], end="")
    if (i < (len(my_list) - 1)):
        print(", ", end="")


