url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv"
import pandas as pd

datos = pd.read_csv(url)

# Imprimir todos los datos
#   print(datos)


#   colum = ['total_bill','tip','smoker','time']
#   print(datos[colum])
#   print(datos[['total_bill','day']])


#   print(datos[:5])
#   print(datos.head(5))


#   print(datos[['tip', 'sex', 'size']].head(10))



#   dinero = (datos['time'] == 'Dinner')
#   print(datos[dinero])



#Filtrar ejericio
#   data = (datos["sex"] == "Female") & (datos["day"] == "Sun")
#   print(datos[data])

#Filtrar ejericio
#   filtros = (datos['sex'] == 'Female') & (datos['day'] == 'Fri') & (datos['smoker'] == 'No')
#   print(datos[filtros])

#   dias = (datos['day'] == 'Fri') | (datos['day'] == 'Thur')
#   print(datos[dias])

# Filtrar "sex" == 'Male' y 'day' == 'Fri' o 'Thur' y 'smoker' == 'Yes' y que sean solo los 8 primeros registros
#   filtro = (datos['sex'] == 'Male') & ((datos['day'] == 'Fri') | (datos['day'] == 'Thur')) & (datos['smoker'] == 'Yes')
#   print(datos[filtro].head(8))

# Obtener booleanos de las personas fumadoras
#   smokers = datos['smoker'] == 'Yes'
#   print(datos[smokers])

#   conteos = fumadores.value_counts()
#   print(conteos)

#   print('La cantidad de fumadores es: {}'.format(conteos[1]))

#Mostrar cantidad de registros donde las personas son fumadoras y el día es domingo

#   filtro = (datos['day'] == 'Sun') & (datos['smoker'] == 'Yes')
#   contar = filtro.value_counts()
#   print('Cantidad de registros donde las personas son fumadoras y el día es domingo es: {}'.format(contar[1]))


#   booleanos = (datos['tip']>5.00) & (datos['time'] == 'Dinner')
#   print(datos[booleanos].head(10))