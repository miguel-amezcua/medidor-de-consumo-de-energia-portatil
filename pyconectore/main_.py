#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyModbusTCP.client import ModbusClient
import time
import paho.mqtt.client as mqtt
from dateutil import parser
import matplotlib.pyplot as plt
import json
#from kivy.clock import  mainthread
import sqlite3
import paho.mqtt.client as mqtt
host = ""
modbus = 0
dns = 0
usuario = ""
id_cliente = 0
password = ""
canal = 75
puerto = 0
LECTURAS = 1
value = False
objetivo = 1

def inicio():
    import Bienvenida

def bienv():
    import from_crud
    import from_user
    #print('hecho', id_cliente,",", usuario,",", password,",", canal)
    import user_ing

def on_conexion():
    print("estoy aqui me reconoces ????")
    def on_connect(client, userdata, flags, rc):
        print("codigo funcionando:" + str(rc))
    def on_publish(client, userdata, mid):  # create function for callback
        print("data published mid=", mid, "\n")
    def on_disconnect(client, userdata, rc):
        print("client disconnected ok")
    def on_subscribe(client, userdata, mid, granted_qos):  # create function for callback
        print("subscribed with qos", granted_qos, "\n")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish  # assign function to callback
    client.on_subscribe = on_subscribe
    client.username_pw_set("UMC_Jalisco", "U_ctq9$a")
    client.connect("sener.ciateq.net.mx", 4001, 60)
    client.subscribe("test/#")  # esta linea de codigo hace funcionar el on_message
    client.loop_start()
    time.sleep(1)
    try:
        client.publish("test/", "iniciando con MQTT con ip nueva :")
        time.sleep(1)
        try:
            c = ModbusClient(host="127.16.5.16", port=502)
            print("connected a puerto")
            value = True
        except ValueError:
            print("Error with host or port params")
            value = False
    except ValueError:
        def error_entrada():
            value = False
    client.loop_stop()
    client.disconnect()




def grafico():
    import graficas
    dataten = graficas.graf1()
    datacor = graficas.graf2()
    datacorMax = graficas.graf3()
    datapotact = graficas.graf4()
    datapotrea = graficas.graf5()
    datapotapa = graficas.graf6()
    datafacpot = graficas.graf7()
    datafacpotm = graficas.graf8()
    pass

def mqtt_():
    while True:
        import export
        LECTURAS
        objetivo = export.export_db()
        print("en json ", objetivo)
        LECTURAS = LECTURAS+1
        time.sleep(15)

def modbus_():

    print ('desecho',"," ,dns,",", id_cliente,",",canal,",", usuario)

def suport():

    dataten = Bienvenida.tensio
    dates = []
    values = []
    for row in dataten:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, 'x-')
    plt.ylabel('Tencion')
    plt.xlabel('Tiempo')
    box = BoxLayout()
    plt.show()
    #return box
    import Bienvenida.tensio

inicio()