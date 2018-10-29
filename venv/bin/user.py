
user_list = list();

class Usuario():
    def __init__(self, list):
        self.name = list[0]
        self.dni = list[1]
        self.email = list[2]
        self.fundo_name = list[3]
        self.password = list[4]
        #user_list.append(self)

    def verificar_password(self, pw):
        if (self.password == pw):
            return True
        else:
            return False