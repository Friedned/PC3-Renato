
def long(x):
    separado=x.split(" ")
    ultima=separado[-1]
    a=len(ultima)
    print(f"La longitud de {ultima} es {a}")

oracion=input("Escriba una oración: ")
long(oracion)
