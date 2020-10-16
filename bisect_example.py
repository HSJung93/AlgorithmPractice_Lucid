"""
Bisect:
- "Built-in" binary search method in Python.
- Can be used to search for an element in a sorted list.
"""

import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

print(bisect.bisect_left(A, 285))
print(bisect.bisect_right(A, 285))
print(bisect.bisect(A, 285))

print(A)
bisect.insort_right(A, 108)
print(A)