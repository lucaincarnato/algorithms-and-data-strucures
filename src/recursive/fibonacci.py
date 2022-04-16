'''
Script created by Luca Maria Incarnato
GitHub: lucaincarnato
Instagram: luca_incarnato
Twitter: incarnato_luca
'''

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1]+fibonacci_sequence[i-2])
    return fibonacci_sequence

'''
The recurrence equation of that algorithm is:
F0 = 0
F1 = 1 
Fn = Fn-1 + Fn-2
And that justify the iteration for i starting from 2 and the initial list
'''