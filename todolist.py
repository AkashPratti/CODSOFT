import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

# Function to add a task to the listbox
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the listbox
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to toggle the completion status of a selected task
def toggle_task():
    try:
        index = listbox.curselection()
        task_text = listbox.get(index)
        if task_text.startswith("✓ "):
            task_text = task_text[2:]
        else:
            task_text = "✓ " + task_text
        listbox.delete(index)
        listbox.insert(index, task_text)
    except:
        messagebox.showwarning("Warning", "Please select the task you've done.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.configure(bg="#ADD8E6")  # Light blue background

# Create an entry widget to add tasks
entry = tk.Entry(window, width=50, bg="#FFFFFF")  # White background
entry.pack(padx=10, pady=5, side=tk.TOP)

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="#F08080")  # Light coral background
button_frame.pack(padx=10, pady=5)

# Define the font for the buttons
button_font = Font(family="Arial", size=12, weight="bold")

# Create an "Add Task" button
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=button_font, bg="#90EE90", fg="#006400")  # Light green background, dark green text
add_button.pack(side=tk.LEFT, padx=5)

# Create a "Delete Task" button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=button_font, bg="#90EE90", fg="#006400")  # Light green background, dark green text
delete_button.pack(side=tk.LEFT, padx=5)

# Create a "Done Task" button
toggle_button = tk.Button(button_frame, text="Done Task", command=toggle_task, font=button_font, bg="#90EE90", fg="#006400")  # Light green background, dark green text
toggle_button.pack(side=tk.LEFT, padx=5)

# Create a listbox to display tasks
listbox = tk.Listbox(window, width=50, bg="#FFFFE0")  # Light yellow background
listbox.pack(padx=10, pady=5)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window, bg="#D3D3D3")  # Light gray background
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
window.mainloop()