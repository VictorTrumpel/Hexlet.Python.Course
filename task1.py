def F(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    if n % 3 == 0:
        return F(n - 1) + n * n + 3
    else:
        return F(n - 2) + n - 6

def all_digits_odd(x):
    for d in str(x):
        if int(d) % 2 == 0:  # есть чётная цифра
            return False
    return True

count = 0
for n in range(1, 1001):
    if all_digits_odd(F(n)):
        count += 1

print("Количество n:", count)
