# EX 2.11 Write a program to compute the difference between two dates.
# Write a program to compute the difference between two dates.
# Test data 1:
# Input:
#     01/01/2022
#     02/02/2022
# Output:
#     32
# Test data 2:
# Input:
#     16/02/2000
#     15/04/2000
# Output:
#     59
import datetime

l1 = input().split("/")
l2 = input().split("/")

day1 = int(l1[0])
month1 = int(l1[1])
year1 = int(l1[2])

day2 = int(l2[0])
month2 = int(l2[1])
year2 = int(l2[2])

date1 = datetime.date(year1, month1, day1)
date2 = datetime.date(year2, month2, day2)
if (date2-date1).days > 0:
    print("{}".format((date2-date1).days), end = "")
else:
    print((date1-date2).days, end = "")

