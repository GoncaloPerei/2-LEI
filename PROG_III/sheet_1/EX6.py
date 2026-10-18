def binarySearch(list, target):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

lists = [10, 20, 30, 40, 50, 60, 70]

print("Índice do 40:", binarySearch(lists, 40))
print("Índice do 25:", binarySearch(lists, 25))