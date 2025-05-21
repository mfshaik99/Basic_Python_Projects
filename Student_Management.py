students = {}

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students[name] = grade
    print(f"{name} added with grade {grade}.\n")

def view_students():
    if not students:
        print("No student data available.\n")
    else:
        for name, grade in students.items():
            print(f"{name}: {grade}")
        print()

def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        new_grade = float(input("Enter new grade: "))
        students[name] = new_grade
        print(f"{name}'s grade updated to {new_grade}.\n")
    else:
        print("Student not found.\n")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"{name} deleted.\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Grade")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_grade()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.\n")

# Start the system
menu()
