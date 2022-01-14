nota1=int(input('ingrese la nota 1: '))
nota2=int(input('ingrese la nota 2: '))
nota3=int(input('ingrese la nota 3: '))

suma=nota1+nota2+nota3
prom=suma/3

print('el promedio es: ',prom)

if prom >=7:
    print('promocionado')
elif prom >=4 and prom <7:
    print('regular')
else:
    print('reprobado')
