 
# imprime los numeros del 1 al 100 o del 100 al 1
import os
os.system('clear')
op = int( input('[1] arriba \n[2] abajo ?\n') )
n = int(input('Limite ?'))
if op==1:
	print(f'\nImprimiendo los numeros de 1 hasta {n}\n')
	for x in range(1,n+1,1):
		print(x,end=' ')
elif op==2:
	print(f'\nImprimiendo los numeros de {n} hasta 1\n')
	for x in range(n,0,-1):
		print(x,end=' ')

