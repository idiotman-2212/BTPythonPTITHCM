# EX 1.10 Get the weekday of an input date
# Given the date (2022, 05, 02) is a Monday, write a program to get the weekday of an input date of year 2022.
# For example,
# Input: 2022, 05, 11
# Output: Wednesday
s = input();
s1 = ""
s2 = ""
s3 = ""
s1 = s[:4];
s2 = s[6:8]
s3 = s[10:]
s1 = int(s1);
s2 = int(s2);
s3 = int(s3)
n = (s3+2*s2+(3*(s2+1)) // 5 + s1 + (s1 // 4)) % 7;
if n==1:
    print("Monday", end="");
elif n==2:
    print("Tuesday", end="");
elif n==3:
    print("Wednesday", end="");
elif n==4:
    print("Thursday", end="");
elif n==5:
    print("Friday", end="");
elif n==6:
    print("Saturday", end="");
else:
    print("Sunday", end="");
