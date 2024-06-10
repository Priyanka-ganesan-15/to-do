import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 14))
        self.style.configure('TLabel', font=('Arial', 12))

        # Create frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(padx=10, pady=5)

        # Create widgets
        self.task_entry = ttk.Entry(self.input_frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.priority_var = tk.StringVar(value="Medium")
        self.priority_label = ttk.Label(self.input_frame, text="Priority:")
        self.priority_label.grid(row=0, column=1, padx=5)
        self.priority_combobox = ttk.Combobox(self.input_frame, textvariable=self.priority_var,
                                              values=["High", "Medium", "Low"], width=10)
        self.priority_combobox.grid(row=0, column=2, padx=5)

        self.due_date_var = tk.StringVar(value="")
        self.due_date_label = ttk.Label(self.input_frame, text="Due Date:")
        self.due_date_label.grid(row=0, column=3, padx=5)
        self.due_date_entry = ttk.Entry(self.input_frame, textvariable=self.due_date_var, width=15)
        self.due_date_entry.grid(row=0, column=4, padx=5)

        self.add_button = ttk.Button(self.input_frame, text="Add Task", width=10, command=self.add_task)
        self.add_button.grid(row=0, column=5, padx=5)

        self.task_listbox = tk.Listbox(self.list_frame, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.delete_button = ttk.Button(self.root, text="Delete Task", width=10, command=self.delete_task)
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_var.get()

        if task:
            task_display = f"{task} - Priority: {priority}"
            if due_date:
                try:
                    due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
                    task_display += f", Due Date: {due_date_obj.strftime('%b %d, %Y')}"
                except ValueError:
                    messagebox.showwarning("Warning", "Invalid due date format. Please use YYYY-MM-DD.")
                    return

            self.tasks.append((task_display, task, priority, due_date))
            self.task_listbox.insert(tk.END, task_display)

            # Clear entry fields
            self.task_entry.delete(0, tk.END)
            self.priority_var.set("Medium")
            self.due_date_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
