#from .profesor import Profesor

#Clase Estudiante hereda de persona
class Curso:
    # Inicio de atributos de persona y atributos adicionales
    def __init__(self,nombre,codigo, profesor):
        self.nombre=nombre
        self.codigo=codigo
        self.profesor =profesor

    def __str__(self):
        #Representación en cadena de estudiante
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}, Profesor: {self.profesor}"