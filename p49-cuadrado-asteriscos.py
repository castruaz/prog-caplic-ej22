# cuadro de asteriscos
 
r = int(input('Cuantos renglones ? '))
c = int(input('Cuantas columnas  ? '))
for i in range(1,r+1):
    for j in range(1,c+1):
        print('* ', end='')
    print('\r')
