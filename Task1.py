import tkinter as tk
from tkinter import messagebox, font

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", f"'{task}' has been added to your list!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        messagebox.showinfo("Task Deleted", f"'{task}' has been removed from your list.")
    except IndexError:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

# Function to update the selected task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            old_task = task_listbox.get(selected_task_index)
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Updated", f"'{old_task}' has been updated to '{new_task}'")
        else:
            messagebox.showwarning("Input Error", "Please enter a task to update.")
    except IndexError:
        messagebox.showwarning("Update Error", "Please select a task to update.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)
    messagebox.showinfo("Tasks Cleared", "All tasks have been cleared.")

# Function to change button color on hover
def on_enter(e, button, color):
    button['background'] = color

def on_leave(e, button, color):
    button['background'] = color

# Create main window
root = tk.Tk()
root.title("Interactive To-Do List")
root.geometry("400x500")  # Set window size
root.config(bg="#F7F7F7")  # Set background color to light gray

# Custom font
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Title label with light background
title_label = tk.Label(root, text="My To-Do List", bg="#4A90E2", fg="white", font=("Arial", 18, "bold"), pady=10)
title_label.pack(fill=tk.X)

# Frame for task entry and buttons
entry_frame = tk.Frame(root, bg="#F7F7F7")
entry_frame.pack(pady=10)

# Create the input field for task entry
task_entry = tk.Entry(entry_frame, width=30, font=("Arial", 12), bg="white", fg="black", relief="flat", highlightbackground="#4A90E2", highlightthickness=1)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Create Add button with hover effect
add_button = tk.Button(entry_frame, text="Add Task", bg="#4A90E2", fg="white", font=custom_font, width=10, relief="flat", bd=0)
add_button.grid(row=0, column=1, padx=5, pady=10)
add_button.config(command=add_task)

# Create a listbox with a modern design
listbox_frame = tk.Frame(root, bg="#F7F7F7")
listbox_frame.pack(pady=10)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
task_listbox = tk.Listbox(listbox_frame, height=8, width=40, font=("Arial", 12), bg="white", fg="black", relief="flat", yscrollcommand=scrollbar.set, selectbackground="#B3E5FC", selectmode=tk.SINGLE)
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Add padding and shadow to the listbox
task_listbox.config(highlightthickness=1, highlightbackground="#4A90E2", bd=2)

# Frame for action buttons
button_frame = tk.Frame(root, bg="#F7F7F7")
button_frame.pack(pady=10)

# Action buttons
delete_button = tk.Button(button_frame, text="Delete Task", bg="#F44336", fg="white", font=custom_font, width=10, relief="flat", bd=0)
delete_button.grid(row=0, column=0, padx=5, pady=5)
delete_button.config(command=delete_task)

update_button = tk.Button(button_frame, text="Update Task", bg="#FFC107", fg="black", font=custom_font, width=10, relief="flat", bd=0)
update_button.grid(row=0, column=1, padx=5, pady=5)
update_button.config(command=update_task)

clear_button = tk.Button(button_frame, text="Clear All", bg="#4A90E2", fg="white", font=custom_font, width=10, relief="flat", bd=0)
clear_button.grid(row=0, column=2, padx=5, pady=5)
clear_button.config(command=clear_tasks)

# Add hover effects to buttons
add_button.bind("<Enter>", lambda e: on_enter(e, add_button, "#1E88E5"))
add_button.bind("<Leave>", lambda e: on_leave(e, add_button, "#4A90E2"))

delete_button.bind("<Enter>", lambda e: on_enter(e, delete_button, "#E53935"))
delete_button.bind("<Leave>", lambda e: on_leave(e, delete_button, "#F44336"))

update_button.bind("<Enter>", lambda e: on_enter(e, update_button, "#FFB300"))
update_button.bind("<Leave>", lambda e: on_leave(e, update_button, "#FFC107"))

clear_button.bind("<Enter>", lambda e: on_enter(e, clear_button, "#1E88E5"))
clear_button.bind("<Leave>", lambda e: on_leave(e, clear_button, "#4A90E2"))

# Start the GUI event loop
root.mainloop()
