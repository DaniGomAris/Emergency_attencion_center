class Persona:
    def __init__(self, urgencia, nombre, descripcionDelProblema, numeroDeSolicitud):
        self.numeroDeSolicitud = numeroDeSolicitud
        self.nombre = nombre
        self.descripcionDelProblema = descripcionDelProblema
        self.urgencia = urgencia

class InformacionPersona:
    def __init__(self, persona: Persona):
        self.persona = persona
        self.datos_persona = []
        self.datos_persona = self.agregar_datos_persona()

    def agregar_datos_persona(self):
        self.datos_persona.append(self.persona.numeroDeSolicitud)
        self.datos_persona.append(self.persona.nombre)
        self.datos_persona.append(self.persona.descripcionDelProblema)
        self.datos_persona.append(self.persona.urgencia)
        return self.datos_persona