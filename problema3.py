import math as mt

class Circulo:

    def __init__(self, radio):
        self.radio=radio
        self.area = print(mt.pi*(radio**2))

x=float(input("Ingrese el número del radio: "))
Circulo(x).area