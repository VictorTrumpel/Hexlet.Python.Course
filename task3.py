def multidigits(number, current = 1, idx = 0):
    digits = [int(d) for d in str(number)]

    if idx >= len(digits):
        return current

    newValue = current * digits[idx]

    return multidigits(number, newValue, idx + 1)

print(multidigits(0)) # 0

print(multidigits(12)) # 2

print(multidigits(33)) # 9