# tabla de multiplicar con for v2

import os

os.system('clear')
t = int(input("Hasta que tabla       ? "))
n = int(input("Hasta donde la deseas ? "))

for x in range(1,t+1):
  for i in range(1,n+1):
    print("{0} x {1} = {2}".format(x,i,x*i))
  print('\r')