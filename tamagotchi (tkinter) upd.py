import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk

weight = 10.00
thirst = 10.00
happiness = 10.00
DecreChar = 0.5

window = Tk()
window.title("тамагочи")
window.geometry('400x250')


def start():
    def decre():
        global weight, thirst, happiness
        weight -= DecreChar
        thirst -= DecreChar
        happiness -= DecreChar
    def food():
        lbl4.grid_remove()
        global weight, thirst, happiness
        decre()
        if (weight > 0.03) and (thirst > 0.03) and (happiness > 0.03):
            if (weight < 9.75) and (weight > 0):
                weight = weight + 0.25
                thirst = thirst - 0.06
            else:
                lbl4.config(text="Не голоден")
                lbl4.grid(column=0, row=4)
            lbl1.config(text=("голод", round(weight, 2)))
            lbl2.config(text=("жажда", round(thirst, 2)))
            lbl3.config(text=("счастье", round(happiness, 2)))
        else:
            messagebox.showerror("тамагочи", "питомец умер")
            quit()

    def water():
        lbl4.grid_remove()
        global weight, thirst, happiness
        decre()
        if (weight > 0.03) and (thirst > 0.03) and (happiness > 0.03):
            if (thirst < 9.75) and (thirst > 0):
                thirst = thirst + 0.25
                weight = weight - 0.07
            else:
                lbl4.config(text="Не хочет пить")
                lbl4.grid(column=0, row=4)
            lbl1.config(text=("голод", round(weight, 2)))
            lbl2.config(text=("жажда", round(thirst, 2)))
            lbl3.config(text=("счастье", round(happiness, 2)))
        else:
            messagebox.showerror("тамагочи", "питомец умер")
            quit()

    def play():
        lbl4.grid_remove()
        global weight, thirst, happiness
        decre()
        if (weight > 0.03) and (thirst > 0.03) and (happiness > 0.03):
            if (happiness < 9.75) and (happiness > 0):
                happiness = happiness + 0.25
                thirst = thirst - 0.07
                weight = weight - 0.06
            else:
                lbl4.config(text="не хочет играть")
                lbl4.grid(column=0, row=4)
            lbl1.config(text=("голод", round(weight, 2)))
            lbl2.config(text=("жажда", round(thirst, 2)))
            lbl3.config(text=("счастье", round(happiness, 2)))
        else:
            messagebox.showerror("тамагочи", "питомец умер")
            quit()

    # Функция ignore отвечает за действие "игнорировать". Все переменные остаются равны сами себе.
    def ignore():
        global weight, thirst, happiness
        lbl4.grid_remove()
        if (weight > 0.03) and (thirst > 0.03) and(happiness > 0.03):
            decre()
            lbl1.config(text=("голод",round(weight,2)))
            lbl2.config(text=("жажда",round(thirst,2)))
            lbl3.config(text=("счастье",round(happiness,2)))
        else:
            messagebox.showerror("тамагочи", "питомец умер")
            quit()
    def info():
        messagebox.showinfo('Инструкция',"""
+ Вы несете ответственность за жизнь своего питомца, для этого вы должны его кормить,
поить и играть с ним.

+ Обратите внимание, что каждое ваше действие изменяет статистику
ваш питомец, когда вы его кормите, будет набирать вес, но будет больше пить, когда
будете поить - будет более голодным, если вы с ним поиграете, то будет более голодным и жаждущим.

+ Помните, что если вы игнорируете своего питомца, все его характеристики будут снижаться каждый ход.

+ Если вы опустите любую из характеристик до 0, ваш питомец умрет.""")
    lbl5=Label(window,text="кот Антон",font=font.Font(weight="bold"))
    lbl5.grid(column=2,row=0)
    lbl1 = Label(window, text=("голод", weight))
    lbl1.grid(column=0, row=1)
    lbl2 = Label(window, text=("жажда", thirst))
    lbl2.grid(column=1, row=1)
    lbl3 = Label(window, text=("счастье", happiness))
    lbl3.grid(column=2, row=1)
    lbl4 = Label(window, text="")

    btn1 = Button(window, text="кормить", command=food)
    btn1.grid(column=0, row=2)
    btn2 = Button(window, text="поить", command=water)
    btn2.grid(column=1, row=2)
    btn3 = Button(window, text="играть", command=play)
    btn3.grid(column=2, row=2)
    btn4 = Button(window, text="игнорировать", command=ignore)
    btn4.grid(column=3, row=2)
    btn5 = Button(window, text="инструкция", command=info)
    btn5.grid(column=2, row=4)

    canvas = tkinter.Canvas(window, height=150, width=150)
    image = Image.open("cat.png")
    image = image.resize((150, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.grid(column=2, row=5)
    window.mainloop()
start()