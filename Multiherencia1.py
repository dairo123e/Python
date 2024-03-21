class Persona:
    total_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

class Estudiante(Persona):
    total_estudiantes = 0

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

class Docente(Persona):
    total_docentes = 0

    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento
        Docente.total_docentes += 1

    def dar_clase(self, asignatura):
        print(f"El docente {self.nombre} está dando clase de {asignatura} en la carrera de {self.departamento}.")


def ingresar_estudiantes():
    estudiantes = []
    continuar = True
    while continuar:
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        carrera = input("Ingrese la carrera del estudiante: ")
        estudiante = Estudiante(nombre, edad, carrera)
        estudiantes.append(estudiante)
        respuesta = input("¿Desea ingresar otro estudiante? (s/n): ")
        if respuesta.lower() != 's':
            continuar = False
    return estudiantes

lista_estudiantes = ingresar_estudiantes()

for estudiante in lista_estudiantes:
    estudiante.saludar()

docente1 = Docente("Diego Fernando", 45, "Programacion II")
docente1.saludar()
docente1.dar_clase("Ingenieria")

print(f"Total de personas: {Persona.total_personas}")
print(f"Total de estudiantes: {Estudiante.total_estudiantes}")
print(f"Total de docentes: {Docente.total_docentes}")
