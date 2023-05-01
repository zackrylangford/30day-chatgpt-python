"""
**Exercises**

1. Create a list comprehension that generates the squares of the numbers from 1 to 10.
2. Use a list comprehension to create a new list of the cubes of the numbers from 1 to 10, but only if the cube is evenly divisible by 4.
3. Given the list `names = ['Nick', 'Alice', 'Kitty', 'Lionel', 'Daisy']`, create a list comprehension that generates a new list containing only the names that start with an 'L'.
4. Use a list comprehension to create a list of all the years from 1900 to 2100 that are leap years. (Hint: a leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400).

These exercises should give you a good sense of how list comprehensions work. Feel free to ask if you need any help or explanations!

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