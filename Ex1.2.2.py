# EX 1.2.2 Write a program to break an integer into a sequence of individual digits.
# EX 1.2 Write a program to break an integer into a sequence of individual digits.
# Please note that your input is an integer (not a string)
# Test Data
# Input six non-negative digits: 12345
# Expected Output: 5 4 3 2 1
n = int(input())
s = str(n)
for i in range(0,len(s)):
    if(i != len(s)-1):
        print(s[i], end =' ');
    else:
        print(s[i], end = '');


