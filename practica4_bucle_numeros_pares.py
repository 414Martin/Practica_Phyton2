"""Practica bucles"""
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por\
pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""


numero=int(input("Ingresar un numero: "))

for i in range(0,numero+1,2):
    print(i,end=",")


"""
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")
"""
