from horario import Horario


class Curso:
    def __init__(self, nombre_curso: str, dias: str, horas: str):
        self.nombre_curso = nombre_curso
        # El horario nace y muere con el curso (composición)
        self.horario = Horario(dias, horas)

    def get_nombre_curso(self) -> str:
        return self.nombre_curso

    def set_nombre_curso(self, nombre_curso: str):
        self.nombre_curso = nombre_curso

    def get_horario(self) -> Horario:
        return self.horario

    def set_horario(self, horario: Horario):
        self.horario = horario

    def __str__(self):
        return f"Curso: {self.nombre_curso} | Horario: {self.horario}"
