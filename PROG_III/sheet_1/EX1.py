def findMax(list):
    if not list:
        return None
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value

list = [3, 5, 2, 8, 1]
max_value = findMax(list)

print(f"The maximum value in the list is: {max_value}")