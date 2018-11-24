from tkinter import *
import tkinter.messagebox
from user import Usuario
import duenho
import sys
import vacas
from vacas import Vaca
import fichas

vaca_list = list() #vacas
test_vaca = Vaca(['V724502','Vaca','Holstein','Hembra','09/09/2016','V721302','V721314'])
test_vaca1 = Vaca(['V722502','Vaca','Holstein','Hembra','09/09/1940','V721702','V121314'])
test_vaca2 = Vaca(['V731502','Toro','Holstein','Hembra','07/12/1978','V721702','V121314'])
test_vaca3 = Vaca(['V789718','Toro','Holstein','Macho','01/10/1913','V721749','V121589'])
test_vaca4 = Vaca(['V145574','Vaca','Holstein','Macho','02/07/1950','V721705','V121485'])

vaca_list.append(test_vaca)
vaca_list.append(test_vaca1)
vaca_list.append(test_vaca2)
vaca_list.append(test_vaca3)
vaca_list.append(test_vaca4)


def buscar_vaca(id): #returns index
    for i in range( len(vaca_list)):
        if (vaca_list[i].nro_arete == id):
            return i

def buscar_vaca_retvaca(id):
    for vaca in vaca_list:
        if (vaca.nro_arete == id):
            return vaca

def get_machos():
    machos = 0
    for vaca in vaca_list:
        if (vaca.sexo == 'Macho'):
            machos += 1

    return str(machos)

def get_hembras():
    hembras = 0
    for vaca in vaca_list:
        if (vaca.sexo == 'Hembra'):
            hembras += 1

    return str(hembras)

def mod_pesos(id_vaca, le_list):
    vaquita = buscar_vaca(id_vaca)
    #vacaa = vaca_list[vaquita]
    vaca_list[vaquita].modify_weight(le_list)
    print ('vaquita peso destete: ' + vaca_list[vaquita].ficha_peso.destete)

def create_vaca(l1, root): #root is tk()
    la_vaca = Vaca(l1)
    vaca_list.append(la_vaca)
    tkinter.messagebox.showinfo(str(l1[0]), "Vaca creada")
    print('Vaca arete:' + vaca_list[len(vaca_list) - 1].nro_arete + ', especie: ' + la_vaca.especie)

def raise_frame(frame):
    frame.tkraise()

def add_info(root):
    add_info = Frame(root)
    add_info.grid(column=0, row=0, sticky="nsew")
    root.title("Crear bovino")

    arete = Label(add_info, text="Número de arete: ")
    arete.grid(column = 0, row = 0)

    arete_input = Entry(add_info)
    arete_input.grid(column=1, row=0)

    especie = Label(add_info, text="Especie: ")
    especie.grid(column=0, row=1)

    especie_input = Entry(add_info)
    especie_input.grid(column=1, row=1)

    raza = Label(add_info, text="Raza: ")
    raza.grid(column=0, row=2)

    raza_input = Entry(add_info)
    raza_input.grid(column=1, row=2)

    sexo = Label(add_info, text="Sexo: ")
    sexo.grid(column=0, row=3)

    sexo_input = Entry(add_info)
    sexo_input.grid(column=1, row=3)

    fecha = Label(add_info, text="Fecha de nacimiento: ")
    fecha.grid(column=0, row=4)

    fecha_input = Entry(add_info)
    fecha_input.grid(column=1, row=4)

    aretema = Label(add_info, text="Nro de arete de la madre: ")
    aretema.grid(column=0, row=5)

    aretema_input = Entry(add_info)
    aretema_input.grid(column=1, row=5)

    aretepa = Label(add_info, text="Nro de arete del padre: ")
    aretepa.grid(column=0, row=6)

    aretepa_input = Entry(add_info)
    aretepa_input.grid(column=1, row=6)

    btn_confirm = Button(add_info, text="Crear", command=lambda: create_vaca(
        [arete_input.get(), especie_input.get(), raza_input.get(), sexo_input.get(),
         fecha_input.get(), aretema_input.get(), aretepa_input.get()], root))
    btn_confirm.grid(column=0, row=7)

    btn_regresar = Button(add_info, text="Regresar", command=lambda: create_addmenu(root))
    btn_regresar.grid(column=1, row=7)

    raise_frame(add_info)

def add_peso(root):
    add_peso = Frame(root)
    add_peso.grid(column=0, row=0, sticky="nsew")
    root.title("Crear bovino")

    nacimiento = Label(add_peso, text="Id vaca: ")
    nacimiento.grid(column=0, row=0)

    nacimiento_input = Entry(add_peso)
    nacimiento_input.grid(column=1, row=0)

    destete = Label(add_peso, text="Destete: ")
    destete.grid(column=0, row=1)

    destete_input = Entry(add_peso)
    destete_input.grid(column=1, row=1)

    anho = Label(add_peso, text="Año: ")
    anho.grid(column=0, row=2)

    anho_input = Entry(add_peso)
    anho_input.grid(column=1, row=2)

    dos = Label(add_peso, text="Dos años: ")
    dos.grid(column=0, row=3)

    dos_input = Entry(add_peso)
    dos_input.grid(column=1, row=3)

    faenado = Label(add_peso, text="Faenado: ")
    faenado.grid(column=0, row=4)

    faenado_input = Entry(add_peso, show="*")
    faenado_input.grid(column=1, row=4)

    btn_regresar = Button(add_peso, text="Regresar", command=lambda: create_addmenu(root))
    btn_regresar.grid(column=0, row=6)

    btn_crear = Button(add_peso, text='Agregar Peso', command=lambda: mod_pesos(nacimiento_input.get(), [destete_input.get(), anho_input.get(),
                                                                                                         dos_input.get(), faenado_input.get()]))
    btn_crear.grid(column=1,row=6)

    raise_frame(add_peso)


def add_sanitaria(root):
    add_sanitaria = Frame(root)
    add_sanitaria.grid(column=0, row=0, sticky="nsew")
    root.title("Añadir ficha sanitaria")
    arete = Label(add_sanitaria, text="Número de arete: ")
    arete.grid(column=0, row=0)

    arete_input = Entry(add_sanitaria)
    arete_input.grid(column=1, row=0)

    fecha = Label(add_sanitaria, text="Fecha: ")
    fecha.grid(column=0, row=1)

    fecha_input = Entry(add_sanitaria)
    fecha_input.grid(column=1, row=1)

    signos = Label(add_sanitaria, text="Signos clínicos: ")
    signos.grid(column=0, row=2)

    signos_input = Entry(add_sanitaria)
    signos_input.grid(column=1, row=2)

    peso = Label(add_sanitaria, text="Peso /condición corporal : ")
    peso.grid(column=0, row=3)

    peso_input = Entry(add_sanitaria)
    peso_input.grid(column=1, row=3)

    temp = Label(add_sanitaria, text="Temperatura: ")
    temp.grid(column=0, row=4)

    temp_input = Entry(add_sanitaria)
    temp_input.grid(column=1, row=4)

    frecuencia = Label(add_sanitaria, text="Frecuencia cardiáca : ")
    frecuencia.grid(column=0, row=5)

    frecuencia_input = Entry(add_sanitaria)
    frecuencia_input.grid(column=1, row=5)

    tratamiento = Label(add_sanitaria, text="Tratamiento: ")
    tratamiento.grid(column=0, row=6)

    tratamiento_input = Entry(add_sanitaria)
    tratamiento_input.grid(column=1, row=6)

    diagnostico = Label(add_sanitaria, text="Diagnóstico: ")
    diagnostico.grid(column=0, row=7)

    diagnostico_input = Entry(add_sanitaria)
    diagnostico_input.grid(column=1, row=7)

    observaciones = Label(add_sanitaria, text="Observaciones: ")
    observaciones.grid(column=0, row=8)

    observaciones_input = Entry(add_sanitaria)
    observaciones_input.grid(column=1, row=8)

    # btn_confirm = Button(add_sanitaria, text="Confirmar", command=lambda: create_user(
    #    [arete_input.get(), fecha_input.get(), signos_input.get(), peso_input.get(),
    #     temp_input.get(), aretema_input.get()], root))
    # btn_confirm.grid(column=1, row=7)

    btn_regresar = Button(add_sanitaria, text="Regresar", command=lambda: create_menu(root))
    btn_regresar.grid(column=0, row=9)

    raise_frame(add_sanitaria)

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

    hemc= Label( my_seeinvmenu, text="Número de Hembras: ")
    hemc.grid(column=0, row=0)

    hemc_num = Label( my_seeinvmenu,text=get_hembras())
    hemc_num.grid(column=1, row=0)

    macc = Label(my_seeinvmenu, text="Número de Machos: ")
    macc.grid(column=0, row=1)

    macc_num = Label(my_seeinvmenu, text=get_machos())
    macc_num.grid(column=1, row=1)

    hem = Label(my_seeinvmenu, text="Número de Crías Hembras: ")
    hem.grid(column=0, row=2)

    hem_num = Label(my_seeinvmenu, text="No hay forma de saber por nuestra incompetencia")
    hem_num.grid(column=1, row=2)

    mac = Label(my_seeinvmenu, text="Número de Crías Machos: ")
    mac.grid(column=0, row=3)

    mac_num = Label(my_seeinvmenu, text="No hay forma de saber por nuestra incompetencia")
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

def see_san(id, root):
    my_seeinvmenu = Frame(root)
    my_seeinvmenu.grid(column=0, row=0, sticky="nsew")
    root.title("Reporte Sanitario del Ganado")

    my_vaca = buscar_vaca_retvaca(id)

    i=0
    j=1
    for Sanitaria in fichas.sanitaria_list:

        if id == Sanitaria.nro_arete:
            c0 = Label(my_seeinvmenu, text="Ficha "+str(j))
            c0.grid(column=0, row=i)

            i = i+1
            c2 = Label(my_seeinvmenu, text="Fecha")
            c2.grid(column=0, row=i)
            c12 = Label(my_seeinvmenu, text=Sanitaria.fecha)
            c12.grid(column=1, row=i)
            i = i+1
            c3 = Label(my_seeinvmenu, text="Signos Clínicos")
            c3.grid(column=0, row=i)
            c13 = Label(my_seeinvmenu, text=Sanitaria.signos)
            c13.grid(column=1, row=i)
            i = i+1
            c4 = Label(my_seeinvmenu, text="Peso / Condición Corporal")
            c4.grid(column=0, row=i)
            c14 = Label(my_seeinvmenu, text=Sanitaria.peso)
            c14.grid(column=1, row=i)
            i = i + 1
            c5 = Label(my_seeinvmenu, text="Temperatura")
            c5.grid(column=0, row=i)
            c15 = Label(my_seeinvmenu, text=Sanitaria.temperatura)
            c15.grid(column=1, row=i)
            i = i + 1
            c6 = Label(my_seeinvmenu, text="Frecuencia Cardiáca")
            c6.grid(column=0, row=i)
            c16 = Label(my_seeinvmenu, text=Sanitaria.temperatura)
            c16.grid(column=1, row=i)
            i = i + 1
            c7 = Label(my_seeinvmenu, text="Tratamiento")
            c7.grid(column=0, row=i)
            c17 = Label(my_seeinvmenu, text=Sanitaria.tratamiento)
            c17.grid(column=1, row=i)
            i = i + 1
            c8 = Label(my_seeinvmenu, text="Diagnóstico")
            c8.grid(column=0, row=i)
            c18 = Label(my_seeinvmenu, text=Sanitaria.diagnostico)
            c18.grid(column=1, row=i)
            i = i + 1
            c9 = Label(my_seeinvmenu, text="Observaciones")
            c9.grid(column=0, row=i)
            c19 = Label(my_seeinvmenu, text=Sanitaria.observaciones)
            c19.grid(column=1, row=i)
            i = i+1
            j = j+1

    btn_regresar = Button(my_seeinvmenu, text="Regresar", command=lambda: create_seemenu(root))
    btn_regresar.grid(column=0, row=i)

def see_sanitario(root):
    my_seeinvmenu = Frame(root)
    my_seeinvmenu.grid(column=0, row=0, sticky="nsew")
    user = Label(my_seeinvmenu, text="Usuario: ", relief=RAISED)

    user.grid(column=0, row=0)

    user_input = Entry(my_seeinvmenu)
    user_input.grid(column=1, row=0)
    login_button = Button(my_seeinvmenu, text="Ingresar", command=lambda: see_san(user_input.get(), root))
    # login_button.pack()
    login_button.grid(column=0, row=2)

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

    btn_seesan = Button(my_seemenu, text="Reporte Sanitarioo", command=lambda: see_sanitario(root))
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

def create_infomenu(root, usuario) :
    #message = "Informacion Menu"
    #tkinter.messagebox.showinfo("Creando", message)

    infomenu = Frame(root)
    infomenu.grid(column=0,row=0,sticky="nsew")
    root.title("Visualizar informacion")

    btn_ver_duenho = Button(infomenu, text="Visualizar datos del duenho", command=lambda: duenho.visualizar_datos_duenho(root,usuario))
    btn_ver_duenho.grid(column=0, row=0)

    btn_ver_fundo = Button(infomenu, text="Visualizar datos del fundo", command=lambda: duenho.visualizar_datos_fundo(root,usuario))
    btn_ver_fundo.grid(column=0, row=1)

    btn_volver = Button(infomenu, text="Regresar", command=lambda: create_menu(root,usuario))
    btn_volver.grid(column=0,row=2)

    infomenu.tkraise()


def exit(root) :
    message = "Menu"
    tkinter.messagebox.showinfo("Saliendo", message)
    sys.exit()

def create_menu(root, usuario = 0):

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

    btn_info = Button(my_menu, text="Información", command = lambda:create_infomenu(root, usuario))
    btn_info.grid(column = 0, row = 4)

    btn_exit= Button(my_menu, text="Cerrar", command = lambda:exit(root))
    btn_exit.grid(column = 0, row = 5)
    raise_frame(my_menu)