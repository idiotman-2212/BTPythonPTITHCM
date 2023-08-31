# EX 3.10 Write a function to rearrange a given array of unique elements such that every second element of the array is greater than its left and right elements.
# Write a function rearrange(list_nums) to rearrange a given array of unique elements such that every second element of the array is greater than its left and right elements.
#
# Test data
#
# Input: [1, 2, 4, 9, 5, 3, 8, 7, 10, 12, 14]
#
# Output: [1, 4, 2, 9, 3, 8, 5, 10, 7, 14, 12]
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
def rearrangeArray(A):
    for i in range(1, len(A), 2):
        if A[i - 1] > A[i]:
            swap(A, i - 1, i)
        if i + 1 < len(A) and A[i + 1] > A[i]:
            swap(A, i + 1, i)
if __name__ == '__main__':
    A = list(map(int, input().strip("[]").split(", ")))
    rearrangeArray(A)
    print(A)
