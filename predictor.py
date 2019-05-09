from tkinter import *

win = Tk()
win.geometry('1000x600+20+20') # Ширина x Высота + Отступ справа + Отступ слева
win.title('Статистика нажатий клавиш') # заголовок окна
win.resizable(False, True) # Можно изменять размер только по вертикали

panel1 = Frame()
panel1.place(width=500, relheight=1) # Левая панель для текстового поля
panel2 = Frame()
panel2.place(x= 500, width=500, relheight=1) # Правая панель для информации и настроек

# Текстовое поле для вывода информации о ходе игры
text = Text(panel1)
text.place(x=20, relwidth=1, relheight=1) # Левый край отступает 20px -
# это место для линейки прокрутки
# относительные ширина и высота =1
# это значит, что занимаем всё доступное место
# в родительском компоненте (Panel1)

text.config(state=DISABLED) # Запрещаем изменение текста вручную

text.tag_config('default', font='"Courier New" 14')
text.tag_config('ok',      font='"Courier New" 14 bold', foreground='green')
text.tag_config('fail',    font='"Courier New" 14 bold', foreground='red')


def write(msg, style='default'):
    '''Процедура для записи в текстовое поле
    Текст "только для чтения" - мы не можем писать туда вручную,
    только со стороны программы'''
    text.config(state=NORMAL) # Разрешаем изменение
    text.insert(END, msg, style) # Записываем сообщение в конец текста
    text.config(state=DISABLED) # Запрещаем изменение
    text.see(END) # Позииционируемся в конец


def clean_text():
    '''Процедура очистки текста'''
    text.config(state=NORMAL) # Разрешаем изменение
    text.delete('1.0', END) # удаляем от первой строки, нулевой позиции до самого конца
    text.config(state=DISABLED) # Запрещаем изменение

#write("Hello.....\n")

# Создаем линейку прокрутки и связываем её с текстовым полем
scrol = Scrollbar(panel1)
scrol.place(width=20, relheight=1)
scrol['command'] = text.yview
text['yscrollcommand'] = scrol.set

# Метка для вывода информации
lb_info = Label(panel2, justify=LEFT, font='Verdana 16')
lb_info.place(x=10, y=150)

win.mainloop()