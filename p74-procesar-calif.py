# Procesar calificaciones 

# Entrada
print("Introduce calificaciones 0..9 (99 para terminar):")
nums=[]
n=0
while n!=99:
    n = float(input("Numero > "))
    if n>=0 and n<=10: 
      nums.append(n)
    else:
      print('x')
print('< fin')

# Calculos
sum=0
prom=0
for n in nums: 
  sum+=n 
prom=sum/len(nums)   
  
mp=[]
for n in nums:        
  if n>prom : 
    mp.append(n)

may=nums[0]
for n in nums:
  if n>may:
    may=n

men=nums[0]
for n in nums:
  if n<men:
    men=n


# Salida 
print(f"\nCapturaste {len(nums)} numeros")
print(f"Las numeros son : {nums}")
print("\nEstadisticas >>")
print(f"Suma             : {sum}")
print(f"Promedio         : {prom}")
print(f"Mayores promedio : {len(mp)} : {mp}")
print(f"Mayor            : {may}")
print(f"Menor            : {men}")