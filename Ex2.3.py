# EX 2.3 Write a function is_ascending to check ascending order list
# Write a function is_ascending that takes a list as a parameter and prints True if the list is sorted in ascending order and False otherwise. Then, write a code to check the function.
# Please do not sort the list, just check it.
#
# For example,
# Input: 1, 2, 3, 4
# Output: True

def is_ascending(test_list):
    flag = 0
    i = 1
    while i < len(test_list):
        if(test_list[i] < test_list[i - 1]):
            flag = 1
        i += 1
    if (not flag) :
        print ("True", end="")
    else :
        print ("False", end="")


mystr = input();
test_list = mystr.split()
is_ascending(test_list)
