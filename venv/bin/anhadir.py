from Tkinter import *
import ttk
from vacas import *

# -*- coding: 850 -*-
def  presentar_informacion():

    f = open('vacas.txt', 'w')
    """for i in range (len(parametros_informacion)):"""





root = Tk()

root.title("Anadir Informacion del Bovino")
root.geometry("300x400+300+50")

menu = Menu(root)
root.config(menu=menu)

i_o_p=0

parametros_informacion=["Numero de arete","Especie","Raza","Sexo","Fecha de nacimiento","Nro de arete de la madre",
            "Nro de arete de la madre","Edad al destete","Peso al destete","Fecha de venta","Fecha de cambio",
            "Fecha de muerte","Nacimiento","Destete","Ano","Dos Anos","Faenado"]

"""parametros_peso=["Nacimiento","Destete","Ano","Dos Anos","Faenado"]"""
"""
for i in range(len(parametros_informacion)):
    Label(root, text=parametros_informacion[i]).grid(row=i, column=0)

for i in range(len(parametros_informacion)):
    exec ('e=Entry(root).grid(row=i, column=1)'.format(i))
"""

notebook = ttk.Notebook(root)
notebook.pack(fill='both',expand='yes')

info=ttk.Frame(root)
pes=ttk.Frame(root)

notebook.add(info,text="informacion")
"""notebook.add(pes,text="peso")"""

for i in range(len(parametros_informacion)):
   Label(info, text=parametros_informacion[i]).grid(row=i, column=0)

for i in range(len(parametros_informacion)):
    exec ('e=Entry(info).grid(row=i, column=1)'.format(i))

"""""
for i in range(len(parametros_peso)):
   Label(pes, text=parametros_peso[i]).grid(row=i, column=0)

for i in range(len(parametros_peso)):
    exec ('e=Entry(pes).grid(row=i, column=1)'.format(i).format(i))
"""
boton1 = ttk.Button(info, text="Guardar").grid(row=17, column=0)
boton2 = ttk.Button(info, text="Regresar").grid(row=17, column=1)
"""""
boton11 = ttk.Button(pes, text="Guardar").grid(row=5, column=0)
boton22 = ttk.Button(pes, text="Regresar").grid(row=5, column=1)
"""
"temp_vaca = Vaca()"

root.mainloop()