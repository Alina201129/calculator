import tkinter as tk
import operations as calc

window = tk.Tk()
window.title("Калькулятор")

input_text = tk.StringVar()

memory_value = 0.0

def click_num(digit):
    input_text.set(input_text.get() + str(digit))

def click_op(op_symbol):
    input_text.set(input_text.get() + op_symbol)

def click_trig_op(op_symbol):
    input_text.set(input_text.get() + op_symbol + "(")

def btn_clear():
    input_text.set("")

def memory_add():
    global memory_value
    try:
        memory_value += float(input_text.get())
    except:
        pass

def memory_clear():
    global memory_value
    memory_value = 0.0

def memory_recall():
    if memory_value % 1 == 0:
        input_text.set(int(memory_value))
    else:
        input_text.set(memory_value)

def memory_subtract():
    global memory_value
    try:
        memory_value -= float(input_text.get())
    except:
        pass

def equal():
    try:
        expression = input_text.get()
        
        allowed_names = {
            "Sin": calc.Sin,
            "Cos": calc.Cos,
            "Sqrt": calc.Sqrt,
            "Floor": calc.Floor,
            "Ceil": calc.Ceil
        }
        
        result = eval(expression, allowed_names)
        
        if isinstance(result, (int, float)):
            result = round(result, 10)
            if result % 1 == 0:
                result = int(result)
                
        input_text.set(result)
    except Exception as e:
        input_text.set("Ошибка")

text_screen = tk.Entry(window, textvariable=input_text, width=30, justify=tk.RIGHT, font=('Arial', 12))
text_screen.grid(row=0, column=0, columnspan=4, ipady=10)

tk.Button(window, text="C", width=7, height=2, fg="red", command=btn_clear).grid(row=1, column=0)
tk.Button(window, text="M+", width=7, height=2, command=memory_add).grid(row=1, column=1)
tk.Button(window, text="MR", width=7, height=2, command=memory_recall).grid(row=1, column=2)
tk.Button(window, text="MC", width=7, height=2, command=memory_clear).grid(row=1, column=3)

tk.Button(window, text="Sin", width=7, height=2, command=lambda: click_trig_op("Sin")).grid(row=2, column=0)
tk.Button(window, text="Cos", width=7, height=2, command=lambda: click_trig_op("Cos")).grid(row=2, column=1)
tk.Button(window, text="xⁿ", width=7, height=2, command=lambda: click_op("**")).grid(row=2, column=2)
tk.Button(window, text=")", width=7, height=2, command=lambda: click_op(")")).grid(row=2, column=3)

tk.Button(window, text="√", width=7, height=2, command=lambda: click_trig_op("Sqrt")).grid(row=3, column=0)
tk.Button(window, text="Floor", width=7, height=2, command=lambda: click_trig_op("Floor")).grid(row=3, column=1)
tk.Button(window, text="Ceil", width=7, height=2, command=lambda: click_trig_op("Ceil")).grid(row=3, column=2)
tk.Button(window, text="M-", width=7, height=2, command=memory_subtract).grid(row=3, column=3)

tk.Button(window, text="7", width=7, height=2, command=lambda: click_num(7)).grid(row=4, column=0)
tk.Button(window, text="8", width=7, height=2, command=lambda: click_num(8)).grid(row=4, column=1)
tk.Button(window, text="9", width=7, height=2, command=lambda: click_num(9)).grid(row=4, column=2)
tk.Button(window, text="%", width=7, height=2, command=lambda: click_op("%")).grid(row=4, column=3)

tk.Button(window, text="4", width=7, height=2, command=lambda: click_num(4)).grid(row=5, column=0)
tk.Button(window, text="5", width=7, height=2, command=lambda: click_num(5)).grid(row=5, column=1)
tk.Button(window, text="6", width=7, height=2, command=lambda: click_num(6)).grid(row=5, column=2)
tk.Button(window, text="/", width=7, height=2, command=lambda: click_op("/")).grid(row=5, column=3)

tk.Button(window, text="1", width=7, height=2, command=lambda: click_num(1)).grid(row=6, column=0)
tk.Button(window, text="2", width=7, height=2, command=lambda: click_num(2)).grid(row=6, column=1)
tk.Button(window, text="3", width=7, height=2, command=lambda: click_num(3)).grid(row=6, column=2)
tk.Button(window, text="*", width=7, height=2, command=lambda: click_op("*")).grid(row=6, column=3)

tk.Button(window, text="0", width=7, height=2, command=lambda: click_num(0)).grid(row=7, column=0)
tk.Button(window, text=".", width=7, height=2, command=lambda: click_num(".")).grid(row=7, column=1)
tk.Button(window, text="-", width=7, height=2, command=lambda: click_op("-")).grid(row=7, column=2)
tk.Button(window, text="+", width=7, height=2, command=lambda: click_op("+")).grid(row=7, column=3)

tk.Button(window, text="=", width=32, height=2, bg="#4caf50", fg="white", command=equal).grid(row=8, column=0, columnspan=4)

window.mainloop()
