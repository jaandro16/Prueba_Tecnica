# ------------------------------------------------------------
# Author: Alejandro Pérez Rentero
# Date: February 10, 2025
# Description: 
#   This program asks the user to input a list of numbers 
#   one by one. Then, it removes duplicate values while 
#   maintaining the original order and prints both the 
#   original and the filtered lists in the requested format.
# Version: 1.0
# ------------------------------------------------------------

def eliminar_duplicados(lista):
    resultado = []
    for num in lista:
        if num not in resultado:
            resultado.append(num)
    return resultado

# Solicitar entrada del usuario
numeros = []
print("Introduce números uno a uno. Escribe 'fin' para terminar:")

while True:
    entrada = input("Número: ")
    if entrada.lower() == "fin":  # Permitir que el usuario termine la entrada
        break
    if entrada.isdigit():  # Verifica que sea un número válido
        numeros.append(int(entrada))
    else:
        print("Entrada no válida. Introduce solo números positivos enteros \no 'fin' para terminar.")


# Imprimir la lista original
print(f"entrada = {numeros}")

# Eliminar duplicados y mostrar resultado
resultado = eliminar_duplicados(numeros)

# Imprimir la lista de salida
print(f"salida = {resultado}")