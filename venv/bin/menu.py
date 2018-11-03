from tkinter import *
import tkinter.messagebox
from user import Usuario


def raise_frame(frame):
    frame.tkraise()

def create_addmenu(root) :
    message = "Añadir Menu"
    tkinter.messagebox.showinfo("Creando", message)

def create_seemenu(root) :
    message = "Visualizar Menu"
    tkinter.messagebox.showinfo("Creando", message)

def create_deletemenu(root) :
    message = "Eliminar Menu"
    tkinter.messagebox.showinfo("Creando", message)

def create_findmenu(root) :
    message = "Buscar Menu"
    tkinter.messagebox.showinfo("Creando", message)

def create_infomenu(root) :
    message = "Informacion Menu"
    tkinter.messagebox.showinfo("Creando", message)

def exit(root) :
    message = "Menu"
    tkinter.messagebox.showinfo("Saliendo", message)

def create_menu(root):

    my_menu = Frame(root)
    my_menu.grid(column=0, row=0, sticky="nsew")
    root.title("Menu principal")

    btn_add = Button(my_menu, text="Añadir", command=lambda: create_addmenu(root))
    btn_add.grid(column=0, row=0)

    btn_see = Button(my_menu, text="Visualizar", command=lambda: create_seemenu(root))
    btn_see.grid(column=0, row=1)

    btn_delete = Button(my_menu, text="Eliminar", command = lambda:create_deletemenu(root))
    btn_delete.grid(column = 0, row = 2)

    btn_find = Button(my_menu, text="Buscar", command = lambda:create_findmenu(root))
    btn_find.grid(column = 0, row = 3)

    btn_info = Button(my_menu, text="Información", command = lambda:create_infomenu(root))
    btn_info.grid(column = 0, row = 4)

    btn_exit= Button(my_menu, text="Cerrar", command = lambda:exit(root))
    btn_exit.grid(column = 0, row = 5)
    raise_frame(my_menu)