import json

# function to add new student to the list


def add_student(new_student):
    # read existing data
    with open('students.json', 'r') as f:
        students = json.load(f)

    # add new student
    students.append(new_student)

    # write updated data back to the file
    with open('students.json', 'w') as f:
        json.dump(students, f)

# function to update an existing student in the list


def update_student(name, updated_info):
    # read existing data
    with open('students.json', 'r') as f:
        students = json.load(f)

    # find the student with the matching name
    for student in students:
        if student['name'] == name:
            # update student's info
            student.update(updated_info)
            break

    # write updated data back to the file
    with open('students.json', 'w') as f:
        json.dump(students, f)

# function to remove a student from the list


def remove_student(name):
    # read existing data
    with open('students.json', 'r') as f:
        students = json.load(f)

    # find the student with the matching name
    for student in students:
        if student['name'] == name:
            # remove the student from the list
            students.remove(student)
            break

    # write updated data back to the file
    with open('students.json', 'w') as f:
        json.dump(students, f)

# function to get user input


def get_input():
    print("What would you like to do?")
    print("1. Add a student")
    print("2. Update a student")
    print("3. Remove a student")
    action = input("Enter the number of your choice: ")

    if action == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        new_student = {"name": name, "age": age}
        add_student(new_student)
    elif action == '2':
        name = input("Enter student name to update: ")
        age = int(input("Enter updated student age: "))
        updated_info = {"age": age}
        update_student(name, updated_info)
    elif action == '3':
        name = input("Enter student name to remove: ")
        remove_student(name)
    else:
        print("Invalid action.")


# get user input and perform selected action
get_input()
