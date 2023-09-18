class PriorityQueue:
    def __init__(self):
        self.cola = []

    def enqueue(self, informacion):
        self.cola.append(informacion)

    def dequeue(self):
        if self.cola:
            self.cola.pop(0) # Desencola y retorna la primera posicion de la cola

    def top(self):
        return self.cola[0] # Retorna la primera posicion de la cola

    def tamaño(self):
        return len(self.cola) 
    
    def is_empty(self):
        return len(self.cola) == 0
    
    def hayar_mayor_valor(self):
        mayor = -1  # Variable para encontrar el nivel de urgencia mas alto encontrado
        posicion = 0  # Variable para moverme entre las posiciones de la cola
        posicion_del_mayor = 1  # Variable para la posición predeterminada del mayor urgencia

        # Recorre cada solicitud en la cola para encontrar la de mayor urgencia
        for informacion_persona in self.cola:
            if informacion_persona.persona.urgencia > mayor:
                mayor = informacion_persona.persona.urgencia  # Actualiza el valor más alto encontrado
                posicion_del_mayor = posicion  # Actualiza la posición de la solicitud de mayor urgencia en la cola
            posicion += 1  # Avanza a la siguiente posición en la cola

        return posicion_del_mayor  # Devuelve la posición de la solicitud de mayor urgencia en la cola

    def llevar_a_primera_posicion(self):
        cola_auxiliar = PriorityQueue()  # Cola auxiliar para reorganizar las solicitudes

        while self.cola != []:
            posicion_mayor = self.hayar_mayor_valor()  # Encuentra la posición de la solicitud de mayor urgencia en la cola
            for posiciones in range(posicion_mayor):
                valor_a_cambiar = self.cola[0] 
                self.dequeue()  # Desencola la solicitud de la primera posición de la cola
                self.enqueue(valor_a_cambiar)  # Vuelve a agregar la solicitud al final de la cola
            valor_a_cambiar = self.top()  # Obtiene la solicitud de mayor urgencia que ahora está en la primera posición
            self.dequeue()  # Desencola la solicitud de la primera posición
            cola_auxiliar.enqueue(valor_a_cambiar)  # Agrega la solicitud a la cola auxiliar

        # Todas las solicitudes se han re organizado en la cola auxiliar
        for i in range(cola_auxiliar.tamaño()):
            valor_actual = cola_auxiliar.top()
            cola_auxiliar.dequeue()
            self.enqueue(valor_actual) # Se encolan de vuelta a la cola original en orden de urgencia descendente
        return self
     
    def imprimir_cola(self):
        print("|Solicitud  |  Nombre | Problema | Nivel|")
        for informacion_persona in self.cola:
            print(f"{informacion_persona.datos_conjuntos}")
