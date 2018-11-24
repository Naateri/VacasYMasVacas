
class Sanitaria():
    def __init__(self, arete):
        self.nro_arete = arete
        self.fecha = 0
        self.signos = 0
        self.peso = 0
        self.temperatura = 0
        self.frecuencia = 0
        self.tratamiento = 0
        self.diagnostico = 0
        self.observaciones = 0

    def modify_sanitaria(self, num, sanitaria):
        if (num == 0):
            self.fecha = sanitaria
        elif (num == 1):
            self.signos = sanitaria
        elif (num == 2):
            self.peso = sanitaria
        elif (num == 3):
            self.temperatura = sanitaria
        elif (num == 4):
            self.frecuencia = sanitaria
        elif (num == 5):
            self.tratamiento = sanitaria
        elif (num == 6):
            self.diagnostico = sanitaria
        else:
            self.observaciones = sanitaria


class Productiva():
    def __init__(self, list):
        self.name = list[0]
        self.dni = list[1]
        self.email = list[2]
        self.fundo_name = list[3]
        self.password = list[4]
        # user_list.append(self)


class Reproductiva():
    def __init__(self, list):
        self.tipo = list[0]
        self.fecha = list[1]
        self.edad = list[2]
        self.numero = list[3]
        self.infertil = list[4]
        self.fertil = list[5]
        self.partosp = list[6]
        self.fechap = list[7]
        self.aborto = list[8]
        self.fechapari = list[9]
        self.aretecri = list[10]
        self.aretere = list[11]


class Peso():
    def __init__(self, fecha_ncto):
        self.fecha_nacimiento = fecha_ncto
        self.destete = 0
        self.anho = 0
        self.two_years = 0
        self.faenado = 0
    def modify_weight(self, num, peso): #num: 0->destete, 1->anho, 2->two_years, 3->faenado
        if (num == 0):
            self.destete = peso
        elif (num == 1):
            self.anho = peso
        elif (num == 2):
            self.two_years = peso
        else:
            self.faenado = peso

sanitaria_list = list();
productiva_list = list();
reproductiva_list = list();
peso_list = list(); #No_need

reg_sanitario = Sanitaria(['V724502','09/09/2017','ninguno1','35','45','120','leche fria','va a mejorar','la vaca esta bien'])
sanitaria_list.append(reg_sanitario)
<<<<<<< HEAD
reg_sanitario = Sanitaria(['V731502','09/09/2017','ninguno2','37','60','120','leche caliente','no va a mejorar','la vaca va a morir pronto'])
sanitaria_list.append(reg_sanitario)
reg_sanitario = Sanitaria(['V731501','09/09/2017','ninguno3','37','60','120','leche caliente','no va a mejorar','la vaca va a morir pronto'])
sanitaria_list.append(reg_sanitario)
reg_sanitario = Sanitaria(['V731502','09/09/2017','ninguno4','37','60','120','leche caliente','no va a mejorar','la vaca va a morir pronto'])
sanitaria_list.append(reg_sanitario)
reg_sanitario = Sanitaria(['V731503','09/09/2017','ninguno5','37','60','120','leche caliente','no va a mejorar','la vaca va a morir pronto'])
sanitaria_list.append(reg_sanitario)
=======
reg_sanitario = Sanitaria(['V731502','09/09/2017','ninguno','37','60','120','leche caliente','no va a mejorar','la vaca va a morir pronto'])
sanitaria_list.append(reg_sanitario)
>>>>>>> 0dfccf7689d4a3ca50b028284d61209099f3acf4
