import sqlite3
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')
conn = sqlite3.connect('lecturas.db')
c = conn.cursor()

def read_from_db():
  c.execute('SELECT * FROM lecturas_ WHERE ID_LECTURA = 5')
  data = c.fetchall()
  print(data)
  for row in data:
    print(row)

def graf_data():
  c.execute('SELECT _datetime, corrienteMaxima  FROM lecturas_')
  data = c.fetchall()
  dates = []
  values = []
  for row in data:
    dates.append(parser.parse(row[0]))
    values.append(row[1])
  plt.plot_date(dates, values, 'x-')
  plt.show()
read_from_db()
graf_data()
read_from_db()
c.close
conn.close()