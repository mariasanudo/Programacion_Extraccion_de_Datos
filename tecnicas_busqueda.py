import pandas as pd

alumnos = {
    "nombre":["Juan","Maria","Pedro","Miguel"],
    "edad":[20,19,22,18],
    "carrera":["IN","C","NI","IN"],
    "promedio":[90,99,70,85]
}

df_alumno = pd.DataFrame(alumnos)

#TECNICA 1. FILTRADO DE DATOS
c1 = df_alumno.promedio > 80
data_c1 = df_alumno[c1]
#print(data_c1)

#c2 = (df_alumno.promedio > 80) & (df_alumno.carrera == "IN")
c2 = (df_alumno.promedio > 80) & (df_alumno.carrera.isin(["IN","C"])) #isin verifica que la condicion se encuentre dentro de el conjunto
#data_c2 = df_alumno[c2] #los corchetes representan la aplicacion de un filtro
#data_c2 = df_alumno[c2][["nombre","carrera"]] #el agregar una lista de columnas que le permita desplegar solo las columnas seleccionadas
columnas = ["nombre","carrera"]
data_c2 = df_alumno[c2][columnas]
print(data_c2)

#TECNICA 2. BUSQUEDA POR QUERY
q1_c1 = df_alumno.query("promedio > 80")
#print(q1_c1)

#q2_c2 = df_alumno.query("promedio > 80 and carrera == 'IN'")
#print(q2_c2)

condicion = "promedio > 80 and carrera.isin(['IN','C'])" #LAS COMILLAS SIMPLES PERMITEN IDENTIFICAR LOS CONTENIDOS DE LAS COLUMNAS
q2_c2 = df_alumno.query(condicion)
print(q2_c2[columnas])
