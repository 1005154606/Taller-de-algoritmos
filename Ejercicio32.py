nota1=float(input("introduce la primera nota: "))
nota2=float(input("introduce la segunda nota: "))
nota3=float(input("introduce la tercera nota: "))
nota4=float(input("introduce la cuarta nota: "))
nota5=float(input("introduce la quinta nota: "))
n1=nota1*0.15
n2=nota2*0.20
n3=nota3*0.15
n4=nota4*0.30
n5=nota5*0.20
suma=n1+n2+n3+n4+n5
if suma<3.0:
    print(suma)
    print("El restudiante reprobo")
    if suma<2.0:
        print("El estudiante no puede habilitar")
if suma>=3.0:
    print(suma)
    print("El estudiante aprobó")
    if suma>=4.5:
        print("Felicitaciones por el excelente desempeño excelente desempeño del estudiante")

