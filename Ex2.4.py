# EX 2.4 Write a function is_unique to check whether a list has unique elements or not
# Write a function is_unique that takes a list and prints True if there is any element that appears more than once, otherwise, prints False; then write a code to check the function.
#
# For example,
# Input: 1, 2, 3, 4, 3
# Output: True

def is_unique(s, l):
    if len(set(l)) == len(l):
        print("False",end="")
    else:
        print("True", end="")
s = input();
l = s.split();
is_unique(s, l)


