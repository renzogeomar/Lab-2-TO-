from profesor import Profesor
from estudiante import Estudiante
from curso import Curso
from universidad import Universidad
from reporte import Reporte


def main():
    # Crear 2 profesores
    prof1 = Profesor("Carlos Mendoza", 45)
    prof2 = Profesor("Ana Suarez", 38)

    # Crear 3 estudiantes
    est1 = Estudiante("Renzo Geomar Mamani Quispe", 19)
    est2 = Estudiante("Lucia Fernandez", 20)
    est3 = Estudiante("Mario Vargas", 21)

    # Crear 2 cursos (el horario se crea por composición dentro del curso)
    curso1 = Curso("Ingeniería de Software", "Lunes y Miércoles", "10:00 - 12:00")
    curso2 = Curso("Base de Datos", "Martes y Jueves", "14:00 - 16:00")

    # Crear universidad y agregar cursos (Agregación)
    unsa = Universidad("UNSA")
    unsa.agregar_curso(curso1)
    unsa.agregar_curso(curso2)

    # Generar reporte de un estudiante (Dependencia)
    reporte = Reporte()
    reporte.generar_reporte_academico(est1)


if __name__ == "__main__":
    main()
