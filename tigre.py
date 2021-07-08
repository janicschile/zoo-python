from animales import *
class Tigre(Animales):
    def __init__(self, nombre: str, genero: str, edad="desconocido", salud: int = 4, felicidad: int = 5, especie: str = "Tigre"):
        super().__init__(nombre, edad, salud, felicidad, genero, especie)
        self.genero = genero