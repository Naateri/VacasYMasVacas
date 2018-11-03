from tkinter import *
import tkinter.messagebox

def volver(root):
    tkinter.messagebox.showinfo("Volver", "Volviendo al menu principal")

def visualizar_datos_duenho(root, usuario):
    datos_duenho = Frame(root)
    datos_duenho.grid(column=0, row=0, sticky="nsew")
    root.title("Datos del papurri")

    nombre = Label(datos_duenho, text="Nombre: ")
    nombre.grid(column=0, row=0)

    nombre_info = Label(datos_duenho, text=usuario.name)
    nombre_info.grid(column=1, row=0)

    dni = Label(datos_duenho, text="DNI: ")
    dni.grid(column=0, row = 1)

    dni_info = Label(datos_duenho, text=usuario.dni)
    dni_info.grid(column=1, row=1)

    email = Label(datos_duenho, text="Correo electrónico: ")
    email.grid(column=0, row=2)

    email_info = Label(datos_duenho, text=usuario.email)
    email_info.grid(column=1, row=2)

    fundo = Label(datos_duenho, text="Nombre del fundo: ")
    fundo.grid(column=0, row=3)

    fundo_info = Label(datos_duenho, text=usuario.fundo_name)
    fundo_info.grid(column=1, row=3)

    btn_back = Button(datos_duenho, text="Volver", command=lambda:volver(root))
    btn_back.grid(column=0, row=4)

    datos_duenho.tkraise()

def visualizar_datos_fundo(root, usuario):
    datos_fundo = Frame(root)
    datos_fundo.grid(column=0, row=0, sticky="nsew")
    root.title("Datos del guanito")

    nombre = Label(datos_fundo, text="Nombre del fundo: ")
    nombre.grid(column=0, row=0)

    nombre_info = Label(datos_fundo, text=usuario.fundo_name)
    nombre_info.grid(column=1, row=0)

    ubicacion = Label(datos_fundo, text="Ubicación: ")
    ubicacion.grid(column=0, row=1)

    ubicacion_info = Label(datos_fundo, text="Toroy")
    ubicacion_info.grid(column=1, row=1)

    btn_back = Button(datos_fundo, text="Volver", command=lambda: volver(root))
    btn_back.grid(column=0, row=4)

    datos_fundo.tkraise()


