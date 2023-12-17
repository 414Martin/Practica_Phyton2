"""practica bubles 2"""

"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos\
los años que ha cumplido (desde 1 hasta su edad).
"""

edad=int(input("¿Que edad tienes?: "))

for edad in  range(1,edad+1):
    print("Has cumplido",edad,"años")

"""
age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")

"""
