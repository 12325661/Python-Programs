tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def list_tasks():
    if tasks:
        index = 0
        for task in tasks:
            print(f"{index}: {task}")
            index += 1
    else:
        print("No tasks.")

def delete_task():
    list_tasks()
    task_number = input("Enter the task number to delete: ")
    
    if task_number.isdigit():
        task_number = int(task_number)
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"'{removed_task}' has been deleted.")
        else:
            print("Task number is out of range.")
    else:
        print("Invalid input. Please enter a valid number.")

def update_task():
    list_tasks()
    task_number = input("Enter the task number to update: ")
    
    if task_number.isdigit():
        task_number = int(task_number)
        if 0 <= task_number < len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_number] = new_task
            print("Task updated.")
        else:
            print("Task number is out of range.")
    else:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        choice = input("\n1. Add Task\n2. Delete Task\n3. List Tasks\n4. Update Task\n5. Quit\nChoose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            update_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "main":
    main()