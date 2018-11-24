from fichas import Peso
from fichas import Sanitaria

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
        self.ficha_sanitaria = Sanitaria(self.nro_arete)

    def modify_weight(self, another_list):
        self.ficha_peso.destete = another_list[0]
        self.ficha_peso.anho = another_list[1]
        self.ficha_peso.two_years = another_list[2]
        self.ficha_peso.faenado = another_list[3]

    def modify_sanitaria(self, listita):
        self.ficha_sanitaria.fecha = listita[0]
        self.ficha_sanitaria.signos = listita[1]
        self.ficha_sanitaria.peso = listita[2]
        self.ficha_sanitaria.temperatura = listita[3]
        self.ficha_sanitaria.frecuencia = listita[4]
        self.ficha_sanitaria.tratamiento = listita[5]
        self.ficha_sanitaria.diagnostico = listita[6]
        self.ficha_sanitaria.observaciones = listita[7]
