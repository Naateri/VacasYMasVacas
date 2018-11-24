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

    def set_sanitaria(self, list):
        self.fecha = list[0]
        self.signos = list[1]
        self.peso = list[2]
        self.temperatura = list[3]
        self.frecuencia = list[4]
        self.tratamiento = list[5]
        self.diagnostico = list[6]
        self.observaciones = list[7]


class Productiva():
    def __init__(self):
        self.diaria = 0
        self.semanal = 0
        self.mensual = 0
        self.anual = 0

    def set_productiva(self,value):
        self.diaria = value
        self.semanal = str(int(value)*7)
        self.mensual = str(int(value)*30)
        self.anual = str(int(value)*365)

class Rep_Productivo():
    def __init__(self, nro_arete):
        self.nro_arete = nro_arete
        self.litros = 0
        self.fecha = 0

    def modify_reporte(self, list):
        self.litros = list[0]
        self.fecha = list[1]

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

reg_sanitario = Sanitaria('V724502')
reg_sanitario.set_sanitaria(['09/09/2017','ninguno','35','45','120','leche fria','va a mejorar','la vaca esta bien'])
sanitaria_list.append(reg_sanitario)
reg_sanitario = Sanitaria('V731502')
reg_sanitario.set_sanitaria(['09/09/2017','ninguno','37','60','120','leche caliente','no va a mejorar','la vaca va a morir pronto'])
sanitaria_list.append(reg_sanitario)
reg_sanitario = Sanitaria('V731502')
reg_sanitario.set_sanitaria(['09/10/2017','ninguno','37','60','120','ni leche lo va a salvar','no va a mejorar','le doy un día de vida'])
sanitaria_list.append(reg_sanitario)

reg_productivo = Rep_Productivo('V724502')
reg_productivo.modify_reporte(['120', '02/02/2010'])
productiva_list.append(reg_productivo)
reg_productivo = Rep_Productivo('V7242502')
reg_productivo.modify_reporte(['69', '01/01/2014'])
productiva_list.append(reg_productivo)
reg_productivo = Rep_Productivo('V731502')
reg_productivo.modify_reporte(['81', '01/03/2014'])
productiva_list.append(reg_productivo)
