'''
Script created by Luca Maria Incarnato
GitHub: lucaincarnato
Instagram: luca_incarnato
Twitter: incarnato_luca
'''

def insertionsort(array:list):
    #The first number is assumed sorted and evaluated
    for step in range(1, len(array)):
        # The key is the element to the right of the last number evaluated
        key = array[step]
        # array[i] is the number to the left of the key
        i = step - 1

        while i >= 0 and key < array[i]:
            # Evaluating if the key is greater than the elements at his left
            array[i + 1] = array[i] # array[step] == array[i]
            # Moving to the left to confront with the key 
            i = i - 1

        # The previous first index is now changed with the key if it is greater
        # It is not updated the key but the array[i], that now is i+1
        array[i + 1] = key # array[i + 1] == array[step]

    return array