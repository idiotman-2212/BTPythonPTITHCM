# EX 1.8 Find reverse pairs
# EX 1.8
# Two words are a "reverse pair" if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list.
# For example,
# Input: "abc", "4567", "7654", "cba"
# Output: ("abc", "cba"), ("4567", "7654")

my_list = input().split(", ")

my_dict = {}
for u in my_list:
    my_dict[u] = 1

my_list = []
for u in my_dict:
    v = u[::-1]
    if(my_dict.get(v) == 1):
        my_list.append([u, v])
        my_dict[u] = 0
        my_dict[v] = 0

for i in range(0, len(my_list)):
    (u, v) = my_list[i]
    message = "({}, {})".format(u, v)
    print(message, end= "")
    if i < (len(my_list) - 1):
        print(", ", end= "")
