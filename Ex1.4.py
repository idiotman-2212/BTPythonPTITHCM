# EX 1.4 Check anagrams
# Two words are anagrams if you can rearrange the letters from one to spell the other. Write a code that takes two strings and prints True if they are anagrams and False otherwise.
# For example,
# - Input: race care
# - Output: True
s = input();
s1 = ""
s2 = ""
for i in range(len(s)):
    if(s[i] == " "):
        s1 = s[:i];
        s2 = s[i+1:len(s)]
if(sorted(s1) == sorted(s2)):
    print("True", end="");
else:
    print("False", end="");
