usuario="carlos"
contrasegna=1234
us=str(input("Introduce tu usuario: "))
contra=int(input("Introduce tu contraseña: "))
if us==usuario and contra==contrasegna:
    print("El usuario y la contraseña coinciden")
else:
    if us!=usuario and contra!=contrasegna:
        print("el usuario", us, "no coincide con el usuario", usuario, " y la contraseña", contra, "tampoco coincide con",contrasegna)


    if us==usuario and contra!=contrasegna:
        print("el usuario", us, "coincide con el usuario", usuario, "pero la contraseña", contra,"no coincide con",contrasegna )


    if us!=usuario and contra==contrasegna:
        print("el usuario", us, "no coincide con el usuario", usuario, "pero la contraseña", contra," coincide con",contrasegna )
