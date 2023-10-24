import pandas as pd

alumnos = {
    "nombre":["Juan","Maria","Pedro","Miguel","Anonimo"],
    "edad":[20,19,22,18,12],
    "carrera":["IN","C","NI","IN",""],
    "promedio":[90,99,70,85,100]
}

df_alumno = pd.DataFrame(alumnos)

carrera = {
    "nombre":["IN","C","NI","IN","AE","I"],
    "alumnos":[190,1000,300,2000,1500,100],
    "creditos":[352,350,360,326,340,510]
}

df_carrera = pd.DataFrame(carrera)

#MERGE INNER, LEFT, RIGHT, OUTHER
data = pd.merge(df_alumno,df_carrera, how="left", #usar inner para unir, left para unir a pesar de que no haya relación entre las tablas
                left_on="carrera", right_on="nombre",
                suffixes=("_alumnos","_carrera"))
#print(data)

alumnos2 = {
    "nombre":["Juan","Maria","Pedro","Miguel","Anonimo"],
    "edad":[20,19,22,18,12],
    "carrera":["IN","C","NI","IN",""],
    "promedio":[90,99,70,85,100]
}
#CONCATENAR
df_alumnos2 = pd.DataFrame(alumnos2)
concatenar = pd.concat([df_alumno, df_alumnos2],
                       axis="index", ignore_index=True)
#print(concatenar)

concatenar2 = pd.concat([df_alumno, df_alumnos2],
                       axis="columns")
print(concatenar2)
