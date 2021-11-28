class RECTANGULO:
    def __init__(self, largo, ancho):
        self.area=print(f"El area del rectangulo es {largo*ancho}")

x=float(input("Ingrese el largo del rectangulo: "))
y=float(input("Ingrese el ancho del rectangulo: "))
RECTANGULO(x,y).area