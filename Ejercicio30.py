venta=int(input("Introduce el precio de la venta: "))
descuento=venta*0.05
if venta>=150000:
    x=venta-descuento
    iva1=x*0.19
    print("El total de la venta es ",x,"y su iva es de ",iva1,"%")
else:
    iva2=venta*0.19
    print("El valor de la venta es de", venta,"y tiene un iva de",iva2)