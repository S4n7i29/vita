from paciente import Paciente
from consultorio import Consultorio

class Consulta:
    def __init__(self, paciente, fecha, consultorio, diagnostico, tratamiento):
        self.paciente = paciente
        self.fecha = fecha
        self.consultorio = consultorio
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento