"""
**Exercises**

1. Create a list comprehension that generates the squares of the numbers from 1 to 10.
2. Use a list comprehension to create a new list of the cubes of the numbers from 1 to 10, but only if the cube is evenly divisible by 4.
3. Given the list `names = ['Nick', 'Alice', 'Kitty', 'Lionel', 'Daisy']`, create a list comprehension that generates a new list containing only the names that start with an 'L'.
4. Use a list comprehension to create a list of all the years from 1900 to 2100 that are leap years. (Hint: a leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400).

These exercises should give you a good sense of how list comprehensions work. Feel free to ask if you need any help or explanations!

"""
"""
#1. Create a list comprehension that generates the squares of the numbers from 1 to 10.

squares = [x**2 for x in range(0,11)]

print(squares)


# 2. Use a list comprehension to create a new list of the cubes of the numbers from 1 to 10, but only if the cube is evenly divisible by 4.

cubes = [x**3 for x in range(0,11) if x % 4 ==0]
print(cubes)

#3 Given the list `names = ['Nick', 'Alice', 'Kitty', 'Lionel', 'Daisy']`, create a list comprehension that generates a new list containing only the names that start with an 'L'.

names = ['Nick', 'Alice', 'Kitty', 'Lionel', 'Daisy']

new_names = [name for name in names if name.startswith('L')]

print(new_names)

#4 Use a list comprehension to create a list of all the years from 1900 to 2100 that are leap years. (Hint: a leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400)


leap_years = [year for year in range(1900, 2101) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
leap_years = [year for year in range(1900, 2101) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

print(leap_years)

"""



"""
Second set of exercises

1. **Odd Numbers**: Create a list comprehension that generates a list of all odd numbers from 1 to 50.

2. **Multiples of Five**: Use a list comprehension to create a list of all numbers between 1 and 100 that are divisible by 5.

3. **First Character**: Given the list `words = ['hello', 'world', 'my', 'name', 'is', 'Python']`, use a list comprehension to create a new list that contains the first character of each word.

4. **Length Condition**: Given the same list `words = ['hello', 'world', 'my', 'name', 'is', 'Python']`, create a list comprehension that generates a new list containing only the words that are more than 2 characters long.

These exercises should continue to strengthen your understanding and skills with list comprehensions. Let me know if you need help with any of them!

"""
"""
#1 **Odd Numbers**: Create a list comprehension that generates a list of all odd numbers from 1 to 50.

odd_numbers = [num for num in range(1,50) if num % 2 != 0]

print(odd_numbers)

#2  **Multiples of Five**: Use a list comprehension to create a list of all numbers between 1 and 100 that are divisible by 5.

five_divide = [num for num in range (1,101) if num % 5 == 0]

print(five_divide)

#3 **First Character**: Given the list `words = ['hello', 'world', 'my', 'name', 'is', 'Python']`, use a list comprehension to create a new list that contains the first character of each word.

words = ['hello', 'world', 'my', 'name', 'is', 'Python']

characters = [word[0] for word in words]

print(characters)

#4 **Length Condition**: Given the same list `words = ['hello', 'world', 'my', 'name', 'is', 'Python']`, create a list comprehension that generates a new list containing only the words that are more than 2 characters long.

words = ['hello', 'world', 'my', 'name', 'is', 'Python']

long_words = [word for word in words if len(word) > 2]

print(long_words)
"""
"""
1. **Nested List Comprehension**: Create a list comprehension within another list comprehension to generate the multiplication table from 1 to 10 (a list of lists).

2. **Complex Conditional**: Given the list `nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]`, create a list comprehension that generates a new list where negative numbers are replaced by 'negative' and positive numbers are replaced by 'positive'.

3. **Complex Data Types**: Given the list `users = [{'name': 'John', 'age': 15}, {'name': 'Jane', 'age': 25}, {'name': 'Doe', 'age': 35}]`, create a list comprehension that extracts all names from the dictionaries.

Remember that the goal is to understand and get comfortable with list comprehensions. There is no pressure to master them in one day. Keep practicing and experimenting, and you'll continue to improve!
"""
"""

#1 Nested List Comprehension**: Create a list comprehension within another list comprehension to generate the multiplication table from 1 to 10 (a list of lists).

mult_table = [[num for num in range(11)] for _ in range(11)]

print(mult_table)


#2 **Complex Conditional**: Given the list `nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]`, create a list comprehension that generates a new list where negative numbers are replaced by 'negative' and positive numbers are replaced by 'positive'.

nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

new_nums = ['negative' if x < 0 else 'positive' for x in nums]
print(new_nums)

#3 **Complex Data Types**: Given the list `users = [{'name': 'John', 'age': 15}, {'name': 'Jane', 'age': 25}, {'name': 'Doe', 'age': 35}]`, create a list comprehension that extracts all names from the dictionaries.

users = [{'name': 'John', 'age': 15}, {'name': 'Jane', 'age': 25}, {'name': 'Doe', 'age': 35}]

names = [user['name'] for user in users]

print(names)
"""
"""
Here are 10 more exercises that you can work on to practice list comprehensions:

1. **Square Numbers**: Create a list comprehension that generates a list of squares of all numbers from 1 to 20.

2. **Lowercase Words**: Given a list of words, use a list comprehension to convert all the words to lowercase.
 `words = ['HELLO', 'World', 'PYTHON', 'progRAMming']`

3. **Matrix Transpose**: Given a matrix (a list of lists), use a nested list comprehension to get its transpose.
`matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

4. **Vowel Filter**: Given a sentence (a string), create a list comprehension that generates a list of all vowels in the sentence.
`sentence = "The quick brown fox jumps over the lazy dog"`

5. **Unique Words**: Given a sentence (a string), create a list comprehension that generates a list of unique words in the sentence (ignore case for uniqueness, but return the words in their original case).
`sentence = "List comprehensions in Python are a concise way to create lists"`

6. **Word Lengths**: Given a list of words, create a list comprehension that generates a list of tuples, where each tuple is a word from the list and its corresponding length.
`words = ['list', 'comprehension', 'python', 'programming', 'concise', 'create']`

7. **Multiple Lists**: Given two lists of equal length, create a list comprehension that generates a list of tuples, where each tuple is a pair of corresponding elements from the two lists.
`list1 = [1, 2, 3, 4, 5], list2 = ['one', 'two', 'three', 'four', 'five']`

8. **Divisors**: For all numbers from 1 to 50, create a list comprehension that generates a list of tuples, where each tuple is a number and a list of its divisors.

9. **Word Classification**: Given a list of words, create a list comprehension that generates a list of tuples, where each tuple is a word from the list and a string 'short' or 'long' depending on whether the word is shorter or longer than 5 characters.
`words = ['Python', 'is', 'a', 'high-level', 'programming', 'language']`

10. **Enumeration**: Given a list, create a list comprehension that generates a list of tuples, where each tuple is an index and the corresponding element from the list.
`my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']`
"""


#1. **Square Numbers**: Create a list comprehension that generates a list of squares of all numbers from 1 to 20.

#2. **Lowercase Words**: Given a list of words, use a list comprehension to convert all the words to lowercase.
words = ['HELLO', 'World', 'PYTHON', 'progRAMming']
lowercase = [word.lower() for word in words]
print(lowercase)

#3. **Matrix Transpose**: Given a matrix (a list of lists), use a nested list comprehension to get its transpose.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_matrix = [num for sublist in matrix for num in sublist]
print(flat_matrix)

#4. **Vowel Filter**: Given a sentence (a string), create a list comprehension that generates a list of all vowels in the sentence.
sentence = "The quick brown fox jumps over the lazy dog"

vowels = [char for char in sentence if char in 'aeiouAEIOU']
print(vowels)

#5. **Unique Words**: Given a sentence (a string), create a list comprehension that generates a list of unique words in the sentence (ignore case for uniqueness, but return the words in their original case).
sentence = "List comprehensions in Python are a concise way to create lists"

seen = set()
result = []
for word in sentence.split():
    if word.lower() not in seen:
        result.append(word)
        seen.add(word.lower())

print(result)


#6. **Word Lengths**: Given a list of words, create a list comprehension that generates a list of tuples, where each tuple is a word from the list and its corresponding length.
words = ['list', 'comprehension', 'python', 'programming', 'concise', 'create']

word_length = [(i, word) for i, word in enumerate(words)]
print(word_length)

#7. **Multiple Lists**: Given two lists of equal length, create a list comprehension that generates a list of tuples, where each tuple is a pair of corresponding elements from the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']
list3 = [(num, word) for num, word in zip(list1, list2)]
print(list3)

#8. **Divisors**: For all numbers from 1 to 50, create a list comprehension that generates a list of tuples, where each tuple is a number and a list of its divisors.
tuples = [(num, [i for i in range(1, num+1) if num % i == 0]) for num in range(1, 51)]
print(tuples)


#9. **Word Classification**: Given a list of words, create a list comprehension that generates a list of tuples, where each tuple is a word from the list and a string 'short' or 'long' depending on whether the word is shorter or longer than 5 characters.
words = ['Python', 'is', 'a', 'high-level', 'programming', 'language']
tuples = [(word, 'short'if len(word)< 6 else 'long') for word in words ]
print(tuples)

#10. **Enumeration**: Given a list, create a list comprehension that generates a list of tuples, where each tuple is an index and the corresponding element from the list.
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

tuples = [(i, value) for i, value in enumerate(my_list)]

print(tuples)
