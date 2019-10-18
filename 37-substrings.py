"""
GIVEN TWO ARRAYS OF STRINGS A AND B.
RETURN A SORTED ARRAY IN LEXICOGRAPHICAL ORDER OF STRINGS OF A WHICH ARE SUBSTRINGS OF B.
"""

A = ["arp", "live", "strong"]

B = ["lively", "harp", "alive", "sharp"]

C = []

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] in B[j]:
            C.append(A[i])

final_list = []

for string in C:
    if string not in final_list:
        final_list.append(string)


print(final_list)
