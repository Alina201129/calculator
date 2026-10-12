import tkinter as tk
import operations as calc  

window = tk.Tk()
window.title("Калькулятор")

input_text = tk.StringVar()

#Интерфейс логика
def click_num(digit):
    input_text.set(input_text.get() + str(digit))

def click_op(op_symbol):
    current = input_text.get()
    if current and not current.endswith(" "):
        input_text.set(current + " " + op_symbol + " ")

def btn_clear():
    input_text.set("")

def equal():
    try:
        expression = input_text.get()
        parts = expression.split()
        
        if len(parts) != 3:
            input_text.set("Ошибка")
            return
            
        first_num = float(parts[0])
        operation = parts[1]
        second_num = float(parts[2])
        
        if operation == "+": result = calc.add(first_num, second_num)
        elif operation == "-": result = calc.subtract(first_num, second_num)
        elif operation == "*": result = calc.multiply(first_num, second_num)
        elif operation == "/": result = calc.divide(first_num, second_num)
        elif operation == "%": result = calc.modulo(first_num, second_num)
        else: result = "Ошибка"
            
        input_text.set(result)
    except:
        input_text.set("Ошибка")

# Интерфейс (экран, кнопки)
text_screen = tk.Entry(window, textvariable=input_text, width=30, justify=tk.RIGHT, font=('Arial', 12))
text_screen.grid(row=0, column=0, columnspan=4, ipady=10)

# Ряд 1
tk.Button(window, text="C", width=7, height=2, fg="red", command=btn_clear).grid(row=1, column=0)
tk.Button(window, text="M+", width=7, height=2).grid(row=1, column=1)
tk.Button(window, text="MR", width=7, height=2).grid(row=1, column=2)
tk.Button(window, text="MC", width=7, height=2).grid(row=1, column=3)

# Ряд 2
tk.Button(window, text="Sin", width=7, height=2).grid(row=2, column=0)
tk.Button(window, text="Cos", width=7, height=2).grid(row=2, column=1)
tk.Button(window, text="xⁿ", width=7, height=2).grid(row=2, column=2)
tk.Button(window, text="√", width=7, height=2).grid(row=2, column=3)

# Ряд 3
tk.Button(window, text="7", width=7, height=2, command=lambda: click_num(7)).grid(row=3, column=0)
tk.Button(window, text="8", width=7, height=2, command=lambda: click_num(8)).grid(row=3, column=1)
tk.Button(window, text="9", width=7, height=2, command=lambda: click_num(9)).grid(row=3, column=2)
tk.Button(window, text="%", width=7, height=2, command=lambda: click_op("%")).grid(row=3, column=3)

# Ряд 4
tk.Button(window, text="4", width=7, height=2, command=lambda: click_num(4)).grid(row=4, column=0)
tk.Button(window, text="5", width=7, height=2, command=lambda: click_num(5)).grid(row=4, column=1)
tk.Button(window, text="6", width=7, height=2, command=lambda: click_num(6)).grid(row=4, column=2)
tk.Button(window, text="/", width=7, height=2, command=lambda: click_op("/")).grid(row=4, column=3)

# Ряд 5
tk.Button(window, text="1", width=7, height=2, command=lambda: click_num(1)).grid(row=5, column=0)
tk.Button(window, text="2", width=7, height=2, command=lambda: click_num(2)).grid(row=5, column=1)
tk.Button(window, text="3", width=7, height=2, command=lambda: click_num(3)).grid(row=5, column=2)
tk.Button(window, text="*", width=7, height=2, command=lambda: click_op("*")).grid(row=5, column=3)

# Ряд 6
tk.Button(window, text="0", width=7, height=2, command=lambda: click_num(0)).grid(row=6, column=0)
tk.Button(window, text=".", width=7, height=2, command=lambda: click_num(".")).grid(row=6, column=1)
tk.Button(window, text="-", width=7, height=2, command=lambda: click_op("-")).grid(row=6, column=2)
tk.Button(window, text="+", width=7, height=2, command=lambda: click_op("+")).grid(row=6, column=3)

# Кнопка равно
tk.Button(window, text="=", width=32, height=2, bg="#4caf50", fg="white", command=equal).grid(row=7, column=0, columnspan=4)

window.mainloop()

