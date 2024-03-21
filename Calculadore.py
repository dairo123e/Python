import tkinter as tk
from tkinter import messagebox

class Persona:
    total_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1

    def saludar(self):
        ventana_saludo = tk.Toplevel()
        ventana_saludo.title("Saludo")
        mensaje = tk.Label(ventana_saludo, text=f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años.", font=('Impact', 12))
        mensaje.pack(padx=10, pady=10)

class Estudiante(Persona):
    total_estudiantes = 0

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1

    def imprimir_informacion(self):
        ventana_info = tk.Toplevel()
        ventana_info.title("Información Estudiante")
        mensaje = tk.Label(ventana_info, text=f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}", font=('Impact', 12))
        mensaje.pack(padx=10, pady=10)

class Docente(Persona):
    total_docentes = 0

    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.departamento = departamento
        Docente.total_docentes += 1

    def dar_clase(self, asignatura):
        ventana_clase = tk.Toplevel()
        ventana_clase.title("Clase")
        mensaje = tk.Label(ventana_clase, text=f"El docente {self.nombre} está dando clase de {asignatura} en el departamento de {self.departamento}.", font=('Impact', 12))
        mensaje.pack(padx=10, pady=10)

def ingresar_persona():
    nombre = nombre_entry.get()
    edad = int(edad_entry.get())
    carrera_departamento = carrera_departamento_entry.get()
    tipo_persona = persona_type.get()

    if tipo_persona == "Estudiante":
        persona = Estudiante(nombre, edad, carrera_departamento)
    else:
        persona = Docente(nombre, edad, carrera_departamento)
    
    persona.saludar()

# Interfaz gráfica
root = tk.Tk()
root.title("Registro de Personas")

tk.Label(root, text="Nombre:", font=('Impact', 12)).grid(row=0, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

tk.Label(root, text="Edad:", font=('Impact', 12)).grid(row=1, column=0)
edad_entry = tk.Entry(root)
edad_entry.grid(row=1, column=1)

tk.Label(root, text="Carrera/Departamento:", font=('Impact', 12)).grid(row=2, column=0)
carrera_departamento_entry = tk.Entry(root)
carrera_departamento_entry.grid(row=2, column=1)

tk.Label(root, text="Tipo de Persona:", font=('Impact', 12)).grid(row=3, column=0)
persona_type = tk.StringVar(root)
persona_type.set("Estudiante")
personas_dropdown = tk.OptionMenu(root, persona_type, "Estudiante", "Docente")
personas_dropdown.grid(row=3, column=1)

ingresar_button = tk.Button(root, text="Saludar", command=ingresar_persona, font=('Impact', 12))
ingresar_button.grid(row=4, column=0, columnspan=2)

root.mainloop()

