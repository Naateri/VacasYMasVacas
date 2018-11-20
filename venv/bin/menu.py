from tkinter import *
import tkinter.messagebox
from user import Usuario


def raise_frame(frame):
    frame.tkraise()

def add_info(root):
    #message = "Visualizar Menu"
    tkinter.messagebox.showinfo("Añadir Información ","Agregando información del Bovino")

def add_peso(root):
    # message = "Visualizar Menu"
    tkinter.messagebox.showinfo("Añadir Peso ","Agregando peso del Bovino")

def add_sanitaria(root):
    # message = "Visualizar Menu"
    tkinter.messagebox.showinfo("Añadir Sanitaria ","Agregando ficha sanitaria del Bovino")

def create_addmenu(root) :
   my_addmenu = Frame(root)
   my_addmenu.grid(column=0, row=0, sticky="nsew")
   root.title("Menú Añadir")

   btn_addinfo = Button(my_addmenu, text="Añadir Información", command=lambda: add_info(root))
   btn_addinfo.grid(column=0, row=0)

   btn_addpeso = Button(my_addmenu, text="Añadir Peso", command=lambda: add_peso(root))
   btn_addpeso.grid(column=0, row=1)

   btn_addsanitaria = Button(my_addmenu, text="Añadir Ficha Sanitaria", command=lambda: add_sanitaria(root))
   btn_addsanitaria.grid(column=0, row=2)

   btn_regresar = Button(my_addmenu, text="Regresar", command=lambda: create_menu(root))
   btn_regresar.grid(column=0, row=3)

def see_inv(root):
    my_seeinvmenu = Frame(root)
    my_seeinvmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Inventario del Ganado")

    hemc= Label( my_seeinvmenu, text="Número de Crías Hembras: ")
    hemc.grid(column=0, row=0)

    hemc_num = Label( my_seeinvmenu,text="150" )
    hemc_num.grid(column=1, row=0)

    macc = Label(my_seeinvmenu, text="Número de Crías Machos: ")
    macc.grid(column=0, row=1)

    macc_num = Label(my_seeinvmenu, text="150")
    macc_num.grid(column=1, row=1)

    hem = Label(my_seeinvmenu, text="Número de Hembras: ")
    hem.grid(column=0, row=2)

    hem_num = Label(my_seeinvmenu, text="500")
    hem_num.grid(column=1, row=2)

    mac = Label(my_seeinvmenu, text="Número de Machos: ")
    mac.grid(column=0, row=3)

    mac_num = Label(my_seeinvmenu, text="300")
    mac_num.grid(column=1, row=3)

    btn_regresar = Button(my_seeinvmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=4)

def see_pro(root):
    my_seeinvmenu = Frame(root)
    my_seeinvmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Reporte Productivo del Ganado")

    hemc= Label( my_seeinvmenu, text="Número de Arete")
    hemc.grid(column=0, row=0)

    hemc_num = Label( my_seeinvmenu,text="Litros" )
    hemc_num.grid(column=1, row=0)

    macc = Label(my_seeinvmenu, text="Fecha")
    macc.grid(column=2, row=0)

    btn_regresar = Button(my_seeinvmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=1)

def see_rep(root):
    my_seeinvmenu = Frame(root)
    my_seeinvmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Reporte Reproductivo del Ganado")

    c1= Label( my_seeinvmenu, text="Número de Servicio: ")
    c1.grid(column=0, row=0)

    c2 = Label( my_seeinvmenu,text="Número de Arete de la Hembra" )
    c2.grid(column=1, row=0)

    c3 = Label(my_seeinvmenu, text="Edad Hembra")
    c3.grid(column=2, row=0)

    c4 = Label(my_seeinvmenu, text="Número de Arete del Macho")
    c4.grid(column=3, row=0)

    c5 = Label(my_seeinvmenu, text="Edad Macho")
    c5.grid(column=4, row=0)

    c6 = Label(my_seeinvmenu, text="Fecha de Servicio")
    c6.grid(column=5, row=0)

    c7 = Label(my_seeinvmenu, text="Fértil")
    c7.grid(column=6, row=0)

    c8 = Label(my_seeinvmenu, text="Aborto")
    c8.grid(column=7, row=0)

    c9 = Label(my_seeinvmenu, text="Fecha de Parición")
    c9.grid(column=8, row=0)

    c10 = Label(my_seeinvmenu, text="Número de Arete de la Cría")
    c10.grid(column=9, row=0)



    btn_regresar = Button(my_seeinvmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=1)

def see_san(root):
    my_seeinvmenu = Frame(root)
    my_seeinvmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Reporte Sanitario del Ganado")

    c1 = Label(my_seeinvmenu, text="Número de Arete")
    c1.grid(column=0, row=0)

    c2 = Label(my_seeinvmenu, text="Fecha")
    c2.grid(column=1, row=0)

    c3 = Label(my_seeinvmenu, text="Signos Clínicos")
    c3.grid(column=2, row=0)

    c4 = Label(my_seeinvmenu, text="Peso / Condición Corporal")
    c4.grid(column=3, row=0)

    c5 = Label(my_seeinvmenu, text="Temperatura")
    c5.grid(column=4, row=0)

    c6 = Label(my_seeinvmenu, text="Frecuencia Cardiáca")
    c6.grid(column=5, row=0)

    c7 = Label(my_seeinvmenu, text="Tratamiento")
    c7.grid(column=6, row=0)

    c8 = Label(my_seeinvmenu, text="Diagnóstico")
    c8.grid(column=7, row=0)

    c9 = Label(my_seeinvmenu, text="Observaciones")
    c9.grid(column=8, row=0)

    btn_regresar = Button(my_seeinvmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=1)

def see_inf(root):
    my_seeinfmenu = Frame(root)
    my_seeinfmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Fichas Informativas del Ganado")

    num= Label( my_seeinfmenu, text="Número de Arete")
    num.grid(column=0, row=0)

    ficha_num = Label( my_seeinfmenu,text="Ficha del Bovino" )
    ficha_num.grid(column=1, row=0)

    btn_regresar = Button(my_seeinfmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=1)

def see_cos(root):
    my_seecosmenu = Frame(root)
    my_seecosmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Registro de Costos")

    c1 = Label(  my_seecosmenu, text="Cantidad")
    c1.grid(column=0, row=0)

    c2 = Label( my_seecosmenu,text="Descripción" )
    c2.grid(column=1, row=0)

    c3 = Label( my_seecosmenu,text="Fecha" )
    c3.grid(column=2, row=0)

    c4 = Label(my_seecosmenu, text="Costo Unitario")
    c4.grid(column=3, row=0)

    c5 = Label(my_seecosmenu, text="Costo Total")
    c5.grid(column=4, row=0)

    c6 = Label(my_seecosmenu, text="Tipo de Documento")
    c6.grid(column=5, row=0)

    btn_regresar = Button( my_seecosmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=1)

def see_venani(root):
    my_venmenu = Frame(root)
    my_venmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Registro de Ventas de Animales")

    c1 = Label(  my_venmenu, text="Categoría")
    c1.grid(column=0, row=0)

    c2 = Label( my_venmenu,text="Número de  Arete" )
    c2.grid(column=1, row=0)

    c3 = Label( my_venmenu,text="Fecha" )
    c3.grid(column=2, row=0)

    c4 = Label( my_venmenu, text="Tipo de Documento")
    c4.grid(column=3, row=0)

    c5 = Label( my_venmenu, text="Precio")
    c5.grid(column=4, row=0)

    btn_regresar = Button(  my_venmenu, text="Regresar", command=lambda: see_menuven(root))
    btn_regresar.grid(column=0, row=1)

def see_vencar(root):
    my_venmenu = Frame(root)
    my_venmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Registro de Ventas de Leche")

    c1 = Label(my_venmenu, text="Cantidad")
    c1.grid(column=0, row=0)

    c2 = Label(my_venmenu, text="Precio")
    c2.grid(column=1, row=0)

    c3 = Label(my_venmenu, text="Fecha")
    c3.grid(column=2, row=0)

    c4 = Label(my_venmenu, text="Tipo de Documento")
    c4.grid(column=3, row=0)

    btn_regresar = Button(my_venmenu, text="Regresar", command=lambda: see_menuven(root))
    btn_regresar.grid(column=0, row=1)

def see_venlec(root):
    my_venmenu = Frame(root)
    my_venmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Registro de Ventas de Leche")

    c1 = Label(my_venmenu, text="Cantidad")
    c1.grid(column=0, row=0)

    c2 = Label(my_venmenu, text="Descripción")
    c2.grid(column=1, row=0)

    c3 = Label(my_venmenu, text="Fecha")
    c3.grid(column=2, row=0)

    c4 = Label(my_venmenu, text="Tipo de Documento")
    c4.grid(column=3, row=0)

    btn_regresar = Button(my_venmenu, text="Regresar", command=lambda: see_menuven(root))
    btn_regresar.grid(column=0, row=1)



def see_menuven(root) :
    my_seemenu = Frame(root)
    my_seemenu.grid(column=0, row=0, sticky="nsew")
    root.title("Registro de Ventas")

    btn_f1 = Button(my_seemenu, text="Registro de Ventas de Animales", command=lambda: see_venani(root))
    btn_f1.grid(column=0, row=0)

    btn_f2= Button(my_seemenu, text="Registro de Ventas de Carne", command=lambda: see_vencar(root))
    btn_f2.grid(column=0, row=1)

    btn_f3 = Button(my_seemenu, text="Registro de Ventas de Leche", command=lambda: see_venlec(root))
    btn_f3.grid(column=0, row=2)

    btn_regresar = Button(my_seemenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=3)


def create_seemenu(root) :
    #message = "Visualizar Menu"
    #tkinter.messagebox.showinfo("Creando", message)

    my_seemenu = Frame(root)
    my_seemenu.grid(column=0, row=0, sticky="nsew")
    root.title("Visualizar")

    btn_seeinv = Button(my_seemenu, text="Inventario de Ganado", command=lambda: see_inv(root))
    btn_seeinv.grid(column=0, row=0)

    btn_seepro= Button(my_seemenu, text="Reporte Productivo", command=lambda: see_pro(root))
    btn_seepro.grid(column=0, row=1)

    btn_seerep = Button(my_seemenu, text="Reporte Reproductivo", command=lambda: see_rep(root))
    btn_seerep.grid(column=0, row=2)

    btn_seesan = Button(my_seemenu, text="Reporte Sanitario", command=lambda: see_san(root))
    btn_seesan.grid(column=0, row=3)

    btn_seeinf = Button(my_seemenu, text="Ficha de Bovino", command=lambda: see_inf(root))
    btn_seeinf.grid(column=0, row=4)

    btn_seecos = Button(my_seemenu, text="Registro de Costos", command=lambda: see_cos(root))
    btn_seecos.grid(column=0, row=5)

    btn_seeven = Button(my_seemenu, text="Registro de Ventas", command=lambda: see_menuven(root))
    btn_seeven.grid(column=0, row=6)

    btn_regresar = Button(my_seemenu, text="Regresar", command=lambda: create_menu(root))
    btn_regresar.grid(column=0, row=7)

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