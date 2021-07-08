
class Animales():
    def __init__(self, nombre: str, edad, salud: int, felicidad: int, genero: str, especie: str):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
        self.genero = genero
        self.especie = especie
    def mostrarInformacion(self):
        if self.genero == "Hembra":
            if self.especie == "Leon":
                self.especie = "Leona"
            if self.especie == "Oso":
                self.especie = "Osa"
            if self.especie == "Tigre":
                self.especie = "Tigresa"
            s = f"Esta {self.especie} se llama {self.nombre}, su nivel de salud es {self.salud}/10 y su nivel de felicidad es {self.felicidad}/10"
        else:
            s = f"Este {self.especie} se llama {self.nombre}, su nivel de salud es {self.salud}/10 y su nivel de felicidad es {self.felicidad}/10"
        return s
    def alimentarAnimales(self):
        self.salud += 10
        self.felicidad += 10