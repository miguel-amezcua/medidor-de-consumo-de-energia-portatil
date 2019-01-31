from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time
import paho.mqtt.client as mqtt
import json
import time

SERVER_HOST = "172.16.5.16"
SERVER_PORT = 502

c = ModbusClient()

c.host(SERVER_HOST)
c.port(SERVER_PORT)
#c.debug(True)
relog =1

if not c.is_open():
    if not c.open():
        print("conexion establecida con "+SERVER_HOST+":"+str(SERVER_PORT))

if c.is_open():
    print("antes de la vuelta", relog)

    print("inicio del siclo")
    regs_list_1 = c.read_holding_registers(3021, 2)
    if regs_list_1:
        vAB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_1)]
    regs_list_2 = c.read_holding_registers(3023, 2)
    if regs_list_2:
        vBC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_2)]
        print("valor de retorno 2 vBC" + str(vBC))
    regs_list_3 = c.read_holding_registers(3025, 2)
    if regs_list_3:
        vCA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_3)]
    regs_list_4 = c.read_holding_registers(3027, 2)
    if regs_list_4:
        vLT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_4)]
    regs_list_5 = c.read_holding_registers(3029, 2)
    if regs_list_5:
        vAN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_5)]
    regs_list_6 = c.read_holding_registers(3031, 2)
    if regs_list_6:
        vBN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_6)]
    regs_list_7 = c.read_holding_registers(3033, 2)
    if regs_list_7:
        vCN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_7)]
    regs_list_8 = c.read_holding_registers(3037, 2)
    if regs_list_8:
        vNT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_8)]
    regs_list_9 = c.read_holding_registers(3001, 2)
    if regs_list_9:
        cA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_9)]
    regs_list_10 = c.read_holding_registers(3003, 2)
    if regs_list_10:
        cB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_10)]

    regs_list_11 = c.read_holding_registers(3005, 2)
    if regs_list_11:
        cC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_11)]
    regs_list_12 = c.read_holding_registers(3011, 2)
    if regs_list_12:
        cT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_12)]
    regs_list_13 = c.read_holding_registers(27695, 2)
    if regs_list_13:
        cMaxA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_13)]
    regs_list_14 = c.read_holding_registers(27697, 2)
    if regs_list_14:
        cMaxB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_14)]
    regs_list_15 = c.read_holding_registers(27699, 2)
    if regs_list_15:
        cMaxC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_15)]
    regs_list_16 = c.read_holding_registers(27705, 2)
    if regs_list_16:
        cMaxT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_16)]
    regs_list_17 = c.read_holding_registers(3055, 2)
    if regs_list_17:
        paA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_17)]
    regs_list_18 = c.read_holding_registers(3057, 2)
    if regs_list_18:
        paB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_18)]
    regs_list_19 = c.read_holding_registers(3059, 2)
    if regs_list_19:
        paC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_19)]
    regs_list_20 = c.read_holding_registers(3061, 2)
    if regs_list_20:
        paT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_20)]
    regs_list_21 = c.read_holding_registers(3063, 2)
    if regs_list_21:
        prA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_21)]
    regs_list_22 = c.read_holding_registers(3065, 2)
    if regs_list_22:
        prB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_22)]
    regs_list_23 = c.read_holding_registers(3067, 2)
    if regs_list_23:
        prC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_23)]
    regs_list_24 = c.read_holding_registers(3069, 2)
    if regs_list_24:
        prT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_24)]
    regs_list_25 = c.read_holding_registers(3071, 2)
    if regs_list_25:
        papA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_25)]
        print("valor de retorno 25 papA" + str(vBC))
    regs_list_26 = c.read_holding_registers(3073, 2)
    if regs_list_26:
        papB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_26)]
    regs_list_27 = c.read_holding_registers(3075, 2)
    if regs_list_27:
        papC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_27)]
    regs_list_28 = c.read_holding_registers(3077, 2)
    if regs_list_28:
        papT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_28)]
    regs_list_29 = c.read_holding_registers(3079, 2)
    if regs_list_29:
        fpA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_29)]
    regs_list_30 = c.read_holding_registers(3081, 2)
    if regs_list_30:
        fpB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_30)]
    regs_list_31 = c.read_holding_registers(3083, 2)
    if regs_list_31:
        fpC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_31)]
    regs_list_32 = c.read_holding_registers(3085, 2)
    if regs_list_32:
        fpT = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_32)]
    regs_list_33 = c.read_holding_registers(27307, 2)
    if regs_list_33:
        fpMinA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_33)]
    regs_list_34 = c.read_holding_registers(27309, 2)
    if regs_list_34:
        fpMinB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_34)]
    regs_list_35 = c.read_holding_registers(27311, 2)
    if regs_list_35:
        fpMinC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_35)]
    regs_list_36 = c.read_holding_registers(27313, 2)
    if regs_list_36:
        fpMin = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_36)]
    regs_list_37 = c.read_holding_registers(3011, 2)
    if regs_list_37:
        fr = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_37)]
    regs_list_38 = c.read_holding_registers(21323, 2)
    if regs_list_38:
        thdvA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_38)]
    regs_list_39 = c.read_holding_registers(21325, 2)
    if regs_list_39:
        thdvB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_39)]
    regs_list_40 = c.read_holding_registers(21327, 2)
    if regs_list_40:
        thdvC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_40)]
    regs_list_41 = c.read_holding_registers(21331, 2)
    if regs_list_41:
        thdvAN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_41)]
    regs_list_42 = c.read_holding_registers(21333, 2)
    if regs_list_42:
        thdvBN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_42)]
    regs_list_43 = c.read_holding_registers(21335, 2)
    if regs_list_43:
        thdvCN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_43)]
    regs_list_44 = c.read_holding_registers(21301, 2)
    if regs_list_44:
        thdcA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_44)]
    regs_list_45 = c.read_holding_registers(21303, 2)
    if regs_list_45:
        thdcB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_45)]
    regs_list_46 = c.read_holding_registers(21305, 2)
    if regs_list_46:
        thdcC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_46)]
    regs_list_47 = c.read_holding_registers(27845, 2)
    if regs_list_47:
        thdvMaxAN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_47)]
    regs_list_48 = c.read_holding_registers(27847, 2)
    if regs_list_48:
        thdvMaxBN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_48)]
    regs_list_49 = c.read_holding_registers(27849, 2)
    if regs_list_49:
        thdvMaxCN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_49)]
    regs_list_50 = c.read_holding_registers(27837, 2)
    if regs_list_50:
        thdcMaxA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_50)]
    regs_list_51 = c.read_holding_registers(27839, 2)
    if regs_list_51:
        thdcMaxB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_51)]
    regs_list_52 = c.read_holding_registers(27841, 2)
    if regs_list_52:
        thdcMaxC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_52)]
    regs_list_53 = c.read_holding_registers(27723, 2)
    if regs_list_53:
        vMaxAN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_53)]
    regs_list_54 = c.read_holding_registers(27725, 2)
    if regs_list_54:
        vMaxBN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_54)]
    regs_list_55 = c.read_holding_registers(27727, 2)
    if regs_list_55:
        vMaxCN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_55)]
    regs_list_56 = c.read_holding_registers(27731, 2)
    if regs_list_56:
        vMaxTLN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_56)]
    regs_list_57 = c.read_holding_registers(27723, 2)
    if regs_list_57:
        vMaxAB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_57)]
    regs_list_58 = c.read_holding_registers(27725, 2)
    if regs_list_58:
        vMaxBC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_58)]
    regs_list_59 = c.read_holding_registers(27727, 2)
    if regs_list_59:
        vMaxCA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_9)]
    regs_list_60 = c.read_holding_registers(32731, 2)
    if regs_list_60:
        vMaxTL = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_60)]
    regs_list_61 = c.read_holding_registers(27247, 2)
    if regs_list_61:
        vMinAN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_61)]
    regs_list_62 = c.read_holding_registers(27249, 2)
    if regs_list_62:
        vMinBN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_62)]
    regs_list_63 = c.read_holding_registers(27251, 2)
    if regs_list_63:
        vMinCN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_63)]
    regs_list_64 = c.read_holding_registers(27255, 2)
    if regs_list_64:
        vMinTLN = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_64)]
    regs_list_65 = c.read_holding_registers(27239, 2)
    if regs_list_65:
        vMinAB = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_65)]
    regs_list_66 = c.read_holding_registers(27241, 2)
    if regs_list_66:
        vMinBC = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_66)]
    regs_list_67 = c.read_holding_registers(27243, 2)
    if regs_list_67:
        vMinCA = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_67)]
    regs_list_68 = c.read_holding_registers(27245, 2)
    if regs_list_68:
        vMinTL = [utils.decode_ieee(f) for f in utils.word_list_to_long(regs_list_68)]
        print("valor de retorno 68 vMinTL " + str(vMinTL))
    time.sleep(1)


    print("fin de la vuelta  ", relog)


time.sleep(1)
relog = relog +1
c.close()
dato = "{\n\t[\n\t{vAB:"+str(vAB)+",\nvBC:"+str(vBC)+",\nvCA:"+str(vCA)+",\nvLT:"+str(vLT)+",\nvAN:"+str(vAN)+",\nvBN:"+str(vBN)+",\nvCN:"+str(vCN)+",\nvNT:"+str(vNT)+",\ncA:"+str(cA)+",\ncB:"+str(cB)+",\ncC:"+str(cC)+",\ncT:"+str(cT)+",\ncMaxA:"+str(cMaxA)+",\ncMaxB:"+str(cMaxB)+",\ncMaxC:"+str(cMaxC)+",\ncMaxT:"+str(cMaxT)+",\npaA:"+str(paA)+",\npaB:"+str(paB)+",\npaC:"+str(paC)+",\npaT:"+str(paT)+",\nprA:"+str(prA)+",\nprB:"+str(prB)+",\nprC:"+str(prC)+",\nprT:"+str(prT)+",\npapA:"+str(papA)+",\npapB:"+str(papB)+",\npapC:"+str(papC)+",\npapT:"+str(papT)+",\nfpA:"+str(fpA)+",\nfpB:"+str(fpB)+",\nfpC:"+str(fpC)+",\nfpT:"+str(fpT)+",\nfpMinA:"+str(fpMinA)+",\nfpMinB:"+str(fpMinB)+",\nfpMinC:"+str(fpMinC)+",\nfpMin:"+str(fpMin)+",\nfr:"+str(fr)+",\nthdvA:"+str(thdvA)+",\nthdvB:"+str(thdvB)+",\nthdvC:"+str(thdvC)+",\nthdvAN:"+str(thdvAN)+",\nthdvBN:"+str(thdvBN)+",\nthdvCN:"+str(thdvCN)+",\nthdcA:"+str(thdcA)+",\nthdcB:"+str(thdcB)+",\nthdcC:"+str(thdcC)+",\nthdvMaxAN:"+str(thdvMaxAN)+",\nthdvMaxBN:"+str(thdvMaxBN)+",\nthdvMaxCN:"+str(thdvMaxCN)+",\nthdvMaxA:"+str(thdcMaxA)+",\nthdvMaxB:"+str(thdcMaxB)+",\nthdvMaxC:"+str(thdcMaxC)+",\nvMaxAN:"+str(vMaxAN)+",\nvMaxBN:"+str(vMaxBN)+",\nvMaxCN:"+str(vMaxCN)+",\nvMaxTLN:"+str(vMaxTLN)+",\nvMaxAB:"+str(vMaxAB)+",\nvMaxBC:"+str(vMaxBC)+",\nvMaxCA:"+str(vMaxCA)+",\nvMaxTL:"+str(vMaxTL)+",\nvMinAN:"+str(vMinAN)+",\nvMinBN:"+str(vMinBN)+",\nvMinCN:"+str(vMinCN)+",\nvMinTLN:"+str(vMinTLN)+",\nvMinAB:"+str(vMinAB)+",\nvMinBC:"+str(vMinBC)+",\nvMinCA:"+str(vMinCA)+",\nvMinTL:"+str(vMinTL)+"}\n]\n}"
jsondato = {
    "vAB": str(vAB),
    "vBC": str(vBC),
    "vCA": str(vCA),
    "vLT": str(vLT),
    "vAN": str(vAN),
    "vBN": str(vBN),
    "vCN": str(vCN),
    "vNT": str(vNT),
    "cA": str(cA),
    "cB": str(cB),
    "cC": str(cC),
    "cT": str(cT),
    "cMaxA": str(cMaxA),
    "cMaxB": str(cMaxB),
    "cMaxC": str(cMaxC),
    "cMaxT": str(cMaxT),
    "paA": str(paA),
    "paB": str(paB),
    "paC": str(paC),
    "paT": str(paT),
    "prA": str(prA),
    "prB": str(prB),
    "prC": str(prC),
    "prT": str(prT),
    "papA": str(papA),
    "papB": str(papB),
    "papC": str(papC),
    "papT": str(papT),
    "fpA": str(fpA),
    "fpB": str(fpB),
    "fpC": str(fpC),
    "fpT": str(fpT),
    "fpMinA": str(fpMinA),
    "fpMinB": str(fpMinB),
    "fpMinC": str(fpMinC),
    "fpMin": str(fpMin),
    "fr": str(fr),
    "thdvA": str(thdvA),
    "thdvB": str(thdvB),
    "thdvC": str(thdvC),
    "thdvAN": str(thdvAN),
    "thdvBN": str(thdvBN),
    "thdvCN": str(thdvCN),
    "thdcA": str(thdcA),
    "thdcB": str(thdcB),
    "thdcC": str(thdcC),
    "thdvMaxAN": str(thdvMaxAN),
    "thdvMaxBN": str(thdvMaxBN),
    "thdvMaxCN": str(thdvMaxCN),
    "thdvMaxA": str(thdcMaxA),
    "thdvMaxB": str(thdcMaxB),
    "thdvMaxC": str(thdcMaxC),
    "vMaxAN": str(vMaxAN),
    "vMaxBN": str(vMaxBN),
    "vMaxCN": str(vMaxCN),
    "vMaxTLN": str(vMaxTLN),
    "vMaxAB": str(vMaxAB),
    "vMaxBC": str(vMaxBC),
    "vMaxCA": str(vMaxCA),
    "vMaxTL": str(vMaxTL),
    "vMinAN": str(vMinAN),
    "vMinBN": str(vMinBN),
    "vMinCN": str(vMinCN),
    "vMinTLN": str(vMinTLN),
    "vMinAB": str(vMinAB),
    "vMinBC": str(vMinBC),
    "vMinCA": str(vMinCA),
    "vMinTL": str(vMinTL)
        }



jsonTo = json.dumps(jsondato)
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
client.connect("sener.ciateq.net.mx", 4001, 60)
client.subscribe("/BROKER/DATA/H-M999")  # esta linea de codigo hace funcionar el on_message
client.loop_start()

client.publish("/BROKER/DATA/H-M999", jsonTo)
time.sleep(1)
client.loop_stop()

client.disconnect()
#print(jsonTo)

print("{\n\t[\n\t{vAB:"+str(vAB)+",\nvBC:"+str(vBC)+",\nvCA:"+str(vCA)+",\nvLT:"+str(vLT)+",\nvAN:"+str(vAN)+",\nvBN:"+str(vBN)+",\nvCN:"+str(vCN)+",\nvNT:"+str(vNT)+",\ncA:"+str(cA)+",\ncB:"+str(cB)+",\ncC:"+str(cC)+",\ncT:"+str(cT)+",\ncMaxA:"+str(cMaxA)+",\ncMaxB:"+str(cMaxB)+",\ncMaxC:"+str(cMaxC)+",\ncMaxT:"+str(cMaxT)+",\npaA:"+str(paA)+",\npaB:"+str(paB)+",\npaC:"+str(paC)+",\npaT:"+str(paT)+",\nprA:"+str(prA)+",\nprB:"+str(prB)+",\nprC:"+str(prC)+",\nprT:"+str(prT)+",\npapA:"+str(papA)+",\npapB:"+str(papB)+",\npapC:"+str(papC)+",\npapT:"+str(papT)+",\nfpA:"+str(fpA)+",\nfpB:"+str(fpB)+",\nfpC:"+str(fpC)+",\nfpT:"+str(fpT)+",\nfpMinA:"+str(fpMinA)+",\nfpMinB:"+str(fpMinB)+",\nfpMinC:"+str(fpMinC)+",\nfpMin:"+str(fpMin)+",\nfr:"+str(fr)+",\nthdvA:"+str(thdvA)+",\nthdvB:"+str(thdvB)+",\nthdvC:"+str(thdvC)+",\nthdvAN:"+str(thdvAN)+",\nthdvBN:"+str(thdvBN)+",\nthdvCN:"+str(thdvCN)+",\nthdcA:"+str(thdcA)+",\nthdcB:"+str(thdcB)+",\nthdcC:"+str(thdcC)+",\nthdvMaxAN:"+str(thdvMaxAN)+",\nthdvMaxBN:"+str(thdvMaxBN)+",\nthdvMaxCN:"+str(thdvMaxCN)+",\nthdvMaxA:"+str(thdcMaxA)+",\nthdvMaxB:"+str(thdcMaxB)+",\nthdvMaxC:"+str(thdcMaxC)+",\nvMaxAN:"+str(vMaxAN)+",\nvMaxBN:"+str(vMaxBN)+",\nvMaxCN:"+str(vMaxCN)+",\nvMaxTLN:"+str(vMaxTLN)+",\nvMaxAB:"+str(vMaxAB)+",\nvMaxBC:"+str(vMaxBC)+",\nvMaxCA:"+str(vMaxCA)+",\nvMaxTL:"+str(vMaxTL)+",\nvMinAN:"+str(vMinAN)+",\nvMinBN:"+str(vMinBN)+",\nvMinCN:"+str(vMinCN)+",\nvMinTLN:"+str(vMinTLN)+",\nvMinAB:"+str(vMinAB)+",\nvMinBC:"+str(vMinBC)+",\nvMinCA:"+str(vMinCA)+",\nvMinTL:"+str(vMinTL)+"}\n]\n}")
print(dato)