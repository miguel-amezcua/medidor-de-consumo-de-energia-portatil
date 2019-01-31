import sqlite3
import os


dire =""
dire= os.getcwdb()

print("la direccion donde se esta generando la base de dato es: \n", dire)

try:
    conn = sqlite3.connect("lecturas.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE "User" (
	"id_cliente"	INTEGER,
	"usuario"	TEXT,
	"password"	TEXT,
	"canal"	NUMERIC,
	"puerto"	INTEGER,
	"dns"	REAL)''')

    print("LA BASE DE DATOS _User_ A SIDO CREADA \n ")

    conn.commit()

except sqlite3.OperationalError as error:
    print("La Base de datos User ya existe ")
cursor.close()
conn.close()

print("Podemos usarlo sin problemas")


