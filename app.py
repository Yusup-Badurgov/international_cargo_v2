import tkinter as tk
from func import app_CRUD


# Создаем главное окно
window = tk.Tk()
window.geometry("700x500")
window.title("Рассчет стоимости перевозки личных вещей | ЕВРОПА")


# Создаем поле со списком для выбора страны
country_label = tk.Label(text="Выбрать страну:", font="Times 20")
country_label.pack()


country_options = app_CRUD.get_country()
country_var = tk.StringVar(window)
country_var.set(country_options[0])  # значение по умолчанию

country_combobox = tk.OptionMenu(window, country_var, *country_options)
country_combobox.pack()

# Создаем тумблер для выбора типа сделки
trade_type_label = tk.Label(text="Выбрать направление:", font="Times 20")
trade_type_label.pack()

trade_type_var = tk.BooleanVar(window)


export_radiobutton = tk.Radiobutton(window, text="Экспорт", font="Times 15", value=True, variable=trade_type_var)
export_radiobutton.pack()

import_radiobutton = tk.Radiobutton(window, text="Импорт", font="Times 15", value=False, variable=trade_type_var)
import_radiobutton.pack()

# Создаем поле для ввода значения
value_label = tk.Label(text="Введите количество кубов N m3:", font="Times 20")
value_label.pack()

value_entry = tk.Entry(window, font='Times 25')
value_entry.pack()


# Создаем кнопку "Рассчитать"
def calculate():
    # Получить выбранную страну и тип сделки
    country = country_var.get()
    trade_type = trade_type_var.get()

   # Получить значение кубометров введеное пользователем
    value_cube = value_entry.get()

    # Выполняем расчет и отображаем результат

    result_text.delete('1.0', 'end')
    result = app_CRUD.get_price(value_cube, country, trade_type)

    result_text.insert('1.0', result)
    result_text.config(state='normal')

calculate_button = tk.Button(window,font='Bold 20', fg='#FFFFFF', background='green', text="CДЕЛАТЬ РАСЧЕТ", command=calculate)
calculate_button.pack()

# Создаем метку для отображения результата
text = tk.Text()
result_text = tk.Text(window, state='normal', width=70, height=8, font='Times 12')
result_text.pack()

import pyperclip

def copy_result():
    result = result_text.get('1.0', 'end')
    pyperclip.copy(result)


calculate_button = tk.Button(window, font=18, text="Скопировать результат", command=copy_result)
calculate_button.pack()

# Запустить цикл событий tkinter
window.mainloop()

