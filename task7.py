def findindex(*args, target, idx=0):
    if idx >= len(args):
        return -1

    if args[idx] == target:
        return idx
        
    return findindex(*args, target=target, idx=idx+1)

print(findindex(4, 3, 1, 6, 8, 9, target=6))
print(findindex(6, 3, 4, 1, 8, 9, target=5))