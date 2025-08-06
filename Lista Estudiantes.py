def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    primer = [a for a in lista[1:] if a < pivote]
    igual = [a for a in lista if a == pivote]
    ultimo = [a for a in lista[1:] if a > pivote]
    return quick_sort(primer) + igual + quick_sort(ultimo)
estudiantes={}
while True:
    print("•••••••MENÚ PRINCIPAL•••••••")
    print("1. Registrar estudiantes")
    print("2. Mostrar estudiantes")
    print("3. Mostrar carnets ordenados")
    print("4. Mostrar nombres ordenados alfabeticamente")
    print("5. Salir")
    opcion=input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = int(input("\nIngrese la cantidad de estudiantes: "))
        for i in range(cantidad):
            print(f"\nEstudiante No.{i + 1}")
            carnet = int(input("Ingrese el carnet del estudiante: "))
            nombre = input("Ingrese el nombre completo del estudiante: ")
            estudiantes[carnet] = {
                "nombre": nombre
            }
    elif opcion == "2":
        if not estudiantes:
            print("No se encontro ningun estudiante registrado")
        else:
            for carnet, datos in estudiantes.items():
                print(f"\nCarnet: {carnet}")
                print(f"Nombre: {datos["nombre"]}")
    elif opcion=="3":
        if not estudiantes:
            print("No se encontro ningun estudiante registrado")
        else:
            carnets=list(estudiantes)
            carnet_ordenado=quick_sort(carnets)
            print("\nLista de carnets ordenados")
            for carnet in carnet_ordenado:
                print(f"Carnet: {carnet} - {estudiantes[carnet]['nombre']}")
    elif opcion=="4":
        if not estudiantes:
            print("No se encontro ningun estudiante registrado")
        else:
            lista_nombres=[(datos['nombre'], carnet) for carnet, datos in estudiantes.items()]
            nombre_ordenado=quick_sort(lista_nombres)
            print("\nLista de nombres ordenados alfabeticamente")
            for nombre, carnet in nombre_ordenado:
                print(f"Nombre: {nombre} - {carnet}")
    elif opcion=="5":
        print("Cerrando Sesión")
        break
    else:
        print("Opcion no valida")