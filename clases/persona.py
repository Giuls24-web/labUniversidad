class Persona:
    def __init__(self,nombre,edad,sexo):
        #Atributos
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def __str__(self):
        #Representación de la cadena
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"
    