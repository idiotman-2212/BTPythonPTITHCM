# EX 2.13 Write a program to find all longest increasing sub-lists from a given list.
# Write a program to find all longest sub-lists from a given list.
# Test data 1
# Input:
#     10 22 99 33 21 50 41 60 80
# Output:
#     10, 22, 99
#     41, 60, 80
# Test data 2
# Input:
#     20 40 30 50 70 80 25 65 45
# Output:
#     30 50 70 80
l = list(map(int, input().split(" ")))

max_len = 1
count = 1;
for i in range(len(l)-1):
    if(l[i] <= l[i+1]):
        count += 1
        if(count >= max_len):
            max_len = count
    else:
        count = 1

result = []
count = 1;

for i in range(0, len(l)-1):
    if(l[i] <= l[i+1]):
        count += 1
        if(count == max_len):
            start = (i+1) - (max_len-1)
            for j in range(start, i+2):
                result.append(l[j])
            count = 1;
    else:
        count = 1;

line = 0
for i in range(0, len(result)):
    print(result[i], end = "")
    line += 1
    if line != max_len:
        print(" ", end = "")
    if line == max_len and i != len(result)-1:
        print()
        line = 0


