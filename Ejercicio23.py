s=int(input("Introduce la cantidad de segundos: "))
m1=float(s/60)
m2=int(m1)
m3=m2*60
m4=s-m3
h1=float(m2/60)
h2=int(h1)
h3=h2*60
h4=m2-h3
print(h2,":",h4,":",m4)