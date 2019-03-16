n=int(input(' Ingrese el número de filas: '))
for i in range(n):
    a = ''
    for j in range(n):

        if j>=i:
            a+='* '
        else:
            a+=' '

    print(a)