from persona import Persona


class Profesor(Persona):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)

    def __str__(self):
        return f"[Profesor] {super().__str__()}"
