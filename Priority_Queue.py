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

    def imprimir_cola(self):
        for informacion_persona in self.cola:
            print(f"{informacion_persona.datos_conjuntos}")