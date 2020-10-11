"""
Define a bitonic sequence as a sequence of intergers such that: x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

For example:
 1, 2, 3, 4, 5, 4, 3, 2, 1

 is a bitonic sequence. Write a program to find the largest element in such a sequence. In the example above, the program should return "5".

 We assume that such a "peak" element exists.
"""

# Peak element is "5"
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Peak element is "4"
B = [1, 2, 3, 4, 1]

# Peak element is "6"
C = [1, 6, 5, 4, 3, 2, 1]

def find_highest_number(A):
    low = 0
    high = len(A) - 1

    # Require at least 3 elements for a valid bitonic sequence
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1 
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]

a = find_highest_number(A)
b = find_highest_number(B)
c = find_highest_number(C)
print(a)
print(b)
print(c)