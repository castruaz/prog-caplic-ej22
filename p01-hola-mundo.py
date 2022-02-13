# p01- Este programa lee datos y envia un saludo

print('Programa que lee datos y envia un saludo')
nombre = input('Dame tu nombre: ') # lee cadena
edad   = int(input('Dame la edad: ')) # lee cadena y convierte a entero
peso   = float(input('Dame tu peso: ')) # lee una cadena y convierte a float
print(f"{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}")
print(type(nombre))
print(type(edad))
print(type(peso))
