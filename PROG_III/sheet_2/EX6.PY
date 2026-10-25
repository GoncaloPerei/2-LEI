dict1 = {'a': 1, 'b': 2, 'c': 3}

dict1_inverted = {value: key for key, value in dict1.items()}

print(f"Inverted dictionary: {dict1_inverted}")