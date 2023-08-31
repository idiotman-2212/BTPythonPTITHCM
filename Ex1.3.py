# EX 1.3 Check palindromes
# A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider". Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
# Write a code to check if a string is a palindrome or not.
# If a string S is a palindrome, print True, otherwise, print False.
string = input()
string_lo = string.lower()
string_re = string_lo[::-1]
if string_lo==string_re:
    print ("True", end= "")
else:
    print ("False",end= "")

