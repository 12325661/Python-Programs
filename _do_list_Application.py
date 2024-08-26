# To do List Application
tasks = []

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print("Task added")

def view_task():
    if tasks:
        index = 0
        for task in tasks:
            print(f"{index}: {task}")
            index += 1
    else:
        print("No task is present in the list.")

def delete_task():
    view_task()
    task_number = input("Enter the task number you want to delete: ")
    if task_number.isdigit():
        task_number = int(task_number)
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"'{removed_task}' has been deleted")
        else:
            print("Task number is out of range")
    else:
        print("Invalid input. Please enter a valid number")

def update_task():
    view_task()
    task_number = input("Enter the task number you want to update: ")

    if task_number.isdigit():
        task_number = int(task_number)
        if 0 <= task_number < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number] = new_task
            print("Task updated.")
        else:
            print("Task number is out of range")
    else:
        print("Invalid input. Please enter a valid number")

def main():
    while True:
        choice = input("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Update Task\n5. Quit\nChoose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__== "__main__":
    main()
