# **Exercises**:

1. **Average Age**: Given a list of dictionaries representing students with their names, ages, and grades, calculate the average age of the students.

2. **Grade Distribution**: Given a list of dictionaries representing students with their names, ages, and grades, create a dictionary with grades as keys and lists of student names as values.

3. **Filter by Grade**: Given a list of dictionaries representing students with their names, ages, and grades, create a new list of dictionaries containing only the students who have a specific grade.

4. **Update Inventory**: Given a list of sold items (each represented by a dictionary with a product name and quantity) and an inventory dictionary with product names as keys and quantities as values, update the inventory to reflect the sold items.

5. **Nested Dictionary to List**: Given a nested dictionary representing students and their courses, extract all the courses into a single list without duplicates.

Feel free to ask for clarification, examples, or help with the exercises. Good luck with your study session!

## In depth explanation for number 2:

Of course! Let's break it down step by step:

1. **Initialize an empty dictionary**:
   Here we're creating a new dictionary which will store our result. We'll add entries to this dictionary as we iterate through the list of students.

   ```python
   new_dict = {}
   ```

2. **Iterate over the list of students**:
   We want to look at each student in the list one by one. We do this by using a for loop. The variable `student` will represent the current student as we iterate through the list.

   ```python
   for student in students:
   ```

3. **Check if the student's grade is already a key in the dictionary**:
   For each student, we look at their grade and check if it's already a key in our dictionary. We do this using the `in` keyword, which checks if a value is in a list or a key is in a dictionary.

   ```python
   if student['grade'] in new_dict:
   ```

4. **If the grade is already a key, append the student's name to the list for that grade**:
   If the grade is already a key in our dictionary, we know that there's already at least one student with that grade. We want to add the current student to the list of students with that grade, so we use the `append` method to add the student's name to the list.

   ```python
   new_dict[student['grade']].append(student['name'])
   ```

5. **If the grade is not a key in the dictionary, add a new entry with the grade as the key and a list containing the student's name as the value**:
   If the grade is not already a key in our dictionary, this is the first student we've seen with that grade. We add a new entry to the dictionary with the grade as the key and a list containing the student's name as the value.

   ```python
   else:
       new_dict[student['grade']] = [student['name']]
   ```

6. **Print the dictionary**:
   After we've iterated through all the students, our dictionary is complete and we can print it to see the result.

   ```python
   print(new_dict)
   ```

This process, where we're creating a new dictionary based on a list of dictionaries, is a common pattern when you're working with data in Python. Once you understand the steps, you can adapt this pattern for many different tasks.