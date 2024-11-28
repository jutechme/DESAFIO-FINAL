# import tkinter as tk 
# import sqlite3
# from tkinter import messagebox





# def create_db():
#     con = sqlite3.connect('meu_db')
#     cursor = con.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(
#                            id INTEGER PRIMARY KEY AUTOINCREMENT,
#                            nomes TEXT NOT NULL)''')


#     con.commit()
#     con.close()




# def salvar():
#     nome  =  entry.get()
#     if nome:
#         con = sqlite3.connect('meu_db')
#         cursor = con.cursor()
#         cursor.execute("INSERT INTO pessoas(nomes)VALUES (?) ", (nome,) )
#         con.commit()
#         cursor.close()
#         messagebox.showinfo('Dado inserido com sucesso', 'inserido com sucesso')
#         listar_nomes()
#         limpar_dados()


#     else:
#         messagebox.showerror('Ocorreu um erro', 'erro')        




# def listar_nomes():
#     con = sqlite3.connect('meu_db')
#     cursor = con.cursor()
#     cursor.execute('SELECT * FROM   pessoas')
#     registros = cursor.fetchall()
#     cursor.close()


#     listbox.delete(0, tk.END)
#     for registro in registros:
#         listbox.insert(tk.END,f'ID{registro[0]}, NOME {registro[1]}')





import tkinter as tk

 
def div():
    n1=float(input_entry.get())
    n2=float(input_entry2.get())
    imc = n1//n2**2
    resultado.config(text=f'resultado{imc}')


root=tk.Tk()
root.geometry('500x500')

label_n1= tk.Label(root, text='digite um seu peso (kg) ')

label_n1.pack()
input_entry= tk.Entry(root,width=10)
input_entry.pack(padx=50, pady=10)

label_n2= tk.Label(root, text='digite um altura (m) ')
label_n2.pack()

input_entry2= tk.Entry(root,width=10)
input_entry2.pack(padx=50, pady=10)



btn_IMC= tk.Button(root,text='IMC',fg='white',bg='black', command=div)
btn_IMC.pack()


resultado=tk.Label(root,text='resultado')
resultado.pack()










root.mainloop()