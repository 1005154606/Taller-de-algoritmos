for x in range(0,7):
    num=int(input("Introduce el número de días: "))
    if num==1:
        print("lunes")
    if num==2:
        print("martes")
    if num==3:
        print("miercoles")
    if num==4:
        print("jueves")
    if num==5:
        print("viernes")
    if num==6:
        print("sabado")
    if num==7:
        print("domingo")
    if num<=0 or num>7:
        print("La semana solo tiene siete días")