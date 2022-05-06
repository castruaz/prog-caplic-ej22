import pandas as pd

# Leer archivo de datos (datos de viviendas por estado)
datos = pd.read_csv('vivienda.csv',header=None, index_col=0).squeeze(1)
datos.name = 'Vivienda'

# toda la seria
print('Orden orginal', datos, '\n')
print('Orden inverso', datos[::-1], '\n')
print('Orden ascendente  por indice', datos.sort_index(ascending=True), '\n')
print('Orden descendente por valor', datos.sort_values(ascending=False), '\n')

# atributos de la serie
print('Los atributos de la serie: \n')
print(f'Nombre: {datos.name}, Tamano: {datos.size}, Tipo: {datos.dtype}, Bytes: {datos.nbytes}, Tamano de dato: {datos.nbytes / datos.size}')

# iterar sobre la serie
print('Iterando sobre los valores de la serie \n')
for m, v in datos.items():
    print(f'El municipio de {m} tiene un total de {v} viviendas')

# Acceso por indice numerico
print('Ejemplos de acceso a datos por indice numerico\n')
print('Los primeros 5    ', datos[:5], '\n')
print('Los ultimos 5     ', datos[-5:], '\n')
print('Consecutivos      ', datos[4:9], '\n')
print('Salteados         ', datos[[5,10,15,20]], '\n')

# Acceso por indice alfabetico
print('Ejemplos de acceso a datos por indice numerico\n')
print('Los primeros 5    ', datos[:'Calera'], '\n')
print('Los ultimos 5     ', datos['Villa Hidalgo':], '\n')
print('Consecutivos      ', datos['Jalpa':'Loreto'], '\n')
print('Salteados         ', datos[['Jerez','Fresnillo','Calera','Pinos']], '\n')

# Filatrar
print('Ejemplos de acceso a datos filatrando\n')
print('Los primeros 5    ', datos.head(5), '\n')
print('Los ultimos 5     ', datos.tail(5), '\n')
print('Con valor > 5000  ', datos[datos > 5000] , '\n')
print('Con valor en rango 100 .. 1000  ', datos[(datos>=100) & (datos<=1000)] , '\n')

# Estadisticas
print('Estadstica descriptiva con los datos de la serie')
print('Resumen descriptivo', datos.describe(), '\n')
print(f'Media: {datos.mean()}, Desviacion:{datos.std()}, Maximo: {datos.max()}, Minimo: {datos.min()} ')
print(f'Q25:{datos.quantile(q=0.25)}, Q50: {datos.quantile(q=0.50)}, Q75: {datos.quantile(q=0.75)}')
print('Moda: ', datos.mode(),'\n')

# Operaciones
print('Operaciones con los datos de la serie \n')
print('Suma de todos     :', datos.sum(), '\n')
print('Suma primeros 10  :', datos.head(10).sum(), '\n' )
print('Meda saltados     :', datos[['Zacatecas','Fresnillo','Guadalupe']].mean(), '\n') 
print('Modulo 20 a todos :', datos.divmod(20), '\n')
print('Sumar 100 a todos :', datos+100, '\n' )
