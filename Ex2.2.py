# EX 2.2 Write a function is_anagrams to check whether two words are anagrams
# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function is_anagrams to check whether two words are anagrams, the function returns True is two words are anagrams, otherwise, return False; then write a code to test the function.
# For example,
# - Input: race care
# - Output: True
def is_annagrams(s, s1, s2):
    for i in range(len(s)):
        if(s[i] == " "):
            s1  = s[:i]
            s2 = s[i+1:len(s)]
    if(sorted(s1) == sorted(s2)):
     print("True", end="");
    else:
     print("False", end="");


s = input()
s1 = ""
s2 = ""
is_annagrams(s,s1,s2)



