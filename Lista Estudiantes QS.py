def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        primer = [a for a in lista[1:] if a < pivote]
        igual = [a for a in lista if a == pivote]
        ultimo = [a for a in lista[1:] if a > pivote]
    return quick_sort(primer) + igual + quick_sort(ultimo)
cantidad = int(input("¿Cuántos nombres deseas ingresar?: "))
nombres = []
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre #{i + 1}: ")
    nombres.append(nombre)
nombres_ordenados = quick_sort(nombres)
print("\nLista ordenada alfabéticamente:")
for nombre in nombres_ordenados:
    print(nombre)