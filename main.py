from clases.universidad import Universidad
from clases.profesor import Profesor
from clases.estudiante import Estudiante
from clases.curso import Curso

# Crear universidad
universidad = Universidad("Universidad del Salvador")

#Crear profesores
profesor_juan=Profesor("Juan Perez", 30,"Masculino", 20240811, "Matemáticas")
profesor_maria=Profesor("María Lopez", 35, "Femenino",20240812, "Física")
profesor_pedro=Profesor("Pedro Ramirez", 40, "Masculino",20240813, "Química")

#Crear cursos
curso_mat=Curso(profesor_juan.especialidad,"MAT101",profesor_juan.nombre)
curso_fisic=Curso(profesor_maria.especialidad,"FIS101",profesor_maria.nombre)
curso_quimic=Curso(profesor_pedro.especialidad,"MAT",profesor_pedro.nombre)

#Agregar los cursos en la U
universidad.agregar_curso(curso_mat)
universidad.agregar_curso(curso_fisic)
universidad.agregar_curso(curso_quimic)

#Crear estudiantes
estudiante_carlos=Estudiante("Carlos Perez",20,"Masculino", 202010101, "Ingeniería en Sistemas Informáticos")

#Imprimir información de la U, estudiante, profesor y curso
print(universidad)
print("---------")
print(estudiante_carlos)
print("---------")
print(profesor_juan)
print("---------")
print(curso_fisic)

#Crear nuevo curso de física
curso_nuevo_fisic = Curso("Física","FIS101","María Lopez")
universidad.agregar_curso(curso_nuevo_fisic)

#Imprimir los cursos
print(universidad)