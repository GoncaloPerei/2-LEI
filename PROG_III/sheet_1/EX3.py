def removeDuplicates(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result

print(f"List without duplicates: {removeDuplicates([1, 2, 3, 2, 1, 4, 5, 3])}")
