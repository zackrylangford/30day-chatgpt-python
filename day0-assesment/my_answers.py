#My answers

"""
1. **Variables and Data Types**: Write a Python program to add two user-provided numbers.
"""

x = int(input("Please provide a number to add: "))
y = int(input("Please provide another number to add: "))
answer = (x + y)

print(f"Answer: {answer}")

"""
2. **Control Flow/Loops**: Write a Python program that prints all the numbers from 0 to n, where n is a user input.
"""

n = int(input("Please provide a number: "))
n +=1
for x in range (0,n):
    print(x)

"""
3. **Lists**: Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers.
"""


def even_numbers(nums):
    for x in nums:
        if x % 2 == 0:
            print(x)

nums = [1,2,3,4,5,6,7,8,9,10]
even_numbers(nums)

"""
4. **Dictionaries**: Given a dictionary, write a Python function that inverts the keys and values of the dictionary (i.e., keys become values and values become keys).
"""

dict = {'1':'a', '2':'b', '3':'c'}


"""
5. **Functions**: Write a Python function that checks whether a passed string is a palindrome or not.
"""

word = input("Please provide a word so I can check if it is a palindrome: ")

def palindrome_check(word):
    for x in word: 
        if [x:] == [:x]:
            print("True")
        else: 
            print("False")


"""
6. **File Handling**: Write a Python program to read a file line by line and store it into a list.
"""

def list_file(file):


"""
7. **Error Handling**: Write a Python function that takes two integers as input and returns their division. Your function should handle the case when the second integer is zero by printing an appropriate message.
"""

x = int(input("Please enter a number: "))
y = int(input("Please enter a second number: "))

if y == 0:
    print("Error, you cannot divide by zero")
else: 
    print(x/y)


"""
8. **Classes and Objects**: Define a Python class named Circle constructed by a radius and two methods that will compute the area and the perimeter of a circle.
"""

class Circle(self):
    radius = 5

    def area(self, radius):
        a = 3.14159 * (radius**2)
        print(a)
    def perimeter(self, radius):
        p = 2 * 3.14159 * radius
        print(p)


"""
9. **Decorators**: Explain what decorators are in Python and write a simple decorator function.
"""
"""
Decorators are methods that you can define and then reuse on functions throughout your code. For instance, in Django a "@login_required" decorator that is placed over a view function makes the function viewable only by those who are logged in. 

I don't know where to begin with writing one though :)
"""

"""
10. **Modules and Packages**: Write a Python script to import a module and use a function that you've defined in it.
"""
import random

list = [1,2,3,4,5,6]

print(randint(list))




