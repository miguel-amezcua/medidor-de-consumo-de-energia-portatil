import sqlite3
import os
import time
import modbus_
a = True
while a:
    tension = modbus_.tension
    corriente = modbus_.corriente
    corrienteMaxima = modbus_.corrienteMaxima
    potenciasActivas = modbus_.potenciasActivas
    potenciaReactiva = modbus_.potenciaReactiva
    potenciaAparente = modbus_.potenciaAparente
    factorPotencia = modbus_.factorPotencia
    factorPotenciaMini = modbus_.factorPotenciaMini

    def Agregar():
        conn = sqlite3.connect('lecturas.db')
        cursor = conn.cursor()
        print("Opcion Agregar")
        print("\n")
        sentencia = "insert into lecturas_ (tension, corriente, corrienteMaxima, potenciasActivas, potenciaReactiva, potenciaAparente, factorPotencia, factorPotenciaMini)values(?,?,?,?,?,?,?,?)"
        cursor.execute(sentencia, [tension, corriente, corrienteMaxima, potenciasActivas, potenciaReactiva, potenciaAparente, factorPotencia, factorPotenciaMini])
        print ("Datos guardados correctamente")

        os.system('cls')
        conn.commit()
        cursor.close()
        conn.close()
    
        print ("\n")
        time.sleep(3)
        os.system('clear')
    #Menu()

Agregar()