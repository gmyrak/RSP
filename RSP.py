from tkinter import *
import random

win = Tk()
win.geometry('600x300')
win.resizable(0, 0)
win.title('RSP')

items = 'Камень', 'Ножницы', 'Бумага'

lab_attr = {'font': 'Verdana 20 bold'}
but_attr = {'font': 'Verdana 20 bold', 'bg': 'yellow', 'border': 6, 'fg': 'blue'}

raund = 0
count_player = 0
count_comp = 0

lb_raund = Label(text=f'Игр: {raund}', **lab_attr)
lb_raund.pack()

buttons = Frame()
buttons.pack()

for p in range(3):
    eval(f"Button(buttons, text = items[{p}], **but_attr, command=lambda : game({p})).pack(side='left')")

ch = Frame()
ch.pack()
lb_player = Label(ch, **lab_attr, width=10)
lb_comp = Label(ch, **lab_attr, width=10)

Label(ch, text='Человек:', **lab_attr).grid(row=0, column=0, sticky='e')
Label(ch, text='Компьютер:', **lab_attr).grid(row=1, column=0, sticky='e')
lb_player.grid(row=0, column=1)
lb_comp.grid(row=1, column=1)

lb_count_player = Label(ch, **lab_attr, text=count_player)
lb_count_player.grid(row=0, column=2)
lb_count_comp = Label(ch, **lab_attr, text=count_comp)
lb_count_comp.grid(row=1, column=2)

lb_winner = Label(**lab_attr)
lb_winner.pack()

ch_show_comp = Checkbutton(text='Показать ход компьютера')
ch_show_comp.pack()

def winner(a, b):
    return a - b if abs(a - b) < 2 else (b - a)//2


def comp_chouse():
    return random.randint(0, 2)


def game(player):
    global raund, count_player, count_comp

    raund += 1
    comp = comp_chouse()
    res = winner(player, comp)

    if res < 0:
        count_player += 1
        lb_winner.config(text='Выиграл человек', fg='green')
    elif res > 0:
        count_comp += 1
        lb_winner.config(text='Выиграл компьютер', fg='red')
    else:
        lb_winner.config(text='Ничья', fg='black')

    lb_raund.config(text=f'Игр: {raund}')
    lb_player.config(text= items[player])
    lb_comp.config(text=items[comp])
    lb_count_player.config(text=count_player)
    lb_count_comp.config(text=count_comp)


win.mainloop()


