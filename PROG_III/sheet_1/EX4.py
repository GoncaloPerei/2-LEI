def generateTable():
    number = int(input("Enter a number: "))
    print(f"--- Multiplication Table of {number} ---") 
    for i in range(1, 11): 
        print(f"{number} x {i} = {number * i}")

generateTable()