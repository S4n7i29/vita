from persona import Persona
from consultorio import Consultorio

class Paciente:
    def __init__(self, persona, obra_social, plan_obra_social, numero_afiliado, fecha_registro, consultorio):
        self.persona = persona
        self.obra_social = obra_social
        self.plan_obra_social = plan_obra_social
        self.numero_afiliado = numero_afiliado
        self.fecha_registro = fecha_registro
        self.consultorio_id = consultorio