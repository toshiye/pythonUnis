from tkinter import *

janela = Tk()

lb1 = Label(janela, text="horizontal", bg="white")
lb1.pack(side=TOP, fill=X)

lb2 = Label(janela, text="", bg="black")
lb2.pack(side=LEFT, fill=Y)

lb3 = Label(janela, text="", bg="black")
lb3.pack(side=RIGHT, fill=Y)

janela.geometry("500x200+600+200")
janela.mainloop()