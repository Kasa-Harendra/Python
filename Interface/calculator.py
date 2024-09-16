import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display the current expression and result
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 14), justify='right', bd=10)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                       command=lambda value=text: on_button_click(value) if value != '=' else calculate_result() if value != 'C' else clear_entry())
    button.grid(row=row, column=col)

# Run the application
window.mainloop()
