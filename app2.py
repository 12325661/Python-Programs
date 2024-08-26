# to_do_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "pending", "reminder": None})
        print(f"Task '{task}' added!")

    def view_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['task']} - {task['status']}")

    def update_task(self, task_id, new_task):
        if task_id > 0 and task_id <= len(self.tasks):
            self.tasks[task_id - 1]["task"] = new_task
            print(f"Task {task_id} updated to '{new_task}'")
        else:
            print("Invalid task ID")

    def track_task(self, task_id):
        if task_id > 0 and task_id <= len(self.tasks):
            task = self.tasks[task_id - 1]
            if task["status"] == "pending":
                task["status"] = "in_progress"
                print(f"Task {task_id} marked as in progress")
            elif task["status"] == "in_progress":
                task["status"] = "completed"
                print(f"Task {task_id} marked as completed")
            else:
                print("Task is already completed")
        else:
            print("Invalid task ID")

    def set_reminder(self, task_id, reminder):
        if task_id > 0 and task_id <= len(self.tasks):
            self.tasks[task_id - 1]["reminder"] = reminder
            print(f"Reminder set for task {task_id} to {reminder}")
        else:
            print("Invalid task ID")

    def delete_task(self, task_id):
        if task_id > 0 and task_id <= len(self.tasks):
            del self.tasks[task_id - 1]
            print(f"Task {task_id} deleted")
        else:
            print("Invalid task ID")

    def invalid_task(self, task_id):
        if task_id > 0 and task_id <= len(self.tasks):
            self.tasks[task_id - 1]["status"] = "invalid"
            print(f"Task {task_id} marked as invalid")
        else:
            print("Invalid task ID")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Track task")
        print("5. Set reminder")
        print("6. Delete task")
        print("7. Mark task as invalid")
        print("8. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter the task ID to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_id, new_task)
        elif choice == "4":
            task_id = int(input("Enter the task ID to track: "))
            todo_list.track_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter the task ID to set a reminder for: "))
            reminder = input("Enter the reminder: ")
            todo_list.set_reminder(task_id, reminder)
        elif choice == "6":
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "7":
            task_id = int(input("Enter the task ID to mark as invalid: "))
            todo_list.invalid_task(task_id)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()