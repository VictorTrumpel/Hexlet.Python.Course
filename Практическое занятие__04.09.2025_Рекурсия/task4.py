def factorial(n):
    if n == 0 or n == 1:
        return 1
        
    return n * factorial(n-1)

def comb(n, k):
    if k < 0 or k > n:
        return 0

    return factorial(n) // (factorial(k) * factorial(n-k))

def count_sequences(a, b):
    return comb(b + 1, a)

print(count_sequences(2, 3)) 