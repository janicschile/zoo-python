from animales import *
class Leon(Animales):
    def __init__(self, nombre: str, genero: str, edad="desconocido", salud: int = 3, felicidad: int = 3, especie: str ="Leon"):
        super().__init__(nombre, edad, salud, felicidad, genero, especie)
        self.genero = genero

