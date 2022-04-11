'''
Script created by Luca Maria Incarnato
GitHub: lucaincarnato
Instagram: luca_incarnato
Twitter: incarnato_luca
'''

def mergesort(array:list):
    # The script will be executed only when the lenght of the (sub)array is greater than one
    # The array of lenght one cannot be divided anymore
    if len(array) > 1:
        R = array[len(array)//2:]
        L = array[:len(array)//2]
        mergesort(R)
        mergesort(L)
        # The recursion will be called for every division of the array into subarrays.
        # It also creates a stack of all the istances not exectuded but only when the lenght of the array is one
        # it will be stopped the recursion calls and will  execute the stacks of previous calls.


        # We compare the single elements of a subarray with the element of the other following the pointers
        # When the left is minor than right element the right pointer (i) will be incremented, if not the left (j)
        # In both cases the major array pointer (k) will be incremented to change array index
        i = j = k = 0
        while i < len(R) and j < len(L):
            if R[i] < L[j]:
                array[k] = R[i]
                i = i + 1
                k = k + 1
            else:
                array[k] = L[j]
                j = j + 1
                k = k + 1

        # When one of the two pointer exceed the lenght of the relative array it will be compared 
        # the remained elements of the other and added to the major one
        while i < len(R):
            array[k] = R[i]
            i = i + 1
            k = k +1
        while j < len(L):
            array[k] = L[j]
            j = j + 1
            k = k + 1
        
        return array

lis = [4, 8, 7, 2, 6, 1]
print(mergesort(lis))