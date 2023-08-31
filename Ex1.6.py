# EX 1.6 Check unique elements
# EX 1.6
# Write a code that takes a list and prints True if there is any element that appears more than once, otherwise, prints False. It should not modify the original list.
# For example,
# Input: 1, 2, 3, 4, 3
# Output: True
s = input();
l = s.split();
if len(set(l)) == len(l):
    print("False",end="")
else:
    print("True", end="")




