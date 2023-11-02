import random
import sys
from Priority_Queue import PriorityQueue
from Priority_QueueABC import PriorityQueue_ABC
from Datos_Solicitud import Persona
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
            urgencia = random.randint(1,10)
            numero_de_solicitud = random.randint(1, 2500)

            persona = Persona(urgencia, nombre +" "+ apellido, problema, numero_de_solicitud)
            self.cola.enqueue(persona)
            contador += 1 
                                 
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
            print()
            self.agregar_solicitud()

        if opcion_menu == 2:
            print()
            self.atender_solicitud()

        if opcion_menu == 3:
            print()
            self.visualizar_solicitudes()

        if opcion_menu == 4:
            print()
            self.actualizar_solicitud()

        if opcion_menu == 5:
            print()
            self.atender_lotes()

        if opcion_menu == 6:
            sys.exit("Chao, gracias por usar este programa")

    def agregar_solicitud(self):
        # Plantilla para crear una nueva solicitud
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        tecnicos = input("Ingrese problema tecnico: ")
        urgencia = int(input("Ingrese nivel de urgencia: "))
        numero_de_solicitud = random.randint(1, 2500)


        persona = Persona(urgencia, nombre +" "+ apellido, tecnicos, numero_de_solicitud) # Informacion de la solicitud
        self.cola.enqueue(persona) # Encola la nueva solicitud
        self.menu()

            
    def atender_solicitud(self):
        persona = self.cola.top() # informacion de la persona de la primera posicion
        self.cola.dequeue() # Retorna la primera posicion de la cola de solicitudes
        print("Solicitud atendida:")
        print("Urgencia:", persona.urgencia)
        print("Nombre:", persona.nombre)
        print("Descripción del problema:", persona.descripcionDelProblema)
        print("Número de solicitud:", persona.numeroDeSolicitud)
        self.menu()

    def visualizar_solicitudes(self):
        self.cola.imprimir_cola()
        self.menu()
        
    def actualizar_solicitud(self):
        numero_de_solicitud = int(input("Ingrese el número de solicitud que desea actualizar: "))  # Numero de solicitud para hacer cambio de nivel de urgencia
        new_urgencia = int(input("Ingrese el nuevo nivel de urgencia: "))  # Nuevo nivel de urgencia

        for persona in self.cola.cola:  #  La primera cola es la instancia de la clase (MenuProgram) y la segunda cola se refiere a la cola de prioridad dentro de esa instancia (PriorityQueue)
            if persona.numeroDeSolicitud == numero_de_solicitud:  # Verifica si la solicitud ingresada si existe
                persona.urgencia = new_urgencia
                self.cola.ordenar_cola()  # Reorganiza la cola
                print("Solicitud actualizada correctamente.")
                self.menu() 

        print("No se encontró ninguna solicitud con ese número de solicitud.") 
        self.menu() 

    def atender_lotes(self):
        # Diccionario para almacenar colas ABC de acuerdo al nivel de urgencia
        # Las claves del diccionario son los niveles de urgencia
        # Los valores de cada clave son las colas ABC

        #colas_ABC_por_urgencia = {
        #   1: <Cola ABC>,
        #   2: <Cola ABC>,
        #   3: <Cola ABC>}

        colas_ABC_por_urgencia = {}
        
        while not self.cola.is_empty():
            persona = self.cola.top() # Solicitud con mayor urgencia de la cola
            nivel_urgencia = persona.urgencia  # Obtener el nivel de urgencia

            # Imprimir la informacion de la solicitud atendida
            print("Solicitud atendida:")
            print("Urgencia:", persona.urgencia)
            print("Nombre:", persona.nombre)
            print("Descripción del problema:", persona.descripcionDelProblema)
            print("Número de solicitud:", persona.numeroDeSolicitud)
            print()

            # Crear la urgencia para añadirla a las colas ABC
            nombre = persona.nombre
            problema = persona.descripcionDelProblema
            urgencia = persona.urgencia
            numero_de_solicitud = persona.numeroDeSolicitud

            # Creacion del objeto
            persona = Persona(urgencia, nombre, problema, numero_de_solicitud)

            # Verificar si ya existe una cola ABC para ese nivel de urgencia
            if nivel_urgencia not in colas_ABC_por_urgencia:
                colas_ABC_por_urgencia[nivel_urgencia] = PriorityQueue_ABC()  # Crear una nueva cola ABC

            # Agregar la nueva urgencia a la cola ABC que corresponde al nivel de urgencia
            colas_ABC_por_urgencia[nivel_urgencia].enqueue(persona)

            # Desencolar de la cola principal
            self.cola.dequeue()

        # Imprimir las colas ABC organizadas por nivel de urgencia y ordenadas por nombre
        # Ciclo en las claves del diccionario(niveles de urgencia) y en los valores del diccionario(Colas ABC)
        # El .items() permite obtener todos los pares clave-valor del diccionario
        for nivel_urgencia, cola_ABC in colas_ABC_por_urgencia.items():
            print(f"Cola Nivel de Urgencia: {nivel_urgencia}")
            cola_ABC.imprimir_cola()  # Imprimir la cola ABC
            print()
    
        self.menu()

