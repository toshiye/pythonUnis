# coding=utf8

import tkinter as tk
from tkinter import ttk
import psycopg2

#Início do bloco de Conexão com o banco PostgreSQL e criação do schema e da tabela
try:
    connection = psycopg2.connect(user="postgres", password="Shigeyoshi@21", host="localhost", port="5432", database="imc")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE SCHEMA IF NOT EXISTS imcschema;
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS imcschema.imc (
            ID SERIAL PRIMARY KEY NOT NULL,
            NAME VARCHAR(250) NOT NULL,
            ADDRESS VARCHAR(250) NOT NULL,
            ALTURA DOUBLE PRECISION NOT NULL,
            PESO DOUBLE PRECISION NOT NULL,
            CALCULO DOUBLE PRECISION NOT NULL,
            RESULTADO VARCHAR(250) NOT NULL 
        );
    ''')

    connection.commit()
except(Exception, psycopg2.Error) as error:
    if(connection):
        print('Não deu certo amiguinho!!!', error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Conexão com o banco encerrada")
#Fim do bloco de Conexão com o banco PostgreSQL e criação do schema e da tabela

#Início do bloco de Funções
def bt_calculo():

    num1 = float(ed3.get())
    print(num1)

    num2 = float(ed4.get())
    print(num2)

    imc = num2 / (num1 * num1)
    print(imc)

    nome = ed1.get('1.0', tk.END)
    print(nome)
    if (num1 and num2):
        if(imc < 17.0):
            lb5["text"] = nome + " Você está: \n" + "Muito abaixo do peso: Cade você?"
        elif(imc >= 17.0 and imc < 18.49):
            lb5["text"] =nome + " Você está: \n" + "Abaixo do peso: Você está abaixo do peso,\n melhor se cuidar."
        elif(imc >= 18.5 and imc < 24.99):
            lb5["text"] =nome + " Você está com: \n" + "Peso normal: Parabéns, você está com bom peso."
        elif(imc >= 25.0 and imc < 29.99):
            lb5["text"] =nome + " Você está: \n" + "Acima do peso: Cuidado, você está acima do peso."
        elif(imc >= 30 and imc < 34.99):
            lb5["text"] =nome + " Você está com: \n" + "Obesidade I: Você está Obeso, melhor começar\n um regime!"
        elif(imc >= 35 and imc < 39.99):
            lb5["text"] =nome + " Você está com: \n" + "Obesidade severa: É sério, sua Obesidade é SEVERA,\n ainda não começou o regime?"
        elif(imc > 40):
            lb5["text"] =nome + "Você está com: \n" + "Obesidade mórbida: Agora deu,\n Você não come mais nada\n até parecer a Gisele Bündchen!!!"
    else:
        lb5["text"] = "Valores informados inválidos!"

def btn_reset():
    ed1.delete('1.0', tk.END)
    ed2.delete('1.0', tk.END)
    ed3.delete(first=0, last=1000)
    ed4.delete(first=0, last=1000)
    lb5['text'] = ''

def btn_close():
    mainWindow.destroy()

def pop_list():
    try:
        connection = psycopg2.connect(user="postgres", password="Shigeyoshi@21", host="localhost", port="5432",
                                      database="imc")
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM imcschema.imc')

        rows = cursor.fetchall()

        for row in rows:
            print(row)

            treeCons.insert("", tk.END, values=row)


    except(Exception, psycopg2.Error) as error:
        if (connection):
            print('Não encontrei nada fera!!!', error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("Conexão com o banco encerrada")

def btn_save():
    try:
        connection = psycopg2.connect(user="postgres", password="Shigeyoshi@21", host="localhost", port="5432", database="imc")
        cursor = connection.cursor()

        name = str(ed1.get('1.0', tk.END)).replace('\n', '')
        address = str(ed2.get('1.0', tk.END)).replace('\n', '')
        altura = float(ed3.get())
        peso = float(ed4.get())
        calculo = float(ed4.get()) / (float(ed3.get()) ** 2)
        resultado = str(lb5['text']).replace('\n', '')

        insert_query = '''INSERT INTO imcschema.imc (name, address, altura, peso, calculo, resultado) VALUES (%s, %s, %s, %s, %s, %s);'''
        record_to_insert = (name, address, altura, peso, calculo, resultado)

        cursor.execute(insert_query, record_to_insert)

        connection.commit()

        btn_reset()

        print('Dados inseridos com sucesso')
    except(Exception, psycopg2.Error) as error:
        if (connection):
            print('Não deu pra salvar nada!!!', error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("Conexão com o banco encerrada")

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

#Fim do bloco de Funções

#Início do bloco de criação da Interface de Usuário
mainWindow = tk.Tk()
mainWindow.title("Cálculo de IMC - Índice de Massa Corporal")

lb1 = tk.Label(mainWindow, text="Nome do Paciente")
lb1.place(x=30, y=30)

ed1 = tk.Text(mainWindow, height=1, width=48)
ed1.place(x=170, y=30)

lb2 = tk.Label(mainWindow, text="Endereço Completo")
lb2.place(x=30, y=80)

ed2 = tk.Text(mainWindow, height=1, width=48)
ed2.place(x=170, y=80)

lb3 = tk.Label(mainWindow, text="Altura (cm)")
lb3.place(x=30, y=130)

ed3 = tk.Entry(mainWindow)
ed3.place(x=170, y=130)

lb4 = tk.Label(mainWindow, text="Peso (kg)")
lb4.place(x=30, y=180)

ed4 = tk.Entry(mainWindow)
ed4.place(x=170, y=180)

lb5 = tk.Label(mainWindow, text="Seu resultado aparecerá aqui...")
lb5.place(x=320, y=130)

bt = tk.Button(mainWindow, text="CALCULAR", width=15, command=bt_calculo)
bt.place(x=30, y=250)

bt = tk.Button(mainWindow, text="Salvar", width=15, command=combine_funcs(btn_save))
bt.place(x=150, y=250)

bt = tk.Button(mainWindow, text="Lista", width=15, command=combine_funcs(pop_list))
bt.place(x=270, y=250)

bt = tk.Button(mainWindow, text="Reiniciar", width=15, command=btn_reset)
bt.place(x=390, y=250)

bt = tk.Button(mainWindow, text="Sair", width=15, command=btn_close)
bt.place(x=510, y=250)

#def create_tree_view():
treeCons = ttk.Treeview(mainWindow, columns=('id', 'name', 'address', 'altura', 'peso', 'calculo', 'resultado'), show='headings')

# self.treeCons['columns'] = ('name', 'calculo', 'resultado')
treeCons.heading('id', text='ID')
treeCons.column('id', width=20)

treeCons.heading('name', text='Nome do Paciente')
treeCons.column('name', width=200)

treeCons.heading('address', text='Endereço')
treeCons.column('address', width=250)

treeCons.heading('altura', text='Altura')
treeCons.column('altura', width=40)

treeCons.heading('peso', text='Peso')
treeCons.column('peso', width=40)

treeCons.heading('calculo', text='Cálculo')
treeCons.column('calculo', width=50)

treeCons.heading('resultado', text='Resultado')
treeCons.column('resultado', width=750)


treeCons.place(x=15, y=290)

mainWindow.geometry("1385x600+100+100")
mainWindow.mainloop()
#Fim do bloco de criação da Interface de Usuário