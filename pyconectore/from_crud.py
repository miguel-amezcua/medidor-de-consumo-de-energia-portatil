#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os


dire =""
dire= os.getcwdb()

print("la direccion donde se esta generando la base de dato es: \n", dire)

try:
    conn = sqlite3.connect('lecturas.db')
    cursor =conn.cursor()

    cursor.execute('''CREATE TABLE lecturas_
    (ID_LECTURA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"_datetime"	INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"tension"	NUMERIC,
	"corriente"	NUMERIC,
	"corrienteMaxima"	NUMERIC,
	"potenciasActivas"	NUMERIC,
	"potenciaReactiva"	NUMERIC,
	"potenciaAparente"	NUMERIC,
	"factorPotencia"	NUMERIC,
	"factorPotenciaMini"    NUMERIC,
	"id_cliente"    NUMERIC,
	FOREIGN KEY ("id_cliente") REFERENCES User ("id_cliente"));''')

    print("LA BASE DE DATOS A SIDO CREADA \n ")
               
    conn.commit()

except sqlite3.OperationalError as error:
    print("La Base de datos ya existe ")
cursor.close()
conn.close()

print("podemos usarlo")