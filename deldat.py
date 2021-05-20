# Archivofuncion borrar datos
import sqlite3

def del_ement():
    print("##########  Borrar elemento  #############\n\n")
    art= input("Ingrese el codigo del elemento que desea borrar: ")

    conectar = sqlite3.connect('base.db')
    cur = conectar.cursor()

    cur.execute("DELETE FROM PRINCIPAL WHERE CODIGO=?",(art,))

    conectar.commit()
    conectar.close()