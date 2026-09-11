from profesor import Profesor
from estudiante import Estudiante
from curso import Curso
from universidad import Universidad
from reporte import Reporte


def main():
    prof1 = Profesor("Carlos Mendoza", 45)
    prof2 = Profesor("Ana Suarez", 38)

    est1 = Estudiante("Renzo Geomar Mamani Quispe", 19)
    est2 = Estudiante("Lucia Fernandez", 20)
    est3 = Estudiante("Mario Vargas", 21)

    curso1 = Curso("Ingeniería de Software", "Lunes y Miércoles", "10:00 - 12:00")
    curso2 = Curso("Base de Datos", "Martes y Jueves", "14:00 - 16:00")

    unsa = Universidad("UNSA")
    unsa.agregar_curso(curso1)
    unsa.agregar_curso(curso2)

    reporte = Reporte()
    reporte.generar_reporte_academico(est1)


if __name__ == "__main__":
    main()
