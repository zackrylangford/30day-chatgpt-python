"""

**Exercises**:

1. **Average Age**: Given a list of dictionaries representing students with their names, ages, and grades, calculate the average age of the students.

2. **Grade Distribution**: Given a list of dictionaries representing students with their names, ages, and grades, create a dictionary with grades as keys and lists of student names as values.

3. **Filter by Grade**: Given a list of dictionaries representing students with their names, ages, and grades, create a new list of dictionaries containing only the students who have a specific grade.

4. **Update Inventory**: Given a list of sold items (each represented by a dictionary with a product name and quantity) and an inventory dictionary with product names as keys and quantities as values, update the inventory to reflect the sold items.

5. **Nested Dictionary to List**: Given a nested dictionary representing students and their courses, extract all the courses into a single list without duplicates.

Feel free to ask for clarification, examples, or help with the exercises. Good luck with your study session!


"""

# 1 **Average Age**: Given a list of dictionaries representing students with their names, ages, and grades, calculate the average age of the students.

students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 22, 'grade': 88},
    {'name': 'Carol', 'age': 19, 'grade': 92},
    {'name': 'Dave', 'age': 21, 'grade': 78}
]

# My solution
age_total = 0
student_total = len(students)
for student in students:
    age_total += student['age']
print(age_total/student_total)

#GPT Solution (cleaner)
average_age = sum(student['age'] for student in students) / len(students)
print(average_age)


#2

students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 22, 'grade': 'B'},
    {'name': 'Carol', 'age': 19, 'grade': 'A'},
    {'name': 'Dave', 'age': 21, 'grade': 'C'},
    {'name': 'Eve', 'age': 22, 'grade': 'B'}
]

new_dict = {grade:name for student['grade'] in students, student['name'] in students}
print(new_dict)

#3

students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 22, 'grade': 'B'},
    {'name': 'Carol', 'age': 19, 'grade': 'A'},
    {'name': 'Dave', 'age': 21, 'grade': 'C'},
    {'name': 'Eve', 'age': 22, 'grade': 'B'}
]

#4
sold_items = [
    {'product': 'apple', 'quantity': 5},
    {'product': 'banana', 'quantity': 2},
    {'product': 'orange', 'quantity': 3}
]

inventory = {
    'apple': 10,
    'banana': 8,
    'orange': 15
}

#5
students = {
    'Alice': {
        'courses': ['Math', 'Physics']
    },
    'Bob': {
        'courses': ['Physics', 'Chemistry']
    },
    'Carol': {
        'courses': ['Biology', 'Math']
    }
}

