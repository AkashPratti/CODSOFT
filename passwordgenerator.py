import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(password_length.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Password length must be greater than zero.")
            return

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        characters = ''
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showwarning("Warning", "Invalid input! Please enter a valid password length.")

def clear_password():
    result_label.config(text="")
    password_entry.delete(0, tk.END)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input fields and labels
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

password_length = tk.StringVar()
entry_length = tk.Entry(root, textvariable=password_length)
entry_length.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Checkbuttons for character types
upper_var = tk.BooleanVar()
upper_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

lower_var = tk.BooleanVar()
lower_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_checkbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Password entry
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=7, column=0, padx=10, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_password)
clear_button.grid(row=7, column=1, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()

