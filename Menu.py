import random
from Priority_Queue import PriorityQueue
from Program import Persona, InformacionPersona
from Persons import nombres,apellidos,problemas_tecnicos

class MenuProgram:

    def __init__(self):
        self.cola = PriorityQueue()

    def iniciar(self, iteracion):
        contador = 1
        while contador <= iteracion:
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            problema = random.choice(problemas_tecnicos)
            urgencia = random.randint(1,3)
            numero_de_solicitud = random.randint(1, 2500)

            persona = Persona(urgencia, nombre +" "+ apellido, problema, numero_de_solicitud)
            informacion_persona = InformacionPersona(persona)
            self.cola.enqueue(informacion_persona)
            contador += 1
        cola = self.cola.llevar_a_primera_posicion()
        print("|Solicitud  |  Nombre | Problema | Nivel|")
        cola.imprimir_cola()   
                                 
    def menu(self):
        print("""
Menu
1. Agregar solicitud
2. Atender solicitud
3. Visualizar solicitudes
4. Actualizacion de urgencia
""")
        opcion_menu = int(input("Opcion: "))
        if opcion_menu == 1:
            self.agregar_solicitud()

        if opcion_menu == 2:
            self.atender_solicitud()

        if opcion_menu == 3:
            self.visualizar_solicitudes()

        if opcion_menu == 4:
            self.acualizar_solicitud()

    def agregar_solicitud(self):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        tecnicos = input("Ingrese problema tecnico: ")
        urgencia = int(input("Ingrese nivel de urgencia(1,2,3): "))
        numero_de_solicitud = random.randint(1, 2500)

        if 1 <= urgencia <= 3:
            persona = Persona(urgencia, nombre +" "+ apellido, tecnicos, numero_de_solicitud)
            informacion_persona = InformacionPersona(persona)
            self.cola.enqueue(informacion_persona)
            self.cola.llevar_a_primera_posicion()
            self.menu()
        else:
            print("nivel de urgencia incorrecto")
            self.menu()
            
    def atender_solicitud(self):
        informacion_persona = self.cola.top()
        self.cola.dequeue()
        print("Solicitud atendida:")
        print("Urgencia:", informacion_persona.persona.urgencia)
        print("Nombre:", informacion_persona.persona.nombre)
        print("Descripción del problema:", informacion_persona.persona.descripcionDelProblema)
        print("Número de solicitud:", informacion_persona.persona.numeroDeSolicitud)
        self.menu()

    def visualizar_solicitudes(self):
        print("|Solicitud  |  Nombre | Problema | Nivel|")
        self.cola.imprimir_cola()
        self.menu()
        
    def acualizar_solicitud(self):
        numero_de_solicitud = int(input("Ingrese el número de solicitud que desea actualizar: "))
        new_urgencia = int(input("Ingrese el nuevo nivel de urgencia (1, 2, 3): "))

        for informacion_persona in self.cola.cola:
            if informacion_persona.persona.numeroDeSolicitud == numero_de_solicitud:
                informacion_persona.persona.urgencia = new_urgencia
                self.cola.llevar_a_primera_posicion()
                print("Solicitud actualizada correctamente.")
                self.menu()

        print("No se encontró ninguna solicitud con ese número de solicitud.")
        self.menu()
