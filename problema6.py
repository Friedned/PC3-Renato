while True:
    try:
        notas=input("Ingrese las notas separadas por comas: ")
        notas_separadas=notas.split(",")
        notas_int=[]
        for i in notas_separadas:
            notas_int.append(int(i))
        print(notas_int)
        break
    except:
        print("Los valores ingresados son inválidos, asegúrese de ingresar solo datos numéricos")
        continue
