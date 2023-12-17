from funcionesCompras import*
compras = {}
opcion = input ("1 Ingresar Compra\n2 Mostrar Compras\n3 Obtener Total de Una compra\n4 Mostrar una compra\n5 Salir\n")

while (opcion != "5"):
    if (opcion == "1"):
        nombreUsuario = input ("Ingresar Nombre de Usuario: ")
        numeroSerie = input ("Ingresar Numero de Serie: ")
        categoria = input ("Categoria: ")
        descripcion = input ("Descripcion: ")
        precio = float (input ("Precio: "))
        cantidad = int (input ("Cantidad: "))
        numeroCompra = input ("Numero de Compra: ")
        compras[numeroCompra] = [nombreUsuario,numeroSerie,categoria,descripcion, precio,cantidad]
    elif (opcion == "2"):
        mostrarCompras (compras)
    elif (opcion == "3"):
        print (montoCompra(compras,input ("Ingresar Numero de Compra: ")))
    elif(opcion == "4"):
        numeroCompraMostrar = input ("Ingresar Numero Compra que desea Mostrar: ")
        mostrarCompra (compras, numeroCompraMostrar)
    opcion = input ("1 Ingresar Compra\n2 Mostrar Compras\n3 Obtener Total de Una compra\n4 Mostrar una compra\n5 Salir\n")
