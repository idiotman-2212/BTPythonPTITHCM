# EX 2.9 Write a function count_words that reads a string and returns only the words with more than k characters (not counting whitespace).
# Write a function count_words that reads a string and return a list of only the words with more than k characters (not counting whitespace).
#
# Write a code to check your function.
# Test data 1
# Input:
#     8
#     which is a perfectly legitimate word, so stop looking at me like that.
# Output:
#     [perfectly, legitimate]
n = int(input())
l = input();
i = 0;
while i < len(l):
    if not l[i].isalpha() and not l[i].isalnum() and l[i] != " ":
        l = l.replace(l[i], " ")
    else:
        i += 1;
l = l.split(" ")
res = [];
for x in l:
    if len(x) > n:
        res.append(x);
if res:
    print("[{}".format(res[0]), end="")
for i in range(1, len(res) - 1):
    print(", {}".format(res[i]), end="")
if len(res) > 1:
    print(", {}]".format(res[len(res) - 1]), end="")
else:
    print("]", end="")



