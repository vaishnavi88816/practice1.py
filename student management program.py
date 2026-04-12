# Simple Student Management System (Single File)

students = []

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students.append([roll, name, marks])
        print(" Student added successfully!")

    # View students
    elif choice == "2":
        if len(students) == 0:
            print(" No students found.")
        else:
            print("\n--- Student List ---")
            for s in students:
                print("Roll:", s[0], "| Name:", s[1], "| Marks:", s[2])

    # Search student
    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        found = False

        for s in students:
            if s[0] == roll:
                print(" Found Student:")
                print("Name:", s[1], "| Marks:", s[2])
                found = True
                break

        if not found:
            print(" Student not found")

    # Delete student
    elif choice == "4":
        roll = input("Enter Roll Number to delete: ")
        found = False

        for s in students:
            if s[0] == roll:
                students.remove(s)
                print(" Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")