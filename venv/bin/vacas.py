from fichas import Peso

vaca_list = list();

class Vaca():
    def __init__(self, list):
        self.nro_arete = list[0]
        self.especie = list[1]
        self.raza = list[2]
        self.sexo = list[3]
        self.fecha_ncto = list[4]
        self.nro_arete_madre = list[5]
        self.nro_arete_padre = list[6]
        self.ficha_peso = Peso(self.fecha_ncto)

    def modify_weight(self, another_list):
        self.ficha_peso.destete = another_list[0]
        self.ficha_peso.anho = another_list[1]
        self.ficha_peso.two_years = another_list[2]
        self.ficha_peso.faenado = another_list[3]