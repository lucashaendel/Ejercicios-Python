# desaprobado = 1 a 4
# bueno = 5 a 7
# aprobado = 8 a 9
# sobresaliente= 10
    
nota=int(input('ingrese un valor: '))

if nota<=4:
    print('desaprobado')
elif nota <=7:
        print('bueno')
elif nota <=9:
        print('aprobado')
elif nota == 10:
        print('sobresaliente')

else:
    print('nota no existe')