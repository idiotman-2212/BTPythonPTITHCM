# EX 1.5 Check ascending order list
# EX 1.5
# Write a code that takes a list as a parameter and prints True if the list is sorted in ascending order and False  otherwise.
# Please do not sort the list, just check it.
# For example,
# Input: 1, 2, 3, 4
# Output: True
mystr = input();
test_list = mystr.split()
flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1
# printing result
if (not flag) :
    print ("True", end="")
else :
    print ("False", end="")


