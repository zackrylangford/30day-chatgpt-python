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
"""

#Day 2 Exercises

"""
Here are some exercises to help you practice:

1. **Nested List Comprehension**: Given a matrix (a list of lists) of numbers, create a list comprehension that flattens the matrix into a single list.

2. **List Comprehension with Conditional Logic**: Given a list of numbers, create a list comprehension that generates a new list that contains "Positive", "Negative" or "Zero" based on each number in the original list.

3. **List Slicing**: Given a list of numbers, create a new list that contains only the last 3 elements of the original list.

4. **List Operations**: Given a list of numbers, write a Python program that inserts a new number at the second position in the list and removes the last element from the list. 

Remember to spend time understanding each concept and task before moving on to the next one. You're doing great! Keep up the good work.

"""
#1 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [num for sublist in matrix for num in sublist]

print(flat_list)

#2 
numbers = [0, -1, 2, -3, 4, -5, 6, 7, -8, 9]
description = ['Positive' if x > 0 else 'Negative' if x < 0 else 'Zero' for x in numbers]

print(description)

#3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last_three = [x for x in numbers[-3:]]
print(last_three)
#4
numbers = [10, 20, 30, 40, 50]
numbers.insert(1,4)
numbers.pop()
print(numbers)

"""
More exercises for day2

1. **Sorting Lists**:
   - Given the list `numbers = [5, 1, 9, 3, 7, 6, 8, 2, 4, 0]`, sort this list in ascending order.
   - Now, sort the same list in descending order.
   - Given a list of strings `fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']`, sort this list alphabetically.

2. **List Comprehensions with Nested Loops**:
   - Given two lists, `list1 = [1, 2, 3]` and `list2 = [10, 20, 30]`, use a nested list comprehension to create a new list that multiplies each element of `list1` with each element of `list2`.
   - Create a list comprehension that generates all combinations of numbers between 1 and 5 where the first number is less than the second number.

3. **Advanced List Slicing**:
   - Given the list `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, use slicing to get every second number, starting from 0.
   - Now, use slicing to get every second number in reverse order, starting from 10 and going down to 0.

4. **Using Lists as Stacks and Queues**:
   - Create a list and use it as a stack. Push `1, 2, 3, 4, 5` onto the stack, then pop three elements off the stack and print the result.
   - Create a list and use it as a queue. Enqueue `1, 2, 3, 4, 5` onto the queue, then dequeue three elements off the queue and print the result.

Work through these exercises, and let me know if you have any questions!

"""

#1
numbers = [5, 1, 9, 3, 7, 6, 8, 2, 4, 0]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)


favorite_meals = ['beef stew', 'tacos', 'apple crisp', 'pasta', 'beans and rice', 'pork chops', 'steak']

print(favorite_meals)
favorite_meals.sort()
print(favorite_meals)
favorite_meals.sort(reverse=True)
print(favorite_meals)
