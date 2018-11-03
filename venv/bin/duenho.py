from tkinter import *
import tkinter.messagebox

def visualizar_datos_duenho(root, usuario):
    datos_duenho = Frame(root)
    datos_duenho.grid(column=0, row=0, sticky="nsew")
    root.title("Datos del papurri")

    nombre = Label(datos_duenho, text="Nombre: ")
    nombre.grid(column=0, row=0)

    nombre_info = Label(datos_duenho, text=usuario.name)
    nombre_info.grid(column=0, row=1)

    dni = Label(datos_duenho, text="DNI: ")
    dni.grid(column=1, row = 0)

    dni_info = Label(datos_duenho, text=usuario.dni)
    dni_info.grid(column=1, row=1)

    email = Label(datos_duenho, text="Correo electronico: ")
    email.grid(column=2, row=0)

    email_info = Label(datos_duenho, text=usuario.email)
    email_info.grid(column=2, row=1)

    fundo = Label(datos_duenho, text="Nombre del fundo: ")
    fundo.gird(column=3, row=0)

    fundo_info = Label(datos_duenho, text=usuario.fundo_name)
    fundo_info.grid(column=3, row=1)

    datos_duenho.tkraise()