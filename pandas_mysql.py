import pandas as pd
from sqlalchemy import create_engine
from enum import Enum

class DataBD(Enum):
    USER = "root"
    PASSWORD = "12345"
    NAME_BD = "olimpiadas"
    SERVER = "localhost"

""" #Despliega las constantes 
for item in DataBD:
    print(item.name, item.value)
"""

cadena_conexion = f"mysql+mysqlconnector://{DataBD.USER.value}:{DataBD.PASSWORD.value}@{DataBD.SERVER.value}/{DataBD.NAME_BD.value}"
#print(cadena_conexion)

engine = create_engine(cadena_conexion)
conexion = engine.connect()
#print(conexion)

data_oli = pd.read_csv("datasets/data_olimpiadas.csv", index_col=0)
#print(data_oli.sample(5))

gender = data_oli.gender.unique()
#print(gender)

df_genders = pd.DataFrame(gender, columns=["nombre"])
#print(df_genders)
#df_genders.to_sql("genero", conexion,if_exists= "append", index=False)

#query = "select nombre from genero where nombre = 'female'"
query = "select nombre from genero where nombre = %s"
parametros = ("female",)
resultados = pd.read_sql(query, conexion, params=parametros)
print(resultados)
