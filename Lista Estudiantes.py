cantidad = int(input("¿Cuántos nombres desea ingresar? "))
for i in range(cantidad):
    print(f"Nombre #{i + 1}")
    nombre = input("Ingrese el nombre: ")
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    primer=[a for a in lista[1:] if a < pivote]
    igual=[a for a in lista if a == pivote]
    ultimo=[a for a in lista[1:] if a > pivote]
    return quick_sort(primer) + igual + quick_sort(ultimo)
estudiantes=""
mostrar=quick_sort(estudiantes)
print(mostrar)