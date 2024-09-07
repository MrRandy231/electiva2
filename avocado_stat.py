# SALUDOS PROFESOR JUAN RESTITUYO
# RANDY JAVIER MOTA DIVISON - 2021-0812 

import pandas as pd
import matplotlib.pyplot as plt


# Carga del conjunto de datos 
data = pd.read_csv("avocado.csv")

# Obtener cuantas filas y cuantas columnas tiene el conjunto de datos:
num_rows, num_cols = data.shape

# Imprimir los resultados
print("Número de filas:", num_rows)
print("Número de columnas:", num_cols)

# Mostrar los primeros 100 registros
print(data.head(100))

# Mostrar los últimos 20 registros
print(data.tail(20))

# Obtener el precio mínimo, máximo y promedio del aguacate
min_price = data["AveragePrice"].min()
max_price = data["AveragePrice"].max()
avg_price = data["AveragePrice"].mean()

# Imprimir los resultados
print("Precio mínimo:", min_price)
print("Precio máximo:", max_price)
print("Precio promedio:", avg_price)

# Obtener los datos para las regiones siguientes: 
region1 = data[data["region"] == "Columbus"]
region2 = data[data["region"] == "Philadelphia"]
region3 = data[data["region"] == "Atlanta"]


# Creación el gráfico 
plt.scatter(region1["year"], region1["AveragePrice"], label="Columbus")
plt.scatter(region2["year"], region2["AveragePrice"], label="Philadelphia")
plt.scatter(region3["year"], region3["AveragePrice"], label="Atlanta")

# Configuración del gráfico
plt.title("Precio promedio del aguacate por año y región")
plt.xlabel("Año")
plt.ylabel("Precio promedio")
plt.legend(ncols=3)

# Mostrar el gráfico
plt.show()
