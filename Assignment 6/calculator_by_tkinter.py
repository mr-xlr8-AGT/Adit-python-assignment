import tkinter as tk

def create_calculator():
    def button_click(item):
        current_text = input_text.get()
        
        if current_text == "0" and item != ".":
            input_text.set(item)
        else:
            input_text.set(current_text + str(item))

    def button_clear():
        input_text.set("0")

    def button_equal():
        try:
            expression = input_text.get()
            expression = expression.replace("×", "*").replace("÷", "/")
            
            result = str(eval(expression))
            
            if result.endswith(".0"):
                result = result[:-2]
                
            input_text.set(result)
        except Exception:
            input_text.set("Error")

    def button_backspace():
        current_text = input_text.get()
        if len(current_text) > 1:
            input_text.set(current_text[:-1])
        else:
            input_text.set("0")

    root = tk.Tk()
    root.title("Tkinter Calculator")
    root.geometry("300x400")
    root.resizable(0, 0)

    input_text = tk.StringVar(value="0") 

    input_field = tk.Entry(
        root, 
        textvariable=input_text, 
        font=('Arial', 24, 'bold'), 
        bd=10, 
        relief=tk.SUNKEN, 
        justify='right'
    )
    input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

    buttons = [
        ('C', 1, 0, 1, 'red'), ('⌫', 1, 1, 1, 'grey'), ('÷', 1, 2, 1, 'orange'), ('×', 1, 3, 1, 'orange'),
        ('7', 2, 0, 1, 'lightgrey'), ('8', 2, 1, 1, 'lightgrey'), ('9', 2, 2, 1, 'lightgrey'), ('-', 2, 3, 1, 'orange'),
        ('4', 3, 0, 1, 'lightgrey'), ('5', 3, 1, 1, 'lightgrey'), ('6', 3, 2, 1, 'lightgrey'), ('+', 3, 3, 1, 'orange'),
        ('1', 4, 0, 1, 'lightgrey'), ('2', 4, 1, 1, 'lightgrey'), ('3', 4, 2, 1, 'lightgrey'),
        ('0', 5, 0, 2, 'lightgrey'), ('.', 5, 2, 1, 'lightgrey'), ('=', 4, 3, 2, 'green')
    ]
    
    for i in range(1, 6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    row_val = 1
    col_val = 0
    for (text, row, col, span, color) in buttons:
        
        if text == 'C':
            command = button_clear
        elif text == '⌫':
            command = button_backspace
        elif text == '=':
            command = button_equal
        else:
            command = lambda t=text: button_click(t)

        tk.Button(
            root, 
            text=text, 
            padx=10, 
            pady=10, 
            font=('Arial', 18),
            bg=color,
            fg='black' if color not in ['orange', 'green'] else 'white',
            command=command
        ).grid(row=row, column=col, columnspan=span, sticky="nsew")
        
    root.mainloop()

if __name__ == '__main__':
    create_calculator()