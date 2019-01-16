import time

import paho.mqtt.client as mqtt
import main_

a = main_.objetivo


# funcion de conexion con servidor mqtt
def on_connect(client, userdata, flags, rc):
    print("codigo funcionando:" + str(rc))  # topic entrada


def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))


def on_publish(client, userdata, mid):  # create function for callback
    print("data published mid=", mid, "\n")


def on_disconnect(client, userdata, rc):
    print("client disconnected ok")


def on_subscribe(client, userdata, mid, granted_qos):  # create function for callback
    print("subscribed with qos", granted_qos, "\n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_publish = on_publish  # assign function to callback
client.on_subscribe = on_subscribe  # assign function to callback
# client.username_pw_set =conexion().build1('usuario', 'passw')


client.username_pw_set("UMC_Jalisco", "U_ctq9$a")
# client.connect(conexion().build1('dns','puerto','60'))
client.connect("sener.ciateq.net.mx", 4000, 60)
client.subscribe("test enable")  # esta linea de codigo hace funcionar el on_message
client.loop_start()
time.sleep(1)
while True:
    client.publish("test/",a)
    time.sleep(5)
client.loop_stop()
client.disconnect()
