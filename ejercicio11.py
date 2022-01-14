nro =int(input("ingresar un numero distinto a cero: "))

if nro != 0:
    if nro %2 == 0:
        print("El numero es par")
    else:
        print('el numero es impar')    
else:
    print("el numero es mayor.")
