# EX 1.2 Write a program to break an integer into a sequence of individual digits.
# EX 1.2 Write a program to break an integer into a sequence of individual digits.
# Test Data
# Input six non-negative digits: 123456
# Expected Output: 1 2 3 4 5 6
n = input();
for i in range(0, len(n)):
    if (i != len(n)-1):
        print(n[i], end = ' ');
    else:
        print(n[i], end = '');

