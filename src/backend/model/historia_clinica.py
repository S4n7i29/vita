from consulta import Consulta

class HistoriaClinica:
    def __init__(self):
        self.consultas = []

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)