import pandas as pd

datos = {
    "nombres": ["Juan", "Lius", "Maria"],
    "materias": ["Matemáticas", "Programación", "Mercadotecnia"],
    "promedios": [80, 90, 100]
}

df_alumnos = pd.DataFrame(datos)
print(df_alumnos)
df_colesterol = pd.read_csv("https://raw.githubusercontent.com/asalber/"                            
                            "manual-python/master/datos/colesteroles.csv", sep = ";", decimal = ",")

# Principales funciones
print(df_colesterol)
print(df_colesterol.head()) # Imprime los primeros 5 renglones por defecto
print(df_colesterol.sample()) # impime 1 renglon aleatorio por defecto
print(df_colesterol.info) # imprime todos
print(df_colesterol.describe()) # descripcion estadistica general
print(df_colesterol.shape) #dimensiones
print(df_colesterol.size) # tamaño
print(df_colesterol.columns) # lista de columnas
print(df_colesterol.dtypes) # tipos de datos de cada columna
print(df_colesterol.index) # devuelve los indices
print(df_colesterol.nombre)
print(df_colesterol[["nombre","edad","colesterol"]])

df_colesterol["colesterol"].plot() # graficar