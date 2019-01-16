import sqlite3
import time
#import main_

#conn = sqlite3.connect('lecturas.db')
ID_LECTURA = main_.LECTURA

def export_db(cursor, row):
    print("hola neptuno ")
    d = {}
    for idx, col in enumerate(cursor.description):
        #print("\n")
        d[col[0]] = row[idx]
    return d
conn = sqlite3.connect("lecturas.db")

conn.row_factory = export_db()
cursor = conn.cursor()
cursor.execute("select * from lecturas_ where ID_LECTURA=1 ",ID_LECTURA)

results = cursor.fetchall()
print(results)
#aservidor = input("json" + results)

conn.commit()
cursor.close()
conn.close()
#print("dentro de mi: \n", aservidor)
time.sleep(2)




