
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
       
    else:
        
        print("\nYour Tasks:")
        i = 1
        for task in tasks:
            print(str(i) + ". " + task)
            i += 1


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!")


def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed:", removed)
        else:
            print("Invalid number!")
    
    except:
        print("Invalid input!")


def main():
   
    tasks = ["Study Python","Practice Coding","Do Homework"]
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            add_task(tasks)

        elif choice == '3':
            remove_task(tasks)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

main()

