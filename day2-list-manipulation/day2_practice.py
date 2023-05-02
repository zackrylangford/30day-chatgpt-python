"""
I spent a little time reviewing day1 with the following exercises: 

1. **Square numbers**: Create a list comprehension that generates a list of squares of the numbers from 1 to 10.

2. **Positive and Negative**: Given a list of numbers, create a list comprehension that generates a new list containing the same numbers, but with their signs flipped (positive numbers become negative, and negative numbers become positive).

3. **Lowercase words**: Given a list of words, create a list comprehension that generates a new list containing the same words but in lowercase.

4. **Even indexes**: Given a list of any elements, create a list comprehension that generates a new list containing only the elements with even indexes.

5. **Divisible by 3 and 5**: Create a list comprehension that generates a list of all numbers between 1 and 100 that are divisible by both 3 and 5.

6. **Length filter**: Given a list of strings and an integer `n`, create a list comprehension that generates a new list containing only the strings that have a length greater than `n`.

7. **Common elements**: Given two lists, create a list comprehension that generates a new list containing the elements that appear in both input lists.

Try working through these exercises, and let me know if you need help with any of them!

"""
## Day 1 Review
#1 

squares = [x**2 for x in range(11)]
print(squares)

#2
numbers = [1,2,3,-4,-5]
flipped = [-n for n in numbers]
print(flipped)

#3
words = ['HELLO', 'World', 'PYTHON', 'progRAMming']
lower = [word.lower() for word in words]
print(lower)

#4
given_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit']
evens = [fruit for i, fruit in enumerate(given_list) if i % 2 == 0]
print(evens)

#5
nums = [num for num in range(101) if num % 3 == 0 and num % 5 == 0]
print(nums)

#6
string_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit']
n = 5

new_list = [string for string in string_list if len(string) > n]

print(new_list)

#7
list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit']
list2 = ['banana', 'date', 'lemon', 'grape', 'orange', 'jackfruit', 'kiwi', 'lime', 'mango', 'nectarine']

new_list = [fruit for fruit in list1 if fruit in list2]

print(new_list)


#Day 2 Exercises

"""




"""

