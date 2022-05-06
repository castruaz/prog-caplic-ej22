# suma de numeros

cuantos = int(input('Cuantos numeros? '))
suma = 0
for i in range(1,cuantos+1):
  n = int(input(f"Numero {i} ? "))
  suma += n
print(f"La suma es {suma}")