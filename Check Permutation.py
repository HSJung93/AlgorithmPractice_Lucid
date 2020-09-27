"""
Given two stirngs, write a method to decide if one is a permutation of the other.
"""

is_permutation_1 = "God"
is_permutation_2 = "dog"

not_permutation_1 = "Not"
not_permutation_2 = "top"


def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True

print(is_perm_1(is_permutation_1, is_permutation_2))

print(is_perm_1(not_permutation_1, not_permutation_2))