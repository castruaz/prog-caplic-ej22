import os ; os.system('clear')
ini = 490
fin = 500
print(f'{"Tabla de conversiones":^40}')
print('-'*40)
print('{p1:.>10}{p2:,^10}{p3:.<10}{p4:,>10}'.format(p1='Decimal',p2='Hexa',p3='Octal',p4='Binario'))
print('-'*40)
for i in range(ini, fin+1):
    print(f'{i:>15}{i:^10x}{i:<10o}{i:>10b}')
print('-'*40)