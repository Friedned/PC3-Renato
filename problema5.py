class Alumno:
    def __init__(self, nombre, registro):
        self.display=print(f"""
        Nombre: {nombre}
        Número de registro: {registro}
        """)
        self.setAge=int(input(f"Ingrese la edad de {nombre}: "))
        self.setNota=(input(f"Ingrese las notas de {nombre} separadas por comas: "))

x=input("Ingrese el nombre del estudiante: ")
y=int(input(f"Ingrese el numero de registro del estudiante {x}: "))
alumno1=Alumno(x, y)
