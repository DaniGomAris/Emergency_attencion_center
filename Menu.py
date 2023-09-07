import random
from Priority_Queue import PriorityQueue
from Program import Persona, InformacionPersona
from Persons import nombres,apellidos,problemas_tecnicos

class Program:
    def main(self, iteracion):
        contador = 1
        cola = PriorityQueue()
        while contador <= iteracion:
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            tecnicos = random.choice(problemas_tecnicos)
            urgencia = random.randint(1,3)
            numero_de_solicitud = random.randint(1, 2500)

            persona = Persona(urgencia, nombre, tecnicos, numero_de_solicitud)
            informacion_persona = InformacionPersona(persona)
            cola.enqueue(informacion_persona)
            contador += 1

        cola = cola.llevar_a_primera_posicion()
        cola.imprimir_cola()
