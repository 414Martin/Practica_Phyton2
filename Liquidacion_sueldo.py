"""practica 1"""
"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas\
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
horas_trabajadas=float(input("Ingrese la cantida de horas trabajadas: "))
coste_hora=float(input("Ingrese el valor por hora: "))
valor_mensual=horas_trabajadas*coste_hora

print("Por",horas_trabajadas,"horas trabajadas en el mes, ganaste",valor_mensual)
