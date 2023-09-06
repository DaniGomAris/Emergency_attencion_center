class Persona:
    def __init__(self, urgencia, nombre, descripcionDelProblema, numeroDeSolicitud):
        self.urgencia = urgencia
        self.nombre = nombre
        self.descripcionDelProblema = descripcionDelProblema
        self.numeroDeSolicitud = numeroDeSolicitud

    def imprimir_atributos(self):
        return (self.urgencia,self.nombre,self.descripcionDelProblema,self.numeroDeSolicitud)


class InformacionPersona:
    def __init__(self, persona: Persona):
        self.persona = persona
        self.prioridad_persona = []
        self.datos_persona = []
        self.datos_conjuntos = []
        self.datos_conjuntos = self.agregar_datos_persona()

    def agregar_datos_persona(self):
        self.prioridad_persona.append(self.persona.urgencia)

        self.datos_persona.append(self.persona.nombre)
        self.datos_persona.append(self.persona.descripcionDelProblema)
        self.datos_persona.append(self.persona.numeroDeSolicitud)

        self.datos_conjuntos.append(self.prioridad_persona)
        self.datos_conjuntos.append(self.datos_persona)

        return self.datos_conjuntos

    def imprimir_datos(self):
        return self.datos_conjuntos
