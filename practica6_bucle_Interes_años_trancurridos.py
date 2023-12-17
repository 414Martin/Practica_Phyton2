"""practica bucles 5"""
"""
Escribir un programa que pregunte al usuario una cantidad a invertir,\
el interés anual y el número de años, y muestre por pantalla el capital\
obtenido en la inversión cada año que dura la inversión.
"""

invercion=float(input("Ingrese la invercion: "))
interes_anual=float(input("Ingrese interes anual: "))
años_trascurridos=int(input("ingrese años transcurridos: "))
for i in range(años_trascurridos):
    invercion *= 1 + interes_anual / 100
    print("El capital tras ", str(i+1), "años: ", round(invercion, 2 ))

"""
cuando en la linea de print despues de un for hay un (i)me indica la cantidad\
de vueltas.
El round(variable, 2): round redondea, y el numero despues de la variable indica\
la cantidad de dijitos despues del punto.
