# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.

def numeros_primos():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    if numero < 2:
        print("El número no es primo")
    elif numero == 2:
        print("El número es primo")
    elif not(numero % 2 == 0):
        print("EL número es primo")
numeros_primos()