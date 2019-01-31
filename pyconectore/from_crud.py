#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os

dire = ""
dire = os.getcwdb()

print("la direccion donde se esta generando la base de dato es: \n", dire)

try:
    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE lecturas_
    (ID_LECTURA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"_datetime"	INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "vAB"	NUMERIC,
    "vBC"	NUMERIC,
    "vCA"	NUMERIC,
    "vLT"	NUMERIC,
    "vAN"	NUMERIC,
    "vBN"	NUMERIC,
    "vCN"	NUMERIC,
    "vNT"	NUMERIC,
    "cA"	NUMERIC,
    "cB"	NUMERIC,
    "cC"    NUMERIC,
    "cT"	NUMERIC,
    "cMaxA"	NUMERIC,
    "cMaxB"	NUMERIC,
    "cMaxC"	NUMERIC,
    "cMaxT"	NUMERIC,
    "paA"	NUMERIC,
    "paB"	NUMERIC,
    "paC"	NUMERIC,
    "paT"	NUMERIC,
    "prA"	NUMERIC,
    "prB"	NUMERIC,
    "prC"	NUMERIC,
    "prT"	NUMERIC,
    "papA"	NUMERIC,
    "papB"	NUMERIC,
    "papC"	NUMERIC,
    "papT"	NUMERIC,
    "fpA"	NUMERIC,
    "fpB"	NUMERIC,
    "fpC"	NUMERIC,
    "fpT"	NUMERIC,
    "fpMinA"	NUMERIC,
    "fpMinB"	NUMERIC,
    "fpMinC"	NUMERIC,
    "fpMin"	NUMERIC,
    "fr"	NUMERIC,
	"thdvA"	NUMERIC,
    "thdvB"	NUMERIC,
    "thdvC"	NUMERIC,
    "thdvAN"	NUMERIC,
    "thdvBN"	NUMERIC,
    "thdvCN"	NUMERIC,
    "thdcA"	NUMERIC,
    "thdcB"	NUMERIC,
    "thdcC"	NUMERIC,
    "thdvMaxAN"	NUMERIC,
    "thdvMaxBN"	NUMERIC,
    "thdvMaxCN"	NUMERIC,
    "thdcMaxA"	NUMERIC,
    "thdcMaxB"	NUMERIC,
    "thdcMaxC"	NUMERIC,
    "vMaxAN"	NUMERIC,
    "vMaxBN"	NUMERIC,
    "vMaxCN"	NUMERIC,
    "vMaxTLN"	NUMERIC,    
    "vMaxAB"	NUMERIC,
    "vMaxBC"	NUMERIC,
    "vMaxCA"	NUMERIC,
    "vMaxTL"	NUMERIC,
    "vMinAN"	NUMERIC,
    "vMinBN"	NUMERIC,
    "vMinCN"	NUMERIC,
    "vMinTLN"	NUMERIC,
    "vMinAB"	NUMERIC,
    "vMinBC"	NUMERIC,
    "vMinCA"	NUMERIC,
    "vMinTL"	NUMERIC);''')

    print("LA BASE DE DATOS A SIDO CREADA \n ")

    conn.commit()

except sqlite3.OperationalError as error:
    print("La Base de datos lecturas_ ya existe ")
cursor.close()
conn.close()

print("podemos usarlo")
