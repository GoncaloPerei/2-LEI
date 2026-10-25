grades = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

lowest_subject = min(grades, key=grades.get)

print(f"Lowest subject is: {lowest_subject}")