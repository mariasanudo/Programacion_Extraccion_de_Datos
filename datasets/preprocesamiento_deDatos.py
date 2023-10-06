import pandas as pd

datos = pd.read_csv("surveys.csv")
#print(datos)

nulos = datos.isnull() #identifica los valores nulos
#print(nulos.any()) #resumen de las columnas que tienen valores nulos
#print(nulos.sum()) #retorna el total de nulos por columna
#print(nulos.sum().sum()) #retorna la suma de todos los nulos dentro del csv
#print(nulos.sum()/len(nulos)) #porcentaje de nulos por columna

#ELIMINAR COLUMNAS
datos_eliminados = datos.drop(["day","month"], axis="columns") #crea una copia
#print(datos.columns)
#print(datos_eliminados.columns)

#ELIMINAR COLUMNAS ORIGINAL
datos_eliminados = datos.drop(["day","month"], axis="columns", inplace=True) #trabaja sobre el original
#print(datos.columns)

#ELIMINAR RENGLONES
datos_reng_elim = datos.drop([2,3,4], axis="index") #elimina los renglones indicados en la lista
#print(datos_reng_elim.head(10))

#ELIMINAR NULOS
datos_notnull = datos.dropna(axis="columns", thresh=100) #elimina las columnas con datos nulos
#print(datos_notnull)

datos_notnull = datos.dropna(axis="index") #elimina las renglones con datos nulos
#print(datos_notnull)

datos_notnull = datos.dropna(thresh=4) #elimina las renglones con datos nulos
#print(datos_notnull)
#print(len(datos))
#print(len(datos_notnull))

datos_notnull = datos.dropna(axis="index", subset=["hindfoot_length", "sex"])
#print(datos_notnull)

#LLENAR VALORES NULOS
#prom = datos.mean()
#print(prom)
datos_llenos = datos.fillna("Sin datos")
#print(datos_llenos)

columnas = ["hindfoot_length", "weight"]
promedios = datos[columnas].mean()
#print(promedios)
datos_llenos = datos.fillna(promedios)
#print(datos_llenos)

#LLENAR VALORES NULOS USANDO BFILL
datos_bfill = datos.bfill() #llena de abajo hacia arriba
#print(datos_bfill)

datos_ffill = datos.ffill() #llena de arriba hacia abajo
#print(datos_ffill)

#LLENAR DATOS NULOS MIX
datos_mix = datos.bfill().fillna(0) #combinas métodos
datos_mix = datos.bfill().ffill() #combinas métodos
#print(datos_mix)

#VERIFICAR DUPLICADOS
duplicados = datos.duplicated()
#print(duplicados)
print(len(duplicados))

duplicados = datos.duplicated(subset= ["sex","weight"]) #elimina los datos de las columnas que se repiten
#print(duplicados)

eliminar_duplicados = datos.drop_duplicates #elimina los datos duplicados

eliminar_duplicados = datos.drop_duplicates(subset= ["sex","weight"]) #elimina los datos de las columnas que se repiten
#print(len(eliminar_duplicados))

