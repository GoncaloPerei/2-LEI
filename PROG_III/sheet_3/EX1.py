# =====================================================================
# DATASET
# =====================================================================
students = [
    {
    "number": 101,
    "name": "Ana",
    "grades": [("Matemática", 16), ("Programação", 18), ("Inglês", 14)]
    },
    {
    "number": 102,
    "name": "Bruno",
    "grades": [("Matemática", 9), ("Programação", 15), ("Inglês", 13)]
    },
    {
    "number": 103,
    "name": "Carla",
    "grades": [("Matemática", 17), ("Programação", 16), ("Inglês", 18)]
    }
]

# =====================================================================
# HELPER FUNCTIONS
# =====================================================================
def get_student_average(student):
    """Calculates the average grade for a given student."""
    total = sum(grade for subject, grade in student["grades"])
    return round((total / len(student["grades"])), 2)

def class_average(subject):
    """Calculates the class average for a specific subject across all students."""
    total = 0
    count = 0
    for student in students:
        for subj, grade in student["grades"]:
            if subj == subject:
                total += grade
                count += 1
    return round((total / count), 2) if count > 0 else None

# =====================================================================
# EXERCISE 1: Map student ID (number) to average grade
# =====================================================================
# Create a dictionary associating each student's ID number with their rounded average
student_averages = dict((student["number"], get_student_average(student)) for student in students)
print(f"1. Student averages (by ID): {student_averages}")

# =====================================================================
# EXERCISE 2: Sort (name, average) descending by grade, break ties by name
# =====================================================================
# Generate pairs of (name, average) and sort them:
# -x[1] sorts by average descending; x[0] sorts alphabetically ascending as a tiebreaker
student_averages_name = dict((student["name"], get_student_average(student)) for student in students)
average_decreasing = sorted(student_averages_name.items(), key=lambda x: (-x[1], x[0]))
print(f"2. Student averages (decreasing or by name): {average_decreasing}")

# =====================================================================
# EXERCISE 3: Calculate the average grade for each subject
# =====================================================================
# Compute the average for each subject
class_averages = {}
for subject in ["Matemática", "Programação", "Inglês"]:
    class_averages[subject] = class_average(subject)

print(f"3. Class averages: {class_averages}")

# =====================================================================
# EXERCISE 4: Identify students with at least one failing grade (< 10)
# =====================================================================
# Filter students who have at least one grade strictly below 10
negative_grades = {
    student["name"]: [(subj, grade) for subj, grade in student["grades"] if grade < 10]
    for student in students
    if any(grade < 10 for _, grade in student["grades"])
}
print(f"4. Students with negative grades: {negative_grades}")

# =====================================================================
# EXERCISE 5: Find top-performing student(s) per subject (handles ties)
# =====================================================================
# Step 5.1: Group all grades and student names by subject
grades_by_subject = {}
for student in students:
    for subject, grade in student["grades"]:
        grades_by_subject.setdefault(subject, []).append((student["name"], grade))

# Step 5.2: Identify the maximum grade and all students who achieved it
top_students_by_subject = {}
for subject, records in grades_by_subject.items():
    max_grade = max(grade for _, grade in records)
    top_students = [name for name, grade in records if grade == max_grade]
    top_students_by_subject[subject] = {
        "grade": max_grade,
        "students": top_students
    }

print(f"5. Top students by subject: {top_students_by_subject}")

