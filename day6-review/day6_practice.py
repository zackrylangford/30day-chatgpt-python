"""

**Exercises**

1. List Comprehension: Given a list of numbers, create a list comprehension that generates a new list containing the squares of the numbers that are divisible by 3.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

2. Complex List Manipulation: Given two lists, use a list comprehension with a nested loop to create a new list containing tuples with the element from the first list as the first element and the element from the second list as the second element.

```python
list1 = ['apple', 'banana', 'cherry']
list2 = [1, 2, 3]
```

3. Dictionary Operation: Given a dictionary of students and their ages, add a new student to the dictionary and update the age of an existing student.

```python
students = {
    'Alice': 20,
    'Bob': 22,
    'Carol': 19
}
```

4. Complex Dictionary Task: Given a dictionary with lists as values, create a new dictionary that has the same keys but with the average of the values in each list.

```python
grades = {
    'Math': [85, 90, 78],
    'Physics': [92, 88, 75],
    'Chemistry': [89, 84, 91]
}
```

5. Combining Lists and Dictionaries: Given a list of dictionaries, create a new dictionary that maps each unique 'category' value to a list of dictionaries with that category.

```python
items = [
    {'name': 'apple', 'category': 'fruit'},
    {'name': 'banana', 'category': 'fruit'},
    {'name': 'spinach', 'category': 'vegetable'},
    {'name': 'carrot', 'category': 'vegetable'}
]
```

After you've attempted these exercises, feel free to ask for help or feedback on your solutions. Good luck with your review session!

"""


#1 List Comprehension: Given a list of numbers, create a list comprehension that generates a new list containing the squares of the numbers that are divisible by 3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [i**2 for i in numbers if i % 3 == 0]

print(new_list)

#2 Complex List Manipulation: Given two lists, use a list comprehension with a nested loop to create a new list containing tuples with the element from the first list as the first element and the element from the second list as the second element.

list1 = ['apple', 'banana', 'cherry']
list2 = [1, 2, 3]

list3 = [(x, y) for x in list1 for y in list2]
print(list3)

#3 Dictionary Operation: Given a dictionary of students and their ages, add a new student to the dictionary and update the age of an existing student.

students = {
    'Alice': 20,
    'Bob': 22,
    'Carol': 19
}

students['Dave'] = 25
students['Alice'] = 21
print(students)

#4 Complex Dictionary Task: Given a dictionary with lists as values, create a new dictionary that has the same keys but with the average of the values in each list.

grades = {
    'Math': [85, 90, 78],
    'Physics': [92, 88, 75],
    'Chemistry': [89, 84, 91]
}

averages = {subject: sum(grades_list)/len(grades_list) for subject, grades_list in grades.items()}
print(averages)


#5 Combining Lists and Dictionaries: Given a list of dictionaries, create a new dictionary that maps each unique 'category' value to a list of dictionaries with that category.


items = [
    {'name': 'apple', 'category': 'fruit'},
    {'name': 'banana', 'category': 'fruit'},
    {'name': 'spinach', 'category': 'vegetable'},
    {'name': 'carrot', 'category': 'vegetable'}
]

categories = {}

for item in items:
    # get the category of the item
    category = item['category']

    # if the category is not already a key in the dictionary, add it
    if category not in categories:
        categories[category] = []

    # append the current item to the correct category
    categories[category].append(item)

print(categories)
