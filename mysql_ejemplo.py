from mysql.connector import connect, Error

try:
    conexion = connect(host="localhost", user="root",
                       password="12345", database="olimpiadas")
    #print(conexion)
    #print(type(conexion))
    cursor = conexion.cursor()
    #mysql = "INSERT INTO GENERO(nombre) VALUES ('Masculino')"
    mysql = "INSERT INTO GENERO(nombre) VALUES (%s)" #Se agrega el comando que se ejecutará en mysql

    #mysql = "UPDATE GENERO SET NOMBRE = %s WHERE ID = %s"
    #valores = [("Femenino", "2"), ("Masculino", )]  -- sustitucion
    #cursor.execute(sql, valores)

    """valores = ("Femenino", )
    cursor.execute(mysql, valores)"""

    #sql = "SELECT *FROM GENERO"
    #cursos.execute(sql)
    #conexion.commit()

    valores = [("Femenino", ), ("Masculino", )]
    cursor.executemany(mysql, valores)
    conexion.commit()

    print(cursor.lastrowid)
    """
    sql = "show databases"
    cursor.execute(sql)
    lista_datos = cursor.fetchall()
    for item in lista_datos:
        print(item)
    #print(cursor)
    """
except Error as e:
    print(f"ERROR {e}")
