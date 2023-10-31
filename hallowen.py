import pandas as pd

alumnos = {
    "nombre":["Juan","Maria","Pedro","Miguel","Juan"],
    "edad":[20,19,22,18,25],
    "carrera":["IN","C","NI","IN","A"],
    "promedio":[90,99,70,85,95]
}

#df_alumnos = pd.DataFrame(alumnos, index= ["A","B","C","D"])
df_alumnos = pd.DataFrame(alumnos)
#df_alumnos_index = df_alumnos.set_index(df_alumnos.nombre)
df_alumnos_index = df_alumnos.set_index("nombre",drop=True) #define la columna nombre como indice y elimina la original para que no se repitan columnas
#print(df_alumnos_index)

df_reset = df_alumnos_index.reset_index() #regresa el df a su formato original
#print(df_reset)
columnas = ["promedio","carrera"]
#print(df_alumnos_index.loc[["Juan","Maria"], columnas])

#print(df_alumnos_index.iloc[2,[1,2]])
print(df_alumnos_index.iloc[0:4:2,:])