import sqlite3


from dateutil import parser
from matplotlib import style
import matplotlib.pyplot as plt
style.use('dark_background')

conn = sqlite3.connect('lecturas.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM lecturas_ WHERE id_cliente > 1')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
    c.execute('SELECT * FROM lecturas_ WHERE poteciaAparente > 100')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
    c.execute('SELECT * FROM lecturas_ WHERE potenciasAcivas > 150' )
    data = c.fetchall()
    print(data)
    for row in data:
        print(row[0])
def graf1():
    c.execute('SELECT _datetime, tension FROM lecturas_')
    dataten = c.fetchall()
    dates = []
    values = []
    for row in dataten:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, 'x-')
    plt.ylabel('Tension')
    plt.xlabel('Tiempo')
    plt.show()
    return dataten
def graf2():
    c.execute('SELECT _datetime, corriente FROM lecturas_')
    datacor = c.fetchall()
    """dates = []
    values = []
    for row in datac:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, 'x-')
    plt.ylabel('Tencion')
    plt.xlabel('Tiempo')
    """#plt.show()
    return datacor
def graf3():
    c.execute('SELECT _datetime, corrienteMaxima FROM lecturas_')
    datacorMax = c.fetchall()
    return datacorMax
def graf4():
    c.execute('SELECT _datetime, potenciasActivas FROM lecturas_')
    datapotact = c.fetchall()
    return datapotact
def graf5():
    c.execute('SELECT _datetime, potenciaReactiva FROM lecturas_')
    datapotrea = c.fetchall()
    return datapotrea
def graf6():
    c.execute('SELECT _datetime, potenciaAparente FROM lecturas_')
    datapotapa = c.fetchall()
    return datapotapa
def graf7():
    c.execute('SELECT _datetime, factorPotencia FROM lecturas_')
    datafacpot = c.fetchall()
    return datafacpot
def graf8():
    c.execute('SELECT _datetime, factorPotenciaMini FROM lecturas_')
    datafacpotm = c.fetchall()
    return datafacpotm

graf1()
graf2()
graf3()
graf4()
graf5()
graf6()
graf7()
graf8()


c.close
conn.close()