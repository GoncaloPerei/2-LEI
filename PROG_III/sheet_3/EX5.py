grades = {
    "Ana": [("Livro A", 5), ("Livro B", 3)],
    "Bruno": [("Livro A", 4), ("Livro C", 5), ("Livro D", 2)],
    "Carla": [("Livro B", 4), ("Livro C", 4), ("Livro D", 5)],
    "Daniel": [("Livro A", 3), ("Livro C", 3), ("Livro E", 5)]
}

grades_by_book = {}

for student, books in grades.items():
    for book, grade in books:
        if book not in grades_by_book:
            grades_by_book[book] = []
        grades_by_book[book].append(grade)

print(f"Grades by book: {grades_by_book}")

def average_grade(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def count_ratings(grades):
    return len(grades)

statistics_per_book = {}
for book, book_grades in grades_by_book.items():
    statistics_per_book[book] = (average_grade(book_grades), count_ratings(book_grades))

print(f"Statistics per book: {statistics_per_book}")

def recommend_books(ratings, user, min_ratings=2, limit=3):
    user_books = {book for book, _ in ratings.get(user, [])}
    
    item_grades = {}
    for _, user_ratings in ratings.items():
        for book, grade in user_ratings:
            item_grades.setdefault(book, []).append(grade)
            
    candidates = []
    for book, g_list in item_grades.items():
        ratings_count = count_ratings(g_list)
        
        if book not in user_books and ratings_count >= min_ratings:
            avg = average_grade(g_list)
            candidates.append((book, avg, ratings_count))
    
    candidates.sort(key=lambda x: (-x[1], -x[2], x[0]))
    
    return candidates[:limit]

print(f"Recommendations for Ana: {recommend_books(grades, 'Ana')}")