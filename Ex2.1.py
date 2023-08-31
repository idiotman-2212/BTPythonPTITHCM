# EX 2.1 Write a function is_palindrome to check whether a string is a palindrome or not.
# A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider". Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
# Write a function is_palindrome to check whether a string is a palindrome or not, then test the function.
# If a string S is a palindrome, return True, otherwise, return False.
def is_palindrome(string_re):
    if string_lo == string_re:
        print("True", end="")
    else:
        print("False", end="");
string = input();
string_lo = string.lower();
string_re = string_lo[::-1];
is_palindrome(string_re);

