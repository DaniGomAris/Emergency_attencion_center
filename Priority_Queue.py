class PriorityQueue:
    def __init__(self):
        self.cola = []

    def enqueue(self, informacion):
        self.cola.append(informacion)
        self.ordenar_cola()

    def dequeue(self):
        if self.cola:
            self.cola.pop(0) # Desencola y retorna la primera posicion de la cola

    def top(self):
        return self.cola[0] # Retorna la primera posicion de la cola

    def tamaño(self):
        return len(self.cola) 
    
    def is_empty(self):
        return len(self.cola) == 0
    
    def ordenar_cola(self):
        self.cola.sort(reverse=True, key=lambda informacion_persona: informacion_persona.persona.urgencia)

    def imprimir_cola(self):
        print("|Solicitud  |  Nombre | Problema | Nivel|")
        for informacion_persona in self.cola:
            print(f"{informacion_persona.datos_persona}")