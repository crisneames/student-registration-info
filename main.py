data = {
    10001:
    {
        'first_name': 'Chris',
        'last_name': 'Herzog',
        'email': 'chriher22@aol.com',
        'classes_taken': ('CSC126', 'CSC211', 'CSC326'),
        'grades_received': ('A', 'C', 'F'),
        'type': 'student'
    },
    10002:
    {
        'first_name': 'Joseph',
        'last_name': 'Smith',
        'email': 'JosephSSmith@rhyta.com',
        'classes_taken': ('CSC456', 'CSC121', 'ENG151'),
        'grades_received': ('A', 'C', 'A'),
        'type': 'student'
    },
    10003:
    {
        'first_name': 'Kelli',
        'last_name': 'Marshall',
        'email': 'JosephSSmith@rhyta.com',
        'classes_taken': ('CSC456', 'CSC121', 'ENG120', 'ENG121', 'ENG151', 'ENG230'),
        'grades_received': ('A', 'A', 'A', 'A', 'A', 'A'),
        'type': 'student'
    },
    10004:
    {
        'first_name': 'Manuel',
        'last_name': 'Horn',
        'email': 'ManuelCHorn@dayrep.com',
        'classes_taken': ('CSC456', 'CSC121'),
        'grades_received': ('A', 'C'),
        'type': 'student'
    },
    10005:
    {
        'first_name': 'Kevin',
        'last_name': 'Lacour',
        'email': 'KevinBLacour@teleworm.us',
        'classes_taken': ('CSC211', 'CSC220'),
        'grades_received': ('F', 'F'),
        'type': 'student'
    },
    10006:
    {
        'first_name': 'Suresh',
        'last_name': 'Sigera',
        'email': 'sureshsigera@ms.edu',
        'password': 'J&hqweh12e7d2n281',
        'type': 'staff'
    },
    10007:
    {
        'first_name': 'Ann',
        'last_name': 'Chatman',
        'email': 'AnnBChatman@ms.edu',
        'password': 'J&hqweh12e7d2n28qq1',
        'type': 'staff'
    },
}


def admin_login():
    """
    validate administrator (staff) login credentials
    if the login is successful, show the menu to access the following functionality:
    add_new_student, list_all_students, search_students, remove_student and display_single_record
    """
    user_id = input("Please enter the admin id: ")
    print()
    user_password = input("Please enter the admin password: ")
    record = None
    if data.get(int(user_id)):
        record = data.get(int(user_id))
        if record['type'] == 'staff' and record['password'] == user_password:
            admin_first_name = record['first_name']
            admin_last_name = record['last_name']
            print(f'Welcome {admin_first_name} {admin_last_name}')
            menu()
        else:
            print('student cannot access this system.')
            print("Please try again")
            admin_login()

    else:
        print("no id found")


def menu():
    print()
    run = True
    while run:
        choice = input(
            "A: add new student B: list all students C: search students D: remove student E: display single record Q: Logout Please enter your choice: ")
        if choice == "A" or choice == "a":
            add_new_student()
        elif choice == "B" or choice == "b":
            list_all_students()
        elif choice == "C" or choice == "c":
            search_students_()
        elif choice == "D" or choice == "d":
            remove_student()
        elif choice == "E" or choice == "e":
            display_single_record()
        elif choice == "Q" or choice == "q":
            print("Goodbye!")
            run = False
        elif choice != "":
            print("\n Not a Valid Choice. Try Again.")


def add_new_student():
    """
    add new student record to the data dictionary
        menu['1'] = "add new student"
    """
    key = 10007
    new_key = key + 1

    data[new_key] = {
        'first_name': input("student first name: "),
        'last_name': input('student last name: '),
        'email': input('student email address: '),
        'classes': input('student classes taken').split(","),
        'grades_received': input('student grades').split(","),
        'type': 'student'
    }
    print(data[new_key])
    print("new student added")
    print("Student Id:", new_key)


def list_all_students():
    """
    list all the student records from the data dictionary
    for each student, show the following:
    first_name, last_name, email, classes_taken, grades_received and the gpa
    """
    grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    for key, value in data.items():
        print(key, '--')
        # Again iterate over the nested dictionary
        for k, v in value.items():
            # if k == "type":
            # 	del data["type"]
            print(k, ' : ', v)
            if k == "grades_received":
                total = 0
                for grade in v:
                    total += grades[grade]
                print("gpa", ' : ', total / len(v))


def search_students_():
    """
    search student records by student id or by email address and print the first and last name
    """
    email = input("Student Email or Student Id: ")
    result = None
    if not email.isnumeric():
        for key in data:
            if data[key]["email"] == email:
                result = data[key]
        if result:
            print(result)
        else:
            print("No matching email")
    else:
        if int(email) in data:
            print(data[int(email)])


def remove_student():
    """
    remove a student record from the data dictionary
    """
    del_record = input("Enter ID of record to delete: ")
    del(data[int(del_record)])
    print("Student record deleted.")


def display_single_record():
    """
    display a single student record by ID
    show the following:
    first name, last name, email, classes_taken, grades_received and the gpa
    """
    grades = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    id = int(input("Student Id: "))
    # .get will return None if the key is not found
    student = data.get(id)
    if student:
        for key, value in student.items():
            print(key, " : ", value)
            if key == "grades_received":
                total = 0
                for grade in value:
                    total += grades[grade]
                print("gpa", ' : ', total / len(value))
    else:
        print("No matching id")


def main():
    """

    """
    admin_login()
    # add_new_student()
    # list_all_students()
    # search_students_()
    # display_single_record()


# the driver code
if __name__ == '__main__':
    main()
