class PriorityQueue:
    def __init__(self):
        self.cola = []

    def enqueue(self, informacion):
        self.cola.append(informacion)

    def dequeue(self):
        if self.cola:
            self.cola.pop(0)

    def top(self):
        return self.cola[0]

    def tamaño(self):
        return len(self.cola)
    
    def hayar_mayor_valor(self):
        mayor = -1
        posicion = 0
        posicion_del_mayor = 1
        for informacion_persona in self.cola:
            if informacion_persona.persona.urgencia > mayor:
                mayor = informacion_persona.persona.urgencia
                posicion_del_mayor = posicion

            posicion += 1
        return posicion_del_mayor

    def imprimir_cola(self):
        for informacion_persona in self.cola:
            print(f" El orden de prioridad es: : {informacion_persona.datos_conjuntos}")

    def llevar_a_primera_posicion(self):
        cola_auxiliar = PriorityQueue()
        while self.cola != []:
            posicion_mayor = self.hayar_mayor_valor()
            for posiciones in range(posicion_mayor):
                valor_a_cambiar = self.cola[0]
                self.dequeue()
                self.enqueue(valor_a_cambiar)

            valor_a_cambiar = self.top()
            self.dequeue()
            cola_auxiliar.enqueue(valor_a_cambiar)
        for i in range(cola_auxiliar.tamaño()):
            valor_actual = cola_auxiliar.top()
            cola_auxiliar.dequeue()
            self.enqueue(valor_actual)
        return self

"""solicitud1 = Persona(1, "Juan", "Problema de red", 1001)
solicitud2 = Persona(2, "Maria", "Error en el software", 1002)
solicitud3 = Persona(1, "Pedro", "Problema de impresora", 1003)
solicitud4 = Persona(300, "Luisa", "Pérdida de datos", 1004)
solicitud5 = Persona(2, "Carlos", "Problema de conexión", 1005)
solicitud6 = Persona(1, "Ana", "Problema de correo electrónico", 1006)
solicitud7 = Persona(3, "Pablo", "Problema de seguridad", 1007)
solicitud8 = Persona(2, "Laura", "Problema de hardware", 1008)
solicitud9 = Persona(1, "Sofía", "Problema de software", 1009)
solicitud10 = Persona(2, "Miguel", "Problema de red", 1010)

verificar_numero1 = InformacionPersona(solicitud1)
verificar_numero2 = InformacionPersona(solicitud2)
verificar_numero3 = InformacionPersona(solicitud3)
verificar_numero4 = InformacionPersona(solicitud4)
verificar_numero5 = InformacionPersona(solicitud5)
verificar_numero6 = InformacionPersona(solicitud6)
verificar_numero7 = InformacionPersona(solicitud7)
verificar_numero8 = InformacionPersona(solicitud8)
verificar_numero9 = InformacionPersona(solicitud9)
verificar_numero10 = InformacionPersona(solicitud10)



mi_cola_principal = PriorityQueue()


mi_cola_principal.enqueue(verificar_numero1)
mi_cola_principal.enqueue(verificar_numero2)
mi_cola_principal.enqueue(verificar_numero3)
mi_cola_principal.enqueue(verificar_numero4)
mi_cola_principal.enqueue(verificar_numero5)
mi_cola_principal.enqueue(verificar_numero6)
mi_cola_principal.enqueue(verificar_numero7)
mi_cola_principal.enqueue(verificar_numero8)
mi_cola_principal.enqueue(verificar_numero9)
mi_cola_principal.enqueue(verificar_numero10)

#print(mi_cola_principal.hayar_mayor_valor())
mi_cola_principal.llevar_a_primera_posicion()
#mi_cola_principal.imprimir_cola()"""