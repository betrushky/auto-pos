import sqlite3

def busqueda():

    print('###########  Busqueda  ###########\n########################################\n')
    gt= input("[1] Mostrar todos los elementos\n[2] Buscar por codigo\n[3]Buscar por nombre\n[4]Mas opciones...\n[5]Salir\n")
    if gt == str(1):
        btodos()
    #-------- faltan agregar elementos de condicionales y control de errores de caracteres
    
    elif gt == str(2):
        bcodi()
       

def bcodi():
     #------ Falta control de errores y elementos
     codd = input("\nIngrese el codigo que desea consultar: ")
     conector = sqlite3.connect('base.db')
     cursor = conector.cursor()

     cursor.execute("SELECT * FROM PRINCIPAL WHERE CODIGO=?",(codd,))
     muestra = cursor.fetchall()
     print(muestra)


     conector.close

    
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
    
