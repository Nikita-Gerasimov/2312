
def func():
    print("Кнопка")
def func2():
    exit()
def BackGround0():
    root0.config(bg="red")
def BackGround1():
    root0.config(bg="yellow")
def BackGround2():
    root0.config(bg="green")
    

from tkinter import *
root0 = Tk()
root0.geometry("400x200")
btn0 = Button(root0, text="Кнопка", bg="gray", command=func)
btn0.pack()
btn2 = Button(root0, text="Красный фон", bg="red", command=BackGround0)
btn2.pack()
btn2 = Button(root0, text="Жёлтый фон", bg="yellow", command=BackGround1)
btn2.pack()
btn2 = Button(root0, text="Зелёный фон", bg="green", command=BackGround2)
btn2.pack()
btn1 = Button(root0, text="Выход", bg="gray", command=func2)
btn1.pack()




