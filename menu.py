from input_datos import anadir
from buscard import busqueda
from deldat import del_ement
import time
import sqlite3
from sqlite3 import Error

    
def menusel():

       while True:

        print('###########  Menu principal  ###########\n########################################\n')
        sel = input("Seleccione una opción:\n\n[1] Añadir\n[2] Buscar\n[3] Borrar\n[4] Salir\n\n")

        if sel == str(1):
            print("añadiendo...")
            anadir()
    
        elif sel == str(2):
            print("Buscando...")
            time.sleep(1)
            busqueda()

        elif sel == str(3):
            del_ement()
  
        elif sel == str(4):
            print ("saliendo...")
            time.sleep(1)
            break
  

try:
#---------Crea la base de dato o revisa siya existe

    con = sqlite3.connect('base.db') 

    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE PRINCIPAL(
        ID           INTEGER         PRIMARY KEY,
        CODIGO       VARCHAR(12)                    NOT NULL,
        NOMBRE       VARCHAR(20)                    NOT NULL,
        FABRICA      VARCHAR(20),
        MODELO       DATE,
        COSTO         FLOAT,
        PRECIO        FLOAT                
    )
        
        
    """)

    print("Base de datos creada con exito")
    time.sleep(2)
    con.close()
    menusel()
      
    #----------- Si ya existe se evita el error y se pasa al menu.
    #----------- Aqui hay que controlar si no genera otro tipo de errores... mas adelante lo checamos
except Error:

    print('Base de datos cargada con exito...')
    menusel()
        




