#-------------------LISTAS-----------------
#Para crearla, sus elementos se ponen entre corchetes []
#Ejemplo de lista
datitos= [1, 2, "b", "c"]
#Accedemos a los elementos de la lista contando por índice, que empieza en 0,
#si queremos acceder a "b" escribimos
datitos[2]
print ("ACCEDEMOS A UN ELEMENTO DE LA LISTA POR ÍNDICE: ", datitos[2])
#para recorrer una lista usamos el for
for elementos in datitos:
    print ("RECORRIDO CON 'FOR': ", elementos)
#y se muestra todo lo que está en la lista
#para AGREGAR elementos a una lista:
#datitos.append()
#y entre paréntesis le ponemos lo que queremos agregar, ej:
datitos.append(3)
print ("LE AGREGAMOS UN ELEMENTO MÁS A LA LISTA: ", datitos)
#para MODIFICAR elementos de una lista escribimos esto:
#datitos.[numDeIndice]=nuevoElemento
datitos[1]=6
print ("MODIFICAMOS UN ELEMENTO DE LA LISTA: ", datitos)
#para ELIMINAR algo de una lista usamos del y el número de índice, por ej
del datitos[0]
print ("ELIMINAMOS UN ELEMENTO DE LA LISTA CON 'DEL': ", datitos)
#también podemos eliminar un elemento con 'pop(indice),
#por ej si queremos borrar la letra "c" de nuestra lista escribimos:
datitos.pop(2)
print ("ELIMINAMOS USANDO DATITOS.POP(): ", datitos)
#para saber la longitud de una lista usamos len(nombreDeLista) x ej:
print ("SABER LA LONGITUD CON 'LEN': ", len(datitos))
#para SABER SI UN ELEMENTO ESTÁ EN UNA LISTA usamos el 'in' x ej:
if "b" in datitos:
    print ("La letra está")
else:
    print ("La letra que busca no está")
print ("")
print ("")
print ("")
#------------------TUPLAS-------------------------
#LAS TUPLAS NO SE PUEDEN MODIFICAR!!!
#Las tuplas se definen así, podemos agregar distintos objetos, como int,
#strings, listas, etc:
tuplita= 1, "casa", 2.5, 3.66, "hola", "amarillo", datitos
print ("ESTO ES UNA TUPLA: ", tuplita)
#para ACCEDER a los elementos de una tupla usamos el número de índice, por ej
print ("ACCEDEMOS AL PRIMER ELEMENTO DE LA TUPLA POR INDICE: ", tuplita[0])
#para RECORRER UNA TUPLA usamos 'for-in' x ej
for elementos in tuplita:
    print ("RECORRIMOS LA TUPLA CON FOR-IN: ", elementos)
#para saber su longitud volvemos a usar len()
    print ("ESTE ES EL LARGO DE LA TUPLA: ", len(tuplita))
#para saber si un elemento está en una tupla usamos el 'in'
    if "casa" in tuplita:
        print ("el elemento buscado está")
    else:
        print ("el elemento buscado no está")
print ("")
print ("")
print ("")

#-------------------DICCIONARIOS--------------------

#los diccionarios usan el par llamado clave:valor, es decir que para
#cada elemento dentro del diccionario va a haber una clave
#la forma más fácil de CREAR un diccionario es encerrar una secuencia de
#clave:valor separados por comas usando llaves {} al principio y al final
dic= {'clave1':'valor1', 'clave2':'valor2',3:3, 'clave4':'valor4'}
print ("Este es el diccionario: ", dic)
#también podemos crear un diccionario vacio asi: dic={}
#para ACCEDER a un valor deel diccionario usamos el nombre del diccionario
#y entre corchetes la CLAVE, x ej
print ("ACCEDEMOS AL PRIMER VALOR: ", dic['clave1'])
#para RECORRER un diccionarios usamos'for-in':

for todo in dic:
    print ("RECORREMOS EL DICCIONARIO: ", todo)
#para AGREGAR un nuevo par a un diccionario hacemos esto
dic['claveNueva']="valor nuevo"
print ("LE AGREGAMOS ALGO AL DICCIONARIO: ", dic)
#si quisieramos MODIFICAR un valor accediendo por clave, hacemos
#lo mismo que hicimos para agregar un par nuevo, pero usamos el
#nombre de clave ya asignado y le cambiamos el valor
dic['clave1']='valor cambiado'
print ("AHORA CAMBIAMOS UN VALOR: ", dic)
#para ELIMINAR un par clave:valor usamos 'del' x ej
del dic['clave2']
print ("ELIMINAMOS UNA CLAVE:VALOR: ", dic)
#la longitud del diccionario se averigua con len()
print ("EL DICCIONARIO TIENE ESTA CANTIDAD DE PARES: ", len(dic))
#para COMPROBAR SI UNA CLAVE ESTÁ en el diccionario lo comprobamos con un in
if 'clave4' in dic:
    print ("La clave que busca está")
else:
    print ("la clave no está")
#si queremos CAMBIAR LA CLAVE de un par en un diccionario, escribimos x ej
dic['claveCambiada']=dic.pop('clave4')
print ("CAMBIAMOS UNA CLAVE: ", dic)
#si queremos podemos METER UN DICCIONARIO EN UNA LISTA x ej
datitos.append(dic)
print ("LISTA CON UN DICCIONARIO AGREGADO: ", datitos)
#o podemos METER UNA LISTA EN UN DICCIONARIO x ej
dic['lista']=datitos
print ("DICCIONARIO CON UNA LISTA AGREGADA: ", dic)
