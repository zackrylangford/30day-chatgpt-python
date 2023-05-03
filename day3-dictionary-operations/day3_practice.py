#2 - Access
# Let's start with a simple dictionary
d = {"apple": 1, "banana": 2, "cherry": 3}

# Accessing a value by its key
print(d["apple"])  # Output: 1

# Trying to access a non-existent key will raise a KeyError
# print(d["orange"])  # This would raise: KeyError: 'orange'

# The get method can be used to avoid the KeyError
# If the key exists, get returns the value
print(d.get("banana"))  # Output: 2

# If the key does not exist, get returns None
print(d.get("orange"))  # Output: None

# You can also provide a default value to return if the key is not in the dictionary
print(d.get("orange", "Not found"))  # Output: Not found


#3 Insert/Update
# Let's start with an empty dictionary
d = {}

# Inserting key-value pairs into the dictionary
d["apple"] = 1
d["banana"] = 2
d["cherry"] = 3

print(d)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

# Updating the value associated with a key
d["apple"] = 4
print(d)  # Output: {'apple': 4, 'banana': 2, 'cherry': 3}

# Inserting a new key-value pair
d["orange"] = 5
print(d)  # Output: {'apple': 4, 'banana': 2, 'cherry': 3, 'orange': 5}

# Using the update method to add or update multiple key-value pairs at once
d.update({"apple": 6, "banana": 7, "grape": 8})
print(d)  # Output: {'apple': 6, 'banana': 7, 'cherry': 3, 'orange': 5, 'grape': 8}

# Using the update method with an iterable of key-value pairs
d.update([("apple", 9), ("cherry", 10)])
print(d)  # Output: {'apple': 9, 'banana': 7, 'cherry': 10, 'orange': 5, 'grape': 8}


names = {"Zack": [38,'blonde'], "Becca": [39, 'brown']}

print(names["Zack"])
print(names["Becca"])

print("Zack" in names)
print("Becca" in names)
print("Sam" in names)
print(names.get("Sam"))
print(names.get("Sam", "Nope"))
print(names)



new_names = {}

new_names["Zack"] = 1
new_names["Becca"] = 2
new_names["Sam"] = 3
new_names["Isaiah"] = 4
new_names["Henry"] = 5
print(new_names)

new_names["Zack"] = 5
print(new_names)

new_names.update({"Zack": 2, "Becca": 7, "Maisy": 8})

print(new_names)

del new_names["Zack"]
print(new_names)

get = new_names.popitem()

print(new_names)
print(get)

print(sorted(new_names))

getnow = iter(new_names)
print(next(getnow))
print(next(getnow))
print(next(getnow))
print(next(getnow))

keys = new_names.keys()
values = new_names.values()
print(keys)
print(values)

#1
student = {'name': 'Zack', 'age': 38, 'grade': 12, 'subjects': ['math', 'science', 'computers']}

print(student.keys())
print(student.values())

#2
d = {'A': 1, 'B': 2, 'C': 3}
print(d)
# Swap keys and values using a dictionary comprehension
swapped_d = {v: k for k, v in d.items()}

print(swapped_d)  # Output: {1: 'A', 2: 'B', 3: 'C'}

#3 

if swapped_d:
    print(swapped_d.popitem())
else:
    print("The dictionary is empty.")
if swapped_d:
    print(swapped_d.popitem())
else:
    print("The dictionary is empty.")
if swapped_d:
    print(swapped_d.popitem())
else:
    print("The dictionary is empty.")
if swapped_d:
    print(swapped_d.popitem())
else:
    print("The dictionary is empty.")
