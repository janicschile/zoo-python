import time
import os
from random import uniform
from animales import Animales
from leon import *
from oso import *
from tigre import *


def screen_clear():
    os.system("cls")


class Zoo:
    def __init__(self, zoo_nombre):
        self.animales = []
        self.nombre = zoo_nombre

    def add_Leon(self, nombre, genero):
        self.animales.append(Leon(nombre, genero))

    def add_Tigre(self, nombre, genero):
        self.animales.append(Tigre(nombre, genero))

    def add_Oso(self, nombre, genero):
        self.animales.append(Oso(nombre, genero))

    def informacionDelZoo(self):
        print("---------------------------------------", self.nombre, "---------------------------------------")
        for Animales in self.animales:
            print(Animales.mostrarInformacion())

def cargaInicial(zoo1):
    zoo1.add_Leon("Nala", "Hembra")
    zoo1.add_Leon("Simba", "Macho")
    zoo1.add_Tigre("Rajah", "Macho")
    zoo1.add_Tigre("Shere Khan", "Macho")
    zoo1.add_Oso("Peresoza", "Hembra")

def opcionUno(zoo1):
    screen_clear()
    zoo1.informacionDelZoo()
    print("")
    os.system("Pause")
    return menuSistema(zoo1)


def menuSistema(zoo1):
    screen_clear()    #╚ ╔ ╗╝ ║ ╩ ╦
    print("\n                 CODING  ZOO  1.0\n        ═══╦══════════════════════════╦═══\n           ║     MENU   PRINCIPAL     ║\n           ╚══════════════════════════╝\n")
    print(f"         \n")
    print("1 >> Informacion General              Recibir Animal << 2")
    print("3 >> Alimentar Animal                          SALIR << 4")
    opcion = int(input("\n             Ingrese Opcion: "))
    print(opcion)

    if opcion == 1 : opcionUno(zoo1)

    if opcion == 2: 
        print("\n Opcion aun sin implementar, favor de utilizar plataforma Web..."); time.sleep(3); return menuSistema(zoo1)
        #opcionDos()

    if opcion == 3 : 
        print("\n Opcion aun sin implementar, favor de utilizar plataforma Web..."); time.sleep(3); return menuSistema(zoo1)
        #opcionTres()

    if opcion == 4 :
        screen_clear()
        #print(bdUsuarios)
        #print(dataCliente.balance)
        #guardarArchivoClientes(bdUsuarios)
        #os.system("Pause")


zoo1 = Zoo("Coding ZOO")
cargaInicial(zoo1)
menuSistema(zoo1)



