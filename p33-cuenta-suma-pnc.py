# cuenta suma, positivos, negativos, ceros

c=n=cp=cn=cc=s=0
while(True):
  n = int(input("Numero ?"))
  if n!=999:
    c+=1; s+=n
    if n>0:
      cp+=1
    elif n<0:
      cn+=1
    else:
      cc+=1
  else:
    break
print("Se introdujeron {0} numeros".format(c))
print("Positivos: {0}, Negativos: {1}, Ceros: {2}".format(cp,cn,cc))
print("La suma de los numeros es {0}".format(s))