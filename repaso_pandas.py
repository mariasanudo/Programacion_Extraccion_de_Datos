import pandas as pd # pd es para acortar la sintaxis

datos = {"Articulo":["Coca-cola","Tostitos","Cheetos","Jugo"],
         "Precio": [20, 35, 20, 22],
         "Costo": [8, 17, 10, 11],
         "Categoria": ["Bebida", "Botana", "Botana", "Bebida"]}

data = pd.DataFrame(datos) #es como un objeto
#print(data)

art = [
    ["Coca-cola", 20, 8, "Bebida"],
    ["Tostitos", 35, 17, "Botana"],
    ["Cheetos", 20, 10, "Botana"],
    ["Jugo", 22, 11, "Bebida"]
]

data2 = pd.DataFrame(art, columns=["Ariculo", "Precio", "Costo", "Categoria"])
#print(data2)

#print(type(data.Articulo))
#print(data["Articulo"])

columnas = ["Articulo","Precio"]
#print(data[columnas])

""" 
index    Articulo    Precio  Costo Categoria
0        Coca-cola      20      8    Bebida
1        Tostitos       35     17    Botana
2        Cheetos        20     10    Botana
3        Jugo           22     11    Bebida
"""

#Calcular las utilidades de cada producto (precio - costo)
utilidad = data.Precio - data.Costo
#Insertar otra columna
data["Utilidad"] = utilidad
#print(data)

"""
#Calcular que articulo o articulos tienen el precio maximo
maximo = max(data.Precio)
#print(maximo)
filtro = data.Precio == maximo
#print(data[filtro][columnas])
"""

#Calcular que articulo o articulos tienen el precio mayor de la categoria bebidas
data_filtrado = data[data.Categoria == "Bebida"]
#print(data_filtrado)
#filtro2 = data_filtrado.Precio == maximo2
#print(data_filtrado[filtro][columnas])
maximo2 = data_filtrado.Precio.max()
filtro = (data.Precio == maximo2) & (data.Categoria == "Bebida")
#print(data[filtro][columnas])

#alcular, maximo, minimo y promedio de las columnas precio y costo, y devolverlo en un dataframe
columnas2 = ["Precio", "Costo"]
maximos = data[columnas2].max()
minimos = data[columnas2].min()
promedios = data[columnas2].mean()
#print(f"{maximos}\n{minimos}\n{promedios}")
res = pd.DataFrame([maximos,minimos,promedios], index=["Maximo","Minimo","Promedio"])
print(res)
