from tkinter import *
import tkinter.messagebox
from user import Usuario

import duenho

import menu


user_list = list() #usuarios

test_user = Usuario(['Renato Postigo', '5678', 'renato.postigo@ucsp.edu.pe',
                     'Vacas y guano', '1234'])

user_list.append(test_user)

def raise_frame(frame):
    frame.tkraise()

def check_password(pw1, pw2):
    if (pw1 == pw2):
        return True
    else:
        return False

def create_user(l1, root): #root is tk()

    if (not check_password(l1[4], l1[5])):
        tkinter.messagebox.showinfo("Revise passwords", "Las passwords no coinciden, vuelva a intentarlo.")
        return 0
    le_user = Usuario(l1)
    user_list.append(le_user)
    tkinter.messagebox.showinfo(str(l1[0]), "Cuenta creada.")
    create_login(root)


def checking_login(username, password, root):
    """
    if (password == ""):
        new_pass = "Ingresa algo pe."
    else:
        new_pass = password
    if (username == ""):
        new_user = "No seas tonto."
    else:
        new_user = username
    tkinter.messagebox.showinfo("Hola manito", "Has sido jakeado, tu usuario es " + new_user
     + ", tu password es: " + new_pass)
     """

def checking_login(username, password,root):
    for usuario in user_list:
        if usuario.dni == username:
            if usuario.password == password:
                message = "Bienvenido/a " + usuario.name
                temp_user = usuario
            else:
                message = "Password equivocada"
            break
        else:
            message = "Has sido hackeado, tu password es " + password
    tkinter.messagebox.showinfo("Login", message)
    duenho.visualizar_datos_duenho(root, temp_user)
    #duenho.visualizar_datos_fundo(root, temp_user)


    #tkinter.messagebox.showinfo("Login", message)
    menu.create_menu(root)


def create_account(root):
    #my_login.destroy()
    #account_creation = Tk()
    account_creation = Frame(root)
    account_creation.grid(column=0, row=0, sticky="nsew")
    root.title("Crear cuenta")

    nombre = Label(account_creation, text="Nombre: ")
    nombre.grid(column = 0, row = 0)

    nombre_input = Entry(account_creation)
    nombre_input.grid(column=1, row=0)

    dni = Label(account_creation, text="DNI: ")
    dni.grid(column=0, row=1)

    dni_input = Entry(account_creation)
    dni_input.grid(column=1, row=1)

    email = Label(account_creation, text="Correo Electronico: ")
    email.grid(column=0, row=2)

    email_input = Entry(account_creation)
    email_input.grid(column=1, row=2)

    fundo = Label(account_creation, text="Nombre del fundo: ")
    fundo.grid(column=0, row=3)

    fundo_input = Entry(account_creation)
    fundo_input.grid(column=1, row=3)

    password = Label(account_creation, text="Password: ")
    password.grid(column=0, row=4)

    password_input = Entry(account_creation, show="*")
    password_input.grid(column=1, row=4)

    pw_confirm = Label(account_creation, text="Confirmar password: ")
    pw_confirm.grid(column=0, row=5)

    pw_confirm_input = Entry(account_creation, show="*")
    pw_confirm_input.grid(column=1, row=5)

    btn_confirm = Button(account_creation, text="Confirmar", command=lambda:create_user(
        [nombre_input.get(), dni_input.get(), email_input.get(), fundo_input.get(),
                      password_input.get(), pw_confirm_input.get()], root))
    btn_confirm.grid(column=1,row=7)

    btn_regresar = Button(account_creation, text="Regresar", command=lambda:create_login(root))
    btn_regresar.grid(column=0, row=7)

    raise_frame(account_creation)



def create_login(root):

    my_login = Frame(root)
    my_login.grid(column=0, row=0, sticky="nsew")
    root.title("Iniciar Sesion")

    path = "/home/nateri/PycharmProjects/VacasYMasVacas/venv/images/vaquitas.jpg"
    img = PhotoImage(path)
    my_canvas = Canvas(root, bg="blue", height=300, width=300)
    background_label = Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_canvas.place()

    #usuario_text = StringVar()
    user = Label(my_login, text="Usuario: ", relief=RAISED)
    #usuario_text.set("Usuario: ")
    #user.pack(side = LEFT)
    user.grid(column = 0, row = 0)

    user_input = Entry(my_login)
    #user_input.pack(side = RIGHT)
    user_input.grid(column = 1, row = 0)

    #password_text = StringVar()
    password = Label(my_login, text="Password: ", relief=RAISED)
    #password_text.set("Password: ")
    #password.pack(side = LEFT)
    password.grid(column = 0, row = 1)

    password_input = Entry(my_login, show="*")
    #password_input.pack(side = RIGHT)
    password_input.grid(column = 1, row = 1)

    #login_button = Button(my_login, text="Ingresar", command = lambda:checking_login(user_input.get(),

    login_button = Button(my_login, text="Ingresar", command = lambda:checking_login(user_input.get(),password_input.get(),root))

    #login_button.pack()
    login_button.grid(column = 0, row = 2)

    register_button = Button(my_login, text="Crear cuenta", command = lambda:create_account(root))
    register_button.grid(column = 0, row = 3)

    raise_frame(my_login)
#top = Tk()
#top.mainloop()