"""
Given a string, write a function to check if it is permutation of a palindrome. A palindrome is a word or pharse that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

palin_perm = "Tack Coa" # Taco Cat
not_plain_perm = "This is not a palindrome permutation"

# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_plain_perm))

