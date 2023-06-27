tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def complete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task completed!")
    else:
        print("Task not found!")

def display_tasks():
    print("Tasks:")
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print("- " + task)

while True:
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Display Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to mark as complete: ")
        complete_task(task)
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")