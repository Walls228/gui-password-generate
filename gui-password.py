# Полключение необходимых библиотек
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
import random

gui_generator = Tk() # создаем переменную
gui_generator.title("Генератор паролей") # заголовок окна
gui_generator.geometry("565x560") # начальные размеры окна
gui_generator.resizable(width=False, height=False) # запрет на изменения окна
gui_generator.configure(bg='black') # цвет фона окна
gui_generator.iconbitmap(r'img.ico') # установка иконки программы

# символы для генерации паролей
chars = 'qwertyuiopasdfghjklzxcvbnm'
symbols='+-#$%^&*()'
num='0123456789'
# финальный список для генерации паролей (метод upper для генерации заглавных букв)
# list (список) для того, чтобы наши элементы являлись отдельным символом для random.choice
chars = list(chars + chars.upper() + symbols + num)

# функция генерации пароля
def generate():
    # проверка на пустые строки
    if entry_count.get() == '':
        showinfo(title="Ошибка!", message="Необходимо ввести кол-во паролей")
    elif entry_len.get() == '':
        showinfo(title="Ошибка!", message="Необходимо ввести длину паролей")

    # проверка исключений на ввод не цифр
    try:
        len_pass = int(entry_len.get())
        count_pass = int(entry_count.get())
    except:
            showinfo(title="Ошибка!", message="Необходимо вводить, только цифры")

    # если проверки все пройдены, то выполнить код
    else:
        # очистка текста с текстового поля
        text_field.delete(0.0, END)
        # цикл итерует столько раз, сколько указано в переменной count_pass
        # цикл отвечает за, то, что пароль будет сгенерирован необходимое количество раз
        # Функция range() возвращает объект, создающий последовательность чисел, начинающуюся с 0 (по умолчанию), 
        # последовательно увеличивающуюся (по умолчанию на 1).
        for i in range(count_pass):
            password = ''
            # цикл итерирует столько раз, сколько указано в переменной len_pass
            # цикл нужен для генерации 1 пароля
            # random.choice - возвращает случайный элемент из указанной последовательности
            # += - cуммирует значение обеих сторон и присваивает его выражению слева
            # + - добавление
            # \n - пароль на новой строке
            for j in range(len_pass):
                password += random.choice(chars)
            text_field.insert(END, password+'\n')

# функция очистки текста с текстового поля
def clear():
    text_field.delete(0.0, END) # 0.0 начало текста и END конец текста

# сохраняем текст из текстового поля в файл
# asksaveasfilename(): открывает диалоговое окно для сохранения файла и возвращает путь к сохраненному файлу. 
# Если файл не выбран, возвращается пустая строка ""
def save_file():
    filepath = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("All files", "*.*")))
    if filepath != "":
        text = text_field.get(0.0, END)
        with open(filepath, "w") as file:
            file.write(text)
            file.close()

# метод place указывает положение либо в абсолютных значениях (в пикселях), 
# либо в долях родительского окна, то есть относительно.
# Добавляем надпись и текстовое поле для ввода кол-ва паролей
col_pass = Label(gui_generator, text='Кол-во паролей: ', bg='black', fg='white').place(x=70, y=30)
entry_count = Entry(gui_generator, width=15)
entry_count.place(x=190, y=30)

# Добавляем надпись и текстовое поле для длины пароля
dl_pass = Label(gui_generator, text='Длина паролей: ', bg='black', fg='white').place(x=70, y=60)
entry_len = Entry(gui_generator, width=15)
entry_len.place(x=190, y=60)

# Добавляем кнопки "Очистить", "Генерировать" и "Сохранить"
btn_clear = Button(gui_generator, text="Очистить", command=clear).place(x=420, y=40)
btn_generate = Button(gui_generator, text='Генерировать', command=generate).place(x=330, y=40)
btn_save = Button(gui_generator, text='Сохранить', command=save_file).place(x=485, y=40)

# Добавляем многосточное текстовое поле
text_field = Text(gui_generator, width=69, height=25)
text_field.place(x=5, y=150)

# функция бесконечного цикла окна
# Окно будет ждать любого взаимодействия с пользователем, пока не будет закрыто
gui_generator.mainloop()