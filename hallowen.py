import pandas as pd

alumnos = {
    "nombre":["Juan","Maria","Pedro","Miguel"],
    "edad":[20,19,22,18],
    "carrera":["IN","C","NI","IN"],
    "promedio":[90,99,70,85]
}

#df_alumnos = pd.DataFrame(alumnos, index= ["A","B","C","D"])
df_alumnos = pd.DataFrame(alumnos)
df_alumnos_index = df_alumnos.set_index(df_alumnos.nombre)
print(df_alumnos_index)