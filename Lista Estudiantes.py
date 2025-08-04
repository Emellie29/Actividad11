estudiantes={}
while True:
    print("•••••••MENÚ PRINCIPAL•••••••")
    print("1. Registrar estudiantes")
    print("2. Mostrar estudiantes")
    print("3. Salir")
    opcion=input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad de estudiantes: "))
        for i in range(cantidad):
            print(f"Estudiante No.{i + 1}")
            carnet = int(input("Ingrese el carnet del estudiante: "))
            nombre = input("Ingrese el nombre completo del estudiante: ")
            carrera = input("Ingrese carrera: ")
            estudiantes[carnet] = {
                "nombre": nombre,
                "carrera": carrera
            }
    elif opcion == "2":
        if not estudiantes:
            print("No se encontro estudiantes registrados")
        else:
            for carnet, datos in estudiantes.items():
                print(f"\nCarnet: {carnet}")
                print(f"Nombre: {datos["nombre"]}")
                print(f"Carrera: {datos["carrera"]}")
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[0]
            primer = [a for a in lista[1:] if a < pivote]
            igual = [a for a in lista if a == pivote]
            ultimo = [a for a in lista[1:] if a > pivote]
            return quick_sort(primer) + igual + quick_sort(ultimo)
        estudiantes = carnet.copy()
        mostrar = quick_sort(estudiantes)
        print(mostrar)
    elif opcion=="3":
        print("Cerrando Sesión")
        break
    else:
        print("Opcion no valida")