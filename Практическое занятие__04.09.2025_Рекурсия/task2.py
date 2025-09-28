def indicator(number, base):
    if number == 1:
        return 0
    elif number < 1:
        return -1 + indicator(number * base, base)
    else:
        return 1 + indicator(number // base, base)

print(indicator(16, 2))
print(indicator(1/625, 5))