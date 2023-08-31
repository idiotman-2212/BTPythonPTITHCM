# EX 2.12 Write a program to check whether a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
# Write a program to check whether a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
# Test data 1
# Input:
#     abc,123
# Output:
#     False
# Test data 2
# Input:
#     convert2string
# Output:
#     True
import re
text = input()
result = re.sub("[A-Za-z0-9]", '', text)
if len(result) == 0:
   print("True", end="")
else :
   print("False", end="")

