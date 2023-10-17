import numpy as np
import pandas as pd

data = pd.read_csv("datasets/data_olimpiadas.csv",
                   index_col=0)

#print(data)
datos_agrupados = data.groupby(["gender","year"])
#print(datos_agrupados.get_group("male"))
columnas = ["gold","silver","bronze"]
res = datos_agrupados[columnas].sum()
#print(res)

#print(data.country.value_counts())
#print(data.sort_values("year"))
#print(data.sort_values("year",ascending=False))

#print(datos_agrupados.mean(numeric_only=True))

#print(data.describe().transpose())
grupos = data.groupby(["gender","country"])
grupos_gender = data.groupby("gender")
#print(grupos_gender.sample(5))
#print(grupos_gender.gold.mean())
#print(grupos.gold.mean().unstack().transpose())
#print(grupos.gold.mean().unstack())
#print(grupos.gold.mean())

print(data.pivot_table("gold", index="gender", columns="year", margins=True, aggfunc=np.sum))
