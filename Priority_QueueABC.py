class PriorityQueue_ABC:
    def __init__(self):
        self.colaABC = []

    def enqueue(self, informacion):
        self.colaABC.append(informacion)

    def dequeue(self):
        if self.colaABC:
            self.colaABC.pop(0) # Desencola y retorna la primera posicion de la cola

    def top(self):
        return self.colaABC[0] # Retorna la primera posicion de la cola

    def tamaño(self):
        return len(self.colaABC) 
    
    def is_empty(self):
        return len(self.colaABC) == 0

    def ordenar_por_nombre(self):
        self.colaABC.sort(key=lambda informacion_persona: informacion_persona.persona.nombre)

    def imprimir_cola(self):
        print("|Solicitud  |  Nombre | Problema | Nivel|")
        for informacion_persona in self.colaABC:
            print(f"{informacion_persona.datos_conjuntos}")