"""

**Exercises:**

1. **Nested Dictionary**: Given a nested dictionary representing a company's employee hierarchy, extract the email addresses of all employees.
```python
employees = {
    'Alice': {
        'title': 'Manager',
        'email': 'alice@example.com'
    },
    'Bob': {
        'title': 'Developer',
        'email': 'bob@example.com'
    },
    'Carol': {
        'title': 'HR',
        'email': 'carol@example.com'
    }
}
```

2. **Dictionary Comprehension**: Given a list of words, create a dictionary comprehension that generates a dictionary with the words as keys and their lengths as values.

3. **Merging Dictionaries**: Given three dictionaries `dict1`, `dict2`, and `dict3`, write a Python program that merges them into a single dictionary, with values from `dict3` taking precedence over `dict2`, and values from `dict2` taking precedence over `dict1`.

4. **Dictionary Filtering**: Given a dictionary of items and their prices, create a dictionary comprehension that generates a new dictionary containing only the items with a price greater than 20.

5. **Nested Dictionary Extraction**: Given a nested dictionary representing students and their courses, extract all the courses into a single list without duplicates.

```python
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
```

These exercises should help you practice and understand complex dictionary tasks better. Good luck!

"""
"""

#1 

employees = {
    'Alice': {
        'title': 'Manager',
        'email': 'alice@example.com'
    },
    'Bob': {
        'title': 'Developer',
        'email': 'bob@example.com'
    },
    'Carol': {
        'title': 'HR',
        'email': 'carol@example.com'
    }
}
print(employees)
email_list = []

for name, details in employees.items():
    email_list.append(details['email'])

print(email_list)

email_list = [details['email'] for details in employees.values()]
print(email_list)


family = {"zack": {
        "age": 26, 
        "favorite food": "cheeseburger"
        }, 
        "becca":{
            "age": 26,
            "favorite food": "pasta"
        }
        }
family_list = []

for name, details in family.items():
    family_list.append(details['favorite food'])

    

family_list.append('tacos')
print(family_list)

lengths = {food:len(food) for food in family_list}
print(lengths)


print(lengths)


#3

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {
    'b': 20,
    'c': 30,
    'd': 40
}

dict3 = {
    'c': 300,
    'd': 400,
    'e': 500
}


merged_dict = {**dict1, **dict2, **dict3}

print(merged_dict)
#4 
items_prices = {
    'item1': 12,
    'item2': 25,
    'item3': 8,
    'item4': 35,
    'item5': 17,
    'item6': 30,
    'item7': 5
}

filtered_dict = {item: price for item, price in items_prices.items() if price > 20}

print(items_prices)
print(filtered_dict)

#5 5. **Nested Dictionary Extraction**: Given a nested dictionary representing students and their courses, extract all the courses into a single list without duplicates.

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

single_list = []

for value in students.values():
    single_list.extend(value['courses'])

print(single_list)

# Remove duplicates by converting to a set and back to a list
unique_courses = list(set(single_list))
print(unique_courses)


"""

list = [4,3,2,1]

list.sort(reverse=True)
print(list)