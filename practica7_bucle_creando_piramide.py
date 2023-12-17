"""practica bucle 6"""
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla\
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****


numero=int(input("Ingres un numero entero: "))

for numero in range (0,5,0):
    numero=numero+1
    print(numero)
"""
numero = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(numero):
   print("*"*(i+1))

