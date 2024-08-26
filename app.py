import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_number = 1

        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(background="#f0f0f0")

        self.header_frame = tk.Frame(self.root, bg="#333", height=50)
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="To-Do List", font=("Arial", 20), fg="white", bg="#333")
        self.header_label.pack(pady=10)

        self.task_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.task_frame.pack(fill="both", expand=True)

        self.task_label = tk.Label(self.task_frame, text="Task:", font=("Arial", 15), fg="#333", bg="#f0f0f0")
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(self.task_frame, width=30, font=("Arial", 15), fg="#333", bg="#f0f0f0")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.task_frame, text="Add task", font=("Arial", 15), fg="white", bg="#007bff", command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_listbox_frame = tk.Frame(self.task_frame, bg="#f0f0f0")
        self.task_listbox_frame.pack(fill="both", expand=True)

        self.task_listbox = tk.Listbox(self.task_listbox_frame, width=30, font=("Arial", 15), fg="#333", bg="#f0f0f0")
        self.task_listbox.pack(side="left", fill="both", expand=True)

        self.task_scrollbar = tk.Scrollbar(self.task_listbox_frame)
        self.task_scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.config(command=self.task_listbox.yview)

        self.delete_button = tk.Button(self.task_frame, text="Delete task", font=("Arial", 15), fg="white", bg="#dc3545", command=self.delete_task)
        self.delete_button.pack(pady=10)

        self.update_button = tk.Button(self.task_frame, text="Update task", font=("Arial", 15), fg="white", bg="#28a745", command=self.update_task)
        self.update_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(self.task_number, task)
            self.task_number += 1
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showerror("Error", "Please select a task to delete.")

    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task = self.task_entry.get()
            if task:
                self.tasks[task_index] = task
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a task to update.")
        except:
            messagebox.showerror("Error", "Please select a task to update.")


def main():
    root = tk.Tk()
    todo = ToDoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()