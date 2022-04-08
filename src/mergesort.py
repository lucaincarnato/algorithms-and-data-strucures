from heapq import merge


def mergesort(S:list):
    if len(S) == 2:
        S[0], S[1] = min(S), max(S)
    else:
        index = len(S)//2
        S1 = S[:index]
        S2 = S[index:]
        L1 = mergesort(S1)
        L2 = mergesort(S2)
        L = L1 + L2
        return L
#! TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

mergesort([3, 1, 4, 5])