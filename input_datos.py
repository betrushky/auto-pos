import sqlite3


def anadir():
    
    while True:
    
        print('###########  Nuevo Registro  ###########\n########################################\n')
        print('Ingrese los datos:\n\nCampos con * son obligatorios \n')

        codigo = input('*Codigo: ')
        nombre = input('*Nombre: ')
        fabrica = input('Concesionaria: ')
        modelo = input('Modelo: ')
        costo = input('Costo: $')
        precio = input('Precio: $')

        if codigo == "" or nombre == "":
            print("Error vuelva a intentarlo...")
        
        else:
            break

    
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
  
    cursor.execute("""
    INSERT INTO PRINCIPAL (CODIGO, NOMBRE, FABRICA, MODELO, COSTO, PRECIO) VALUES
    ('%s', '%s', '%s', '%s', '%s', '%s')
    """ % (codigo,nombre,fabrica,modelo,costo,precio))
    conexion.commit()
    
    conexion.close()

    dec=input('Se agregaron datos con exito...\nDesea agregar otro nuevo registro?[S][N] ')
    if dec == str('s') or dec== str('S'):
        anadir()
    else:
        print('Saliendo...')
   



    
 



