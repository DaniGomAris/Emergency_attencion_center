class PriorityQueue_ABC:
    def __init__(self):
        self.colaABC = []

    def enqueue(self, informacion):
        self.colaABC.append(informacion)
        self.ordenar_cola()

    def dequeue(self):
        if self.colaABC:
            self.colaABC.pop(0) # Desencola y retorna la primera posicion de la cola

    def top(self):
        return self.colaABC[0] # Retorna la primera posicion de la cola

    def tamaño(self):
        return len(self.colaABC) 
    
    def is_empty(self):
        return len(self.colaABC) == 0
    
    def ordenar_cola(self):
        self.colaABC.sort(key=lambda persona: persona.nombre)

    def imprimir_cola(self):
        print("|Solicitud  |  Nombre | Problema | Nivel|")
        for informacion_persona in self.colaABC:
            print(f"{informacion_persona.numeroDeSolicitud} | {informacion_persona.nombre} | {informacion_persona.descripcionDelProblema} | {informacion_persona.urgencia}")