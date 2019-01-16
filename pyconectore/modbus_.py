from pymodbus.client.sync import ModbusTcpClient
from pyModbusTCP.client import ModbusClient
import sqlite3
import os
import time

tension = 0
corriente= 0
corrienteMaxima= 0
potenciasActivas=0
potenciaReactiva= 0
potenciaAparente= 0
factorPotencia= 0
factorPotenciaMini= 0


try:
    c = ModbusClient(host="127.16.5.16", port=502)
    print("connected a puerto")
    a = True
    increment = 0
    while a:
        if c.is_open():

            print("inicio del siclo")
            regs_list_1 = c.read_holding_registers(0, 10)
            regs_list_2 = c.read_holding_registers(55, 10)
        else:
            c.open()
            print("abriendo puerto cerrado para bucle while")
            increment = increment + 1
            if (increment == 10):
                a = False

        time.sleep(1)

    c.debug(True)

    print(c.read_holding_registers(0, 4))
except ValueError:
    print("Error with host or port params")

a = True
increment =0
while a:
    if c.is_open():

        print("inicio del siclo 2")
        regs_list_1 = c.read_holding_registers(0, 10)
        regs_list_2 = c.read_holding_registers(55, 10)
    else:
        c.open()
        print("abriendo puerto cerrado para bucle while 2")
        increment = increment+1
        if (increment==10):
            a = False

    time.sleep(1)
c = ModbusClient(host="127.16.5.16", port=502)
c.debug(True)

print(c.read_holding_registers(0, 4))

def entrada():
    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()
    print("Opcion Agregar")
    print("\n")



    os.system('cls')
    conn.commit()
    cursor.close()
    conn.close()
