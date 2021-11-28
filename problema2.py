def mayuscula(string):
    separado=string.split()
    lista=[]
    for i in separado:
        palabra=i.capitalize()
        lista.append(palabra)
    string=" ".join(lista)
    print(string)

x=input("Introduce una oración: ")
mayuscula(x)
