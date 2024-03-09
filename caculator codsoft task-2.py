import tkinter as tk
from tkinter import messagebox

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero!")
            return
        result = num1 / num2

    label_result.config(text="Result: " + str(result))
    big_display.config(text=str(result))

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create input widgets
label_num1 = tk.Label(root, text="First Number:")
label_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(root, text="Second Number:")
label_num2.grid(row=1, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation dropdown
operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value

label_operation = tk.Label(root, text="Operation:")
label_operation.grid(row=2, column=0, padx=5, pady=5)

operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

# Result label
label_result = tk.Label(root, text="")
label_result.grid(row=4, columnspan=2, padx=5, pady=5)

# Big display label
big_display = tk.Label(root, text="", font=("Helvetica", 24))
big_display.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()
