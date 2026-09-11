from datetime import date

from estudiante import Estudiante


class Reporte:
    # El método depende del objeto Estudiante temporalmente para funcionar
    def generar_reporte_academico(self, estudiante: Estudiante):
        print("=== REPORTE GENERADO ===")
        print(f"Fecha: {date.today()}")
        print(f"Datos del alumno: {estudiante.get_nombre()}")
        print(f"Edad: {estudiante.get_edad()}")
        print("========================")
