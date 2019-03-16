distancia=float(input("Introduce la distancia en km: "))
dias=int(input("Introduce el número de días de estancia: "))
precio=distancia*5000

if precio<100000:
    precio=100000
    print("el precio es de", precio)
else:
    print("el precio es de", precio)


if distancia>1000 and dias>7:
        descuento=precio*0.15
        preciof=precio-descuento
        print("Aplicando es descuento elprecio es de", preciof)
