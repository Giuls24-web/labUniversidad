from .curso import Curso

class Universidad:
    
    def __init__(self, nombre):
        #Atributos
        self.nombre=nombre
        self.cursos=[]
    
    def agregar_curso(self, curso):
        #método para agregar curso de la U
        self.cursos.append(curso)    
    
    def __str__(self):
        #Representacion en cadena de la U y sus cursos
        cursos_str ="\n".join([str(curso) for curso in self.cursos])
        return f"Universidad: {self.nombre}\n {cursos_str} "