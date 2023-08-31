# EX 2.8 Write a function compute_edit_distance to compute edit distance between two strings
# Edit distance is a string metric that quantifies how dissimilar two strings are to one another, that is measured by counting the minimum number of operations (delete, insert, replace) required to transform one string into the other.
#
# Write a function compute_edit_distance to compute edit distance between two strings and write a code to check your function.
# Test data 1
# Input: kitten, sitting
# Output: 3
# Test data 2
# Input: bear, hear
# Output: 1
l = input().split();
s1 = l[0];
s2 = l[1];
res = len(s2) - len(s1);
for i in range(0, len(s1)):
    if (s1[i] not in s2):
        res += 1;
print(res, end="")

