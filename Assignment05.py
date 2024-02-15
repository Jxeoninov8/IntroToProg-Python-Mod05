# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jeisson Guerrero Estrada,02/14/24, Finished project
# ------------------------------------------------------------------------------------------ #

# Library import json

import json

# Define the Data Constants

MENU: str = '''
------ Course Registration Program ------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants

FILE_NAME: str = 'Enrollments.json'  # Change to Json file

# Define the Data Variables and constants

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)

# Extract the data from the file

try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print('The file does not exist.\n')
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
    file = open(FILE_NAME, 'w')
    json.dump(students, file)
finally:
    if not file.close:
        file.close()

    # Present and Process the data

while True:

    # Present the menu of choices

    print(MENU)
    menu_choice = input('What would you like to do: ')

    # Input user data

    if menu_choice == '1':
        try:
            student_first_name = input('Enter the student\'s first name: ')
            if not student_first_name.isalpha():
                raise ValueError('Student first name can only contain alphanumeric characters')
            student_last_name = input('Enter the student\'s last name: ')
            if not student_last_name.isalpha():
                raise ValueError('Student last name can only contain alphanumeric characters')
            course_name = input('Please enter the name of the course: ')
            student_data = {"first_name": student_first_name, "last_name": student_last_name,
                            "course_name": course_name}  # Change list to a dictionary
            students.append(student_data)
            print('-' * 50)
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
            print('-' * 50)
        except ValueError as e:
            print('Unknown Error\n')
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data

    elif menu_choice == '2':

        # Process the data to create and display a custom message
        print('-' * 50)
        try:
            for student in students:
                print(f'{student["first_name"]},{student["last_name"]},{student["course_name"]}\n')
        except KeyError as e:
            print('Invalid data found\n')
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
            print('-' * 50)
            continue

    # Save the data to a file

    elif menu_choice == '3':
        try:
            print('-' * 50)
            file = open(FILE_NAME, 'w')
            json.dump(students, file)
            file.close()
            print('Data has been saved to file!')
            for student in students:
                print(f'{student["first_name"]},{student["last_name"]},{student["course_name"]}\n')
            print('-' * 50)
        except Exception as e:
            print('Unknown Error')
            print('---Technical Information---')
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Stop the loop

    elif menu_choice == '4':
        break
    else:
        print('Option invalid please  choose from options 1, 2, or 3')

print('Goodbye program will now end')
