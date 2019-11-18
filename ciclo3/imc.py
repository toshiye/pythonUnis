# coding=utf8

from tkinter import *

def bt_calculo():

    num1 = float(ed3.get())
    print(num1)

    num2 = float(ed4.get())
    print(num2)

    imc = num2 / (num1 * num1)
    print(imc)

    nome = ed1.get('1.0', END)
    print(nome)
    if (num1 and num2):
        if(imc < 17.0):
            lb5["text"] = nome + "Você está: \n" + "Muito abaixo do peso: Cade você?"
        elif(imc >= 17.0 and imc < 18.49):
            lb5["text"] =nome + "Você está: \n" + "Abaixo do peso: Você está abaixo do peso,\n melhor se cuidar."
        elif(imc >= 18.5 and imc < 24.99):
            lb5["text"] =nome + "Você está com: \n" + "Peso normal: Parabéns, você está com bom peso."
        elif(imc >= 25.0 and imc < 29.99):
            lb5["text"] =nome + "Você está: \n" + "Acima do peso: Cuidado, você está acima do peso."
        elif(imc >= 30 and imc < 34.99):
            lb5["text"] =nome + "Você está com: \n" + "Obesidade I: Você está Obeso, melhor começar\n um regime!"
        elif(imc >= 35 and imc < 39.99):
            lb5["text"] =nome + "Você está com: \n" + "Obesidade severa: É sério, sua Obesidade é SEVERA,\n ainda não começou o regime?"
        elif(imc > 40):
            lb5["text"] =nome + "Você está com: \n" + "Obesidade mórbida: Agora deu,\n Você não come mais nada\n até parecer a Gisele Bündchen!!!"
    else:
        lb5["text"] = "Valores informados inválidos!"

def btn_reset():
    ed1.delete('1.0', END)
    ed2.delete('1.0', END)
    ed3.delete(first=0, last=1000)
    ed4.delete(first=0, last=1000)

def btn_close():
    mainWindow.destroy()

mainWindow = Tk()
mainWindow.title("Cálculo de IMC - Índice de Massa Corporal")

lb1 = Label(mainWindow, text="Nome do Paciente")
lb1.place(x=30, y=30)

ed1 = Text(mainWindow, height=1, width=48)
ed1.place(x=170, y=30)

lb2 = Label(mainWindow, text="Endereço Completo")
lb2.place(x=30, y=80)

ed2 = Text(mainWindow, height=1, width=48)
ed2.place(x=170, y=80)

lb3 = Label(mainWindow, text="Altura (cm)")
lb3.place(x=30, y=130)

ed3 = Entry(mainWindow)
ed3.place(x=170, y=130)

lb4 = Label(mainWindow, text="Peso (kg)")
lb4.place(x=30, y=180)

ed4 = Entry(mainWindow)
ed4.place(x=170, y=180)

lb5 = Label(mainWindow, text="Seu resultado aparecerá aqui...")
lb5.place(x=320, y=130)

bt = Button(mainWindow, text="CALCULAR", width=20, command=bt_calculo)
bt.place(x=30, y=250)

bt = Button(mainWindow, text="Reiniciar", width=20, command=btn_reset)
bt.place(x=200, y=250)

bt = Button(mainWindow, text="Sair", width=20, command=btn_close)
bt.place(x=370, y=250)

mainWindow.geometry("600x300+600+200")
mainWindow.mainloop()