import sqlite3
import os

def ingr():

    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()
    print("Opcion Agregar")
    print("\n")
    import main_
    id_cliente =main_.id_cliente
    usuario = main_.usuario
    password =main_.password
    canal =main_.canal
    puerto = main_.puerto
    dns = main_.dns
    sentencia = "insert into User (id_cliente, usuario, password, canal, puerto, dns)values(?,?,?,?,?,?)"
    cursor.execute(sentencia, [id_cliente, usuario, password, canal, puerto, dns])
    print("Datos de conexion guardados correctamente")

    #os.system('cls')
    conn.commit()
    cursor.close()
    conn.close()

ingr()