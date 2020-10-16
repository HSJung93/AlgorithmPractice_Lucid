"""
Write a function that takes a non-negative interger and returns the largest integer whose square is less than or equal to the interger given.
"""

k = 300

def integer_square_root(k):

    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1 

print(integer_square_root(k))