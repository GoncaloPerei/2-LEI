def checkEvenUneven(list):
    even = 0
    uneven = 0

    for number in list: 
        if number % 2 == 0: 
            even += 1
        else:
            uneven += 1

    print(f"Even numbers: {even}, Uneven numbers: {uneven}")

num = [1, 2, 3, 4, 5]

checkEvenUneven(num)