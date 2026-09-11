class Horario:
    def __init__(self, dias: str, horas: str):
        self.dias = dias
        self.horas = horas

    def get_dias(self) -> str:
        return self.dias

    def set_dias(self, dias: str):
        self.dias = dias

    def get_horas(self) -> str:
        return self.horas

    def set_horas(self, horas: str):
        self.horas = horas

    def __str__(self):
        return f"{self.dias} a las {self.horas}"
