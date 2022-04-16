'''
Script created by Luca Maria Incarnato
GitHub: lucaincarnato
Instagram: luca_incarnato
Twitter: incarnato_luca
'''

def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*factorial(n-1)
    else:
        return 'Error'

'''
The recurrence equation of that algorithm is
1! = 1
n! = n*(n-1)!
and that justify the difference between n == 1 and n > 1
'''