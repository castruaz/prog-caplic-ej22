# tabla de multiplicar con for

t = int(input("Dame una tabla ? "))
n = int(input("Hasta donde la deseas ? "))

for i in range(1,n+1):
  print("{0} x {1} = {2}".format(t,i,t*i))