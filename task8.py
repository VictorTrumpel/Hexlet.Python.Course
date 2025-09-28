def pal(t):
    t = t.replace(" ", "")

    if len(t) <= 1:
        return True

    if t[0] != t[-1]:
        return False
        
    return pal(t[1:-1])

print(pal("а роза упала на лапу азора"))
print(pal("hello"))  