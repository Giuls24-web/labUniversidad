from .persona import Persona 

#Clase Profesor hereda de persona
class Profesor (Persona):
    # Inicio de atributos de persona y atributos adicionales
    def __init__(self,nombre,edad,sexo,codigo,especialidad):
        super().__init__(nombre,edad,sexo)
        self.codigo=codigo
        self.especialidad=especialidad
    
    def __str__(self):
        #Representación en cadena de profesor
        return f"{super().__str__}, Código: {self.codigo}, Especialidad: {self.especialidad}"