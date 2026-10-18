def rotateList(lst, n):
    if not lst:
        return lst 
    n = n % len(lst)
    return lst[n:] + lst[:n]

print(f"Rotated list: {rotateList([1, 2, 3, 4, 5], 2)}") 