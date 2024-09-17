import tkinter as tk 

def  update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear_display():
    display.delete(0, tk.END)

window = tk.Tk()
window.title("Calculadora")

display = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), 
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: update_display(t))
    button.grid(row=row, column=col)

# CLEAR BUTTON

clear_button = tk.Button(window, text='C', width=5, height=2, font=("Arial", 18), command=clear_display)
clear_button.grid(row=5, column=0)


window.mainloop()