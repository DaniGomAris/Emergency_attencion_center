import random
import sys
from Priority_Queue import PriorityQueue
from Datos_Solicitud import Persona, InformacionPersona
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
                                 
    def menu(self):
        print("""
Menu
1. Agregar solicitud
2. Atender solicitud
3. Visualizar solicitudes
4. Actualizacion de urgencia
5. Atender lotes
6. Salir
""")
        opcion_menu = int(input("Opcion: "))
        if opcion_menu == 1:
            self.agregar_solicitud()

        if opcion_menu == 2:
            self.atender_solicitud()

        if opcion_menu == 3:
            self.visualizar_solicitudes()

        if opcion_menu == 4:
            self.actualizar_solicitud()

        if opcion_menu == 5:
            self.atender_lotes()

        if opcion_menu == 6:
            sys.exit("Chao, gracias por usar este programa")

    def agregar_solicitud(self):
        # Plantilla para crear una nueva solicitud
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        tecnicos = input("Ingrese problema tecnico: ")
        urgencia = int(input("Ingrese nivel de urgencia(1,2,3): "))
        numero_de_solicitud = random.randint(1, 2500)

        if 1 <= urgencia <= 3: # Verifica su nivel de urgencia (mayor o igual a 1 y menor o igual a 3)
            persona = Persona(urgencia, nombre +" "+ apellido, tecnicos, numero_de_solicitud) # Informacion de la solicitud
            informacion_persona = InformacionPersona(persona) # Crea una nueva persona
            self.cola.enqueue(informacion_persona) # Encola la nueva solicitud
            self.cola.llevar_a_primera_posicion() # Reorganiza la cola
            self.menu()
        else:
            print("nivel de urgencia incorrecto")
            self.menu()
            
    def atender_solicitud(self):
        informacion_persona = self.cola.top() # informacion de la persona de la primera posicion
        self.cola.dequeue() # Retorna la primera posicion de la cola de solicitudes
        print("Solicitud atendida:")
        print("Urgencia:", informacion_persona.persona.urgencia)
        print("Nombre:", informacion_persona.persona.nombre)
        print("Descripción del problema:", informacion_persona.persona.descripcionDelProblema)
        print("Número de solicitud:", informacion_persona.persona.numeroDeSolicitud)
        self.menu()

    def visualizar_solicitudes(self):
        print()
        self.cola.imprimir_cola()
        self.menu()
        
    def actualizar_solicitud(self):
        numero_de_solicitud = int(input("Ingrese el número de solicitud que desea actualizar: "))  # Numero de solicitud para hacer cambio de nivel de urgencia
        new_urgencia = int(input("Ingrese el nuevo nivel de urgencia (1, 2, 3): "))  # Nuevo nivel de urgencia

        for informacion_persona in self.cola.cola:  #  La primera cola es la instancia de la clase (MenuProgram) y la segunda cola se refiere a la cola de prioridad dentro de esa instancia (PriorityQueue)
            if informacion_persona.persona.numeroDeSolicitud == numero_de_solicitud:  # Verifica si la solicitud ingresada si existe
                informacion_persona.persona.urgencia = new_urgencia  # Actualiza el nivel de urgencia de la solicitud
                self.cola.llevar_a_primera_posicion()  # Reorganiza la cola
                print("Solicitud actualizada correctamente.")
                self.menu() 

        print("No se encontró ninguna solicitud con ese número de solicitud.") 
        self.menu() 


    def atender_lotes(self, colalvl1=PriorityQueue(), colalvl2=PriorityQueue(), colalvl3=PriorityQueue()):
        self.cola.cola.sort(key=lambda informacion_persona: informacion_persona.persona.nombre)

        while not self.cola.is_empty():
            informacion_persona = self.cola.top()  # Obtener la información de la persona en la primera posición

            if informacion_persona.persona.urgencia == 3:
                print("Solicitud atendida:")
                print("Urgencia:", informacion_persona.persona.urgencia)
                print("Nombre:", informacion_persona.persona.nombre)
                print("Descripción del problema:", informacion_persona.persona.descripcionDelProblema)
                print("Número de solicitud:", informacion_persona.persona.numeroDeSolicitud)
                print()

                nombre = informacion_persona.persona.nombre
                problema = informacion_persona.persona.descripcionDelProblema
                urgencia = informacion_persona.persona.urgencia
                numero_de_solicitud = informacion_persona.persona.numeroDeSolicitud

                persona = Persona(urgencia, nombre, problema, numero_de_solicitud)
                informacion_persona = InformacionPersona(persona)
                colalvl3.enqueue(informacion_persona)

            if informacion_persona.persona.urgencia == 2:
                print("Solicitud atendida:")
                print("Urgencia:", informacion_persona.persona.urgencia)
                print("Nombre:", informacion_persona.persona.nombre)
                print("Descripción del problema:", informacion_persona.persona.descripcionDelProblema)
                print("Número de solicitud:", informacion_persona.persona.numeroDeSolicitud)
                print()

                nombre = informacion_persona.persona.nombre
                problema = informacion_persona.persona.descripcionDelProblema
                urgencia = informacion_persona.persona.urgencia
                numero_de_solicitud = informacion_persona.persona.numeroDeSolicitud

                persona = Persona(urgencia, nombre, problema, numero_de_solicitud)
                informacion_persona = InformacionPersona(persona)
                colalvl2.enqueue(informacion_persona)

            if informacion_persona.persona.urgencia == 1:
                print("Solicitud atendida:")
                print("Urgencia:", informacion_persona.persona.urgencia)
                print("Nombre:", informacion_persona.persona.nombre)
                print("Descripción del problema:", informacion_persona.persona.descripcionDelProblema)
                print("Número de solicitud:", informacion_persona.persona.numeroDeSolicitud)
                print()

                nombre = informacion_persona.persona.nombre
                problema = informacion_persona.persona.descripcionDelProblema
                urgencia = informacion_persona.persona.urgencia
                numero_de_solicitud = informacion_persona.persona.numeroDeSolicitud

                persona = Persona(urgencia, nombre, problema, numero_de_solicitud)
                informacion_persona = InformacionPersona(persona)
                colalvl1.enqueue(informacion_persona)

            self.cola.dequeue()

        print("Cola nivel 3")
        colalvl3.imprimir_cola() 

        print()

        print("Cola nivel 2")
        colalvl2.imprimir_cola()  

        print()

        print("Cola nivel 1")
        colalvl1.imprimir_cola()  

        self.menu()