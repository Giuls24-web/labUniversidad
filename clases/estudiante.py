from .persona import Persona 

#Clase Estudiante hereda de persona
class Estudiante(Persona):
    # Inicio de atributos de persona y atributos adicionales
    def __init__(self,nombre,edad,sexo,carnet,carrera):
        super().__init__(nombre,edad,sexo)
        self.carnet=carnet
        self.carrera=carrera
    
    def __str__(self):
        #Representación en cadena de estudiante
        return f"{super().__str__()}, Carnet: {self.carnet}, Carrera: {self.carrera}"