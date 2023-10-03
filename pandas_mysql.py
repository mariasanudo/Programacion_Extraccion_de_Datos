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
print(cadena_conexion)

engine = create_engine(cadena_conexion)
conexion = engine.connect()
print(conexion)

