import sqlite3
import os
import time

def Menu():
     print ("Menu provicional de acciones. ")
     print("")
     print("1.- agregar ")
     print("2.- modificar")
     print("3.- eliminar ")
     print("4.- mostrar")
     print("5.- salir ")
     print("")
     try:
         op=int(input("intruduce una opcion valida:"))
     except:
         print("No es una opcion valida")
         print("")
         Menu()

     os.system('cls')
     if op==1:
         Agregar()
     elif op==2:
         Modificar()
     elif op==3:
         Eliminar()
     elif op==4:
         Mostrar()
     elif op==5:
         Salir()
     else:
         print("ingrese un numero del menu")
         Menu()

def Mostrar():
    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()
    #print ("esto indica que nos conectamos""\n")
    a=cursor.execute("select ID_LECTURA, _datetime, tension, corriente, corrienteMaxima, potenciasActivas, potenciaReactiva, potenciaAparente, factorPotencia, factorPotenciaMini FROM lecturas_")
    print(" ")
    print("\tid Cod \t  fecha   \t\t\t\tTension    Corriente    corrienteMax  PotenciaAct PotenciaReac PotenciaApar FactorPot FactopPotMi ")
    print("\t==============================================================")
    for lecturas_ in cursor:
        #print("esto indica que a mediados estoy bien ")
        lecturas_='\t'+str(lecturas_[0])+'\t\t'+str(lecturas_[1])+'\t\t'+str(lecturas_[2])+'\t\t\t'+str(lecturas_[3])+'\t\t\t  '+str(lecturas_[4])+'\t\t\t  '+str(lecturas_[5])+'\t\t\t'+str(lecturas_[6])+'\t\t\t'+str(lecturas_[7])+'\t\t\t'+str(lecturas_[8])+'\t\t\t'+str(lecturas_[9])#+'\t'+str(lecturas_[10])
        print (str(lecturas_))
    conn.commit()
    cursor.close()
    conn.close()
    print ("\n")
   
    time.sleep(7)
    os.system('clear')
    Menu()

def Agregar():
    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()
    print("Opcion Agregar")
    print("\n")
    #_datetime =input("Ingrese un valor para fecha: ")
    tension =input("Ingrese un valor para tension: ")
    corriente =int(input("Ingrese un valor para corriente: "))
    corrienteMaxima =int(input("Ingrese un valor corrienteMaxima: "))
    potenciasActivas =int(input("Ingrese un valor para potenciasActivas: "))
    potenciaReactiva =int(input("Iingrese un valor para potenciaReactiva: "))
    potenciaAparente =int(input("Iingrese un valor para potenciaAparente: "))   
    factorPotencia =int(input("Iingrese un valor para factorPotencia: "))
    factorPotenciaMini =int(input("Iingrese un valor para factorPotenciaMini: "))

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
    Menu()
    
def Eliminar():
    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()
    cursor.execute("select * from lecturas_")
    print("Esta en opcion: Eliminar, \n Tenga cuidado de no eliminar algo no deceado ")
    print(" ")
    print("\tid Cod \t  fecha   \t\t\t\tTension    Corriente    corrienteMax  PotenciaAct PotenciaReac PotenciaApar FactorPot FactopPotMi ")
    print("\t==============================================================")
    for lecturas_ in cursor:
        #print("esto indica que a mediados estoy bien ")
        lecturas_='\t'+str(lecturas_[0])+'\t\t'+str(lecturas_[1])+'\t\t'+str(lecturas_[2])+'\t\t\t'+str(lecturas_[3])+'\t\t\t'+str(lecturas_[4])+'\t\t\t\t'+str(lecturas_[5])+'\t\t\t\t'+str(lecturas_[6])+'\t\t\t'+str(lecturas_[7])+'\t\t\t'+str(lecturas_[8])+'\t\t\t'+str(lecturas_[9])
        print (str(lecturas_))
    print("")
    print("Decea eliminar alguna entrada:")
    cod=input("digita el codigo de la entrada que decea eliminar:")
    sentencia="delete from lecturas_ where ID_LECTURA = ?; "
    cursor.execute(sentencia, [cod])
    print ("la entrafa fue eliminada ")
    conn.commit()
    cursor.close()
    conn.close()
    print ("\n")
    time.sleep(2)
    os.system('clear')
    Menu()

def Modificar():
    info=[]
    conn = sqlite3.connect('lecturas.db')
    cursor = conn.cursor()
    print("Esta en opcion Modificar ")
    cursor.execute("select * from lecturas_")

    print(" ")
    print("\tid Cod \t   fecha  \t\t\t\tTension    Corriente    corrienteMax  PotenciaAct PotenciaReac PotenciaApar FactorPot FactopPotMi ")
    print("\t==============================================================")
    for lecturas_ in cursor:
        info.append(lecturas_)
        #print("esto indica que a mediados estoy bien ")
        lecturas_='\t'+str(lecturas_[0])+'\t\t'+str(lecturas_[1])+'\t\t'+str(lecturas_[2])+'\t\t\t'+str(lecturas_[3])+'\t\t\t  '+str(lecturas_[4])+'\t\t\t  '+str(lecturas_[5])+'\t\t\t'+str(lecturas_[6])+'\t\t\t'+str(lecturas_[7])+'\t\t\t'+str(lecturas_[8])+'\t\t\t'+str(lecturas_[9])
        print (str(lecturas_))
    print("")
    print("Decea Modificar algun valor:")
    cod=input("digita el codigo de la entrada que decea Modificar:")
    for lecturas_ in info:
        if int(lecturas_[0])== int (cod):
                _datetime=lecturas_[1]
                tension=lecturas_[2]
                corriente=lecturas_[3]
                corrienteMaxima=lecturas_[4]
                potenciasActivas=lecturas_[5]
                potenciaReactiva=lecturas_[6]
                potenciaAparente=lecturas_[7]
                factorPotencia=lecturas_[8]
                factorPotenciaMini=lecturas_[9]
                encontrado=True
        break
    _datetime=input("ingrese el nuevo valor para la fecha:")
    tension=input("ingrese un nuevo valor par la tension:")
    corriente=input("ingrese un nuevo valor para la corriente:")
    corrienteMaxima=input("ingrese un nuevo valor corriente maxima :")
    potenciasActivas=input("ingrese un nuevo valor para la potenca activa:")
    potenciaReactiva=input("ingrese un nuevo valor para la potencia reactiva :")
    potenciaAparente=input("ingrese un nuevo valor potencia aparente:")
    factorPotencia=input("ingrese un nuevo valor factor potencia :")
    factorPotenciaMini=input("ingrese un nuevo valor factor potencia minima:")
    
    sentencia="update lecturas_ set _datetime='"+_datetime+"',tension='"+tension+"',corriente='"+corriente+"',corrienteMaxima='"+corrienteMaxima+"',potenciasActivas='"+potenciasActivas+"',potenciaReactiva='"+potenciaReactiva+"',potenciaAparente='"+potenciaAparente+"',factorPotencia='"+factorPotencia+"',factorPotenciaMini='"+factorPotenciaMini+"' where ID_LECTURA =?"
    cursor.execute(sentencia, [cod])
    print ("El producto fue modificado")
    conn.commit()
    cursor.close()
    conn.close()
    print ("\n")
    time.sleep(2)
    os.system('clear')
    Menu()

def Salir():
    print("Has elegido salir ")

Menu()