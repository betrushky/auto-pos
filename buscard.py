import sqlite3

def busqueda():

    print('###########  Busqueda  ###########\n########################################\n')
    gt= input("[1] Mostrar todos los elementos\n[2] Buscar por codigo\n[3]Buscar por nombre\n[4]Mas opciones...\n[5]Salir\n")
    if gt == str(1):
        btodos()
    #-------- faltan agregar elementos de condicionales y control de errores de caracteres
    
    elif gt == str(2):
        bcodi()

    elif gt == str(3):
        bxnom()
       

def bcodi():
    while True:

        codd = input("\nIngrese el codigo que desea consultar o Q para salir: ")
        if codd == 'Q' or codd == 'q':
            break
        
            
        conector = sqlite3.connect('base.db')
        cursor = conector.cursor()

        cursor.execute("SELECT CODIGO FROM PRINCIPAL")
        existe = cursor.fetchall()
        

        for i in existe:
                
            if codd in i:
                conector = sqlite3.connect('base.db')
                cursor.execute("SELECT * FROM PRINCIPAL WHERE CODIGO=?",(codd,))
                muestra = cursor.fetchall()
                for _ in muestra:
                    print(_)
                
                input("\nPresione una teclapara continuar...")
                conector.close()
                break
                 
     
        conector.close()   
        #input("Codigo no valido...")
        
    
def btodos():
# Mostrar todos los datos
    conetor = sqlite3.connect('base.db')
    cursor = conetor.cursor()

    cursor.execute("SELECT CODIGO,FABRICA,NOMBRE,MODELO,PRECIO FROM PRINCIPAL")

    elemento = cursor.fetchall()
    for elem in elemento:
        print(elem)
        
    conetor.close()
    input('\nPresione una tecla para regresar al menu...')
    
def bxnom():

    codd = input("\nIngrese el nombre que desea consultar: ")
    conecta = sqlite3.connect('base.db')
    cur = conecta.cursor()

    #cur.execute("SELECT NOMBRE FROM PRINCIPAL")

    cur.execute("SELECT CODIGO, FABRICA,NOMBRE, MODELO,PRECIO FROM PRINCIPAL WHERE NOMBRE=?",(codd,))
    muestra=cur.fetchall()
    print(muestra)

    conecta.close()
    input('\nPresione una teclapara volver al menu...')