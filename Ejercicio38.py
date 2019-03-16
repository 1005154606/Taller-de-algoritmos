agno=int(input("Introduce un año: "))
if (agno%400==0 ) or (agno%4==0 and agno%100!=0):
    print("el año es bisiesto")
else:
    print("El año no es bisiesto")