import tkinter as tk
from tkinter import messagebox


def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            raise ZeroDivisionError
        result = float(entry1.get()) / denominator
        result_label.config(text="Результат: " + str(result))
    except ZeroDivisionError:
        messagebox.showerror("Помилка", "Ділення на нуль неможливе")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root, width=10)
entry2 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Перше число:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Друге число:").grid(row=1, column=0, padx=5, pady=5)

button_add = tk.Button(root, text="+", width=5, command=add)
button_add.grid(row=2, column=0, padx=5, pady=5)
button_subtract = tk.Button(root, text="-", width=5, command=subtract)
button_subtract.grid(row=2, column=1, padx=5, pady=5)
button_multiply = tk.Button(root, text="*", width=5, command=multiply)
button_multiply.grid(row=2, column=2, padx=5, pady=5)
button_divide = tk.Button(root, text="/", width=5, command=divide)
button_divide.grid(row=2, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="Результат: ")
result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# root.mainloop()  # Видаляємо виклик, щоб інтерфейс міг тестуватися
