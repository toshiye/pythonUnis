from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1")
lb1.grid(row=1, column=1)

lb2 = Label(janela, text="Label 2")
lb2.grid(row=2, column=2)

janela.geometry("500x200+600+200")
janela.mainloop()