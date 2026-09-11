from typing import List

from curso import Curso


class Universidad:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cursos: List[Curso] = []

    def agregar_curso(self, curso: Curso):
        self.cursos.append(curso)

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_cursos(self) -> List[Curso]:
        return self.cursos

    def set_cursos(self, cursos: List[Curso]):
        self.cursos = cursos

    def __str__(self):
        return f"Universidad: {self.nombre} | Total cursos: {len(self.cursos)}"
