from Menu import MenuProgram

if __name__ == "__main__":
    console = MenuProgram()
    print("""
¿Cuantas solicitudes quiere?
1. 10
2. 100
3. 1000
4. 10000
""")
    opcion_numero_solicitudes = int(input("Opcion: "))
    if opcion_numero_solicitudes == 1:
        console.iniciar(10)
        console.menu()

    if opcion_numero_solicitudes == 2 :
        console.iniciar(100)
        console.menu()

    if opcion_numero_solicitudes == 3:
        console.iniciar(1000)
        console.menu()

    if opcion_numero_solicitudes == 4:
        console.iniciar(10000)
        console.menu()
    