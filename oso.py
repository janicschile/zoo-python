from animales import *
class Oso(Animales):
    def __init__(self, nombre: str, genero: str, edad="desconocido", salud: int = 4, felicidad: int = 20, especie: str = "Oso"):
        super().__init__(nombre, edad, salud, felicidad, genero, especie)
        self.genero = genero