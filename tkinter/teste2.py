from tkinter import *

janela = Tk()

janela.geometry("300x300+200+200")

lb = Label(janela, text='Fala pessoal!')
lb.place(x=100, y=100)

janela.mainloop()