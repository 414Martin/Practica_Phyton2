def mostrarCompras (compras):
    for numeroCompra in compras:
        print (numeroCompra, compras[numeroCompra])

def montoCompra (compras, numeroCompra):
    return compras[numeroCompra][4]*compras[numeroCompra][5]

def montoTotalCompras (compras):
    montoTotal = 0
    for numeroCompra in compras:
        montoTotal += montoCompra(compras, numeroCompra)
##        montoTotal = montoTotal + montoCompra(compras, numeroCompra)
    return montoTotal

def mostrarCompra (compras, numeroCompra):
    print (compras[numeroCompra])
