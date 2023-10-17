import pandas as pd

data = pd.read_csv("datasets/data_olimpiadas.csv",
                   index_col=0)

#print(data)
datos_agrupados = data.groupby(["gender","year"])
#print(datos_agrupados.get_group("male"))
columnas = ["gold","silver","bronze"]
res = datos_agrupados[columnas].sum()
#print(res)

print(data.country.value_counts())