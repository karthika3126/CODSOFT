import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"title": task, "completed": False})
        entry.delete(0, tk.END)
        refresh_tasks()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        refresh_tasks()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Toggle task completion
def toggle_complete(event=None):
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["completed"] = not tasks[selected]["completed"]
        refresh_tasks()
        save_tasks()
    except IndexError:
        pass

# Refresh the listbox
def refresh_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        listbox.insert(tk.END, f"[{status}] {task['title']}")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

tasks = load_tasks()

# Entry + Buttons
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Task List
listbox = tk.Listbox(root, width=60)
listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
listbox.bind("<Double-Button-1>", toggle_complete)

refresh_tasks()

# Run the app
root.mainloop()
