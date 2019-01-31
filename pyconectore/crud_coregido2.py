import sqlite3
import os
import time
import modbus22
a = True
while a:

    vAB = modbus22.vAB
    vBC = modbus22.vBC
    vCA = modbus22.vCA
    vLT = modbus22.vLT
    vAN = modbus22.vAN
    vBN = modbus22.vBN
    vCN = modbus22.vCN
    vNT = modbus22.vNT
    cA = modbus22.cA
    cB = modbus22.cB
    cC = modbus22.cC
    cT = modbus22.cT
    cMaxA = modbus22.cMaxA
    cMaxB = modbus22.cMaxB
    cMaxC = modbus22.cMaxC
    cMaxT = modbus22.cMaxT
    paA = modbus22.paA
    paB = modbus22.paB
    paC = modbus22.paC
    paT = modbus22.paT
    prA = modbus22.prA
    prB = modbus22.prB
    prC = modbus22.prC
    prT = modbus22.prT
    papA = modbus22.papA
    papB = modbus22.papB
    papC = modbus22.papC
    papT = modbus22.papT
    fpA = modbus22.fpA
    fpB = modbus22.fpB
    fpC = modbus22.fpC
    fpT = modbus22.fpT
    fpMinA = modbus22.fpMinA
    fpMinB = modbus22.fpMinB
    fpMinC = modbus22.fpMinC
    fpMin = modbus22.fpMin
    fr = modbus22.fr
    thdvA = modbus22.thdvA
    thdvB = modbus22.thdvB
    thdvC = modbus22.thdvC
    thdvAN = modbus22.thdvAN
    thdvBN = modbus22.thdvBN
    thdvCN = modbus22.thdvCN
    thdcA = modbus22.thdcA
    thdcB = modbus22.thdcB
    thdcC = modbus22.thdcC
    thdvMaxAN = modbus22.thdvMaxAN
    thdvMaxBN = modbus22.thdvMaxBN
    thdvMaxCN = modbus22.thdvMaxCN
    thdcMaxA = modbus22.thdcMaxA
    thdcMaxB = modbus22.thdcMaxB
    thdcMaxC = modbus22.thdcMaxC
    vMaxAN = modbus22.vMaxAN
    vMaxBN = modbus22.vMaxBN
    vMaxCN = modbus22.vMaxCN
    vMaxTLN = modbus22.vMaxTLN
    vMaxAB = modbus22.vMaxAB
    vMaxBC = modbus22.vMaxBC
    vMaxCA = modbus22.vMaxCA
    vMaxTL = modbus22.vMaxTL
    vMinAN = modbus22.vMinAN
    vMinBN = modbus22.vMinBN
    vMinCN = modbus22.vMinCN
    vMinTLN = modbus22.vMinTLN
    vMinAB = modbus22.vMinAB
    vMinBC = modbus22.vMinBC
    vMinCA = modbus22.vMinCA
    vMinTL = modbus22.vMinTL

    def Agregar():
        conn = sqlite3.connect('lecturas.db')
        cursor = conn.cursor()
        print("Opcion Agregar")
        #print(" prueba de lectura de variables \n", vAB)
        sentencia = "insert into lecturas_ (vAB, vBC, vCA, vLT, vAN, vBN, vCN, vNT, cA, cB, cC, cT, cMaxA, cMaxB, cMaxC, cMaxT, paA, paB, paC, paT, prA, prB, prC, prT, papA, papB, papC, papT, fpA, fpB, fpC, fpT, fpMinA, fpMinB, fpMinC, fpMin, fr, thdvA, thdvB, thdvC, thdvAN, thdvBN, thdvCN, thdcA, thdcB, thdcC, thdvMaxAN, thdvMaxBN, thdvMaxCN, thdcMaxA, thdcMaxB, thdcMaxC, vMaxAN, vMaxBN, vMaxCN, vMaxTLN, vMaxAB, vMaxBC, vMaxCA, vMaxTL, vMinAN, vMinBN, vMinCN, vMinTLN, vMinAB, vMinBC, vMinCA, vMinTL)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sentencia, [vAB, vBC, vCA, vLT, vAN, vBN, vCN, vNT, cA, cB, cC, cT, cMaxA, cMaxB, cMaxC, cMaxT, paA, paB, paC, paT, prA, prB, prC, prT, papA, papB, papC, papT, fpA, fpB, fpC, fpT, fpMinA, fpMinB, fpMinC, fpMin, fr, thdvA, thdvB, thdvC, thdvAN, thdvBN, thdvCN, thdcA, thdcB, thdcC, thdvMaxAN, thdvMaxBN, thdvMaxCN, thdcMaxA, thdcMaxB, thdcMaxC, vMaxAN, vMaxBN, vMaxCN, vMaxTLN, vMaxAB, vMaxBC, vMaxCA, vMaxTL, vMinAN, vMinBN, vMinCN, vMinTLN, vMinAB, vMinBC, vMinCA, vMinTL])
        print ("Datos guardados correctamente")

        os.system('cls')
        conn.commit()
        cursor.close()
        conn.close()
    
        print ("\n")
        time.sleep(3)
        os.system('clear')
    Agregar()