from config import dataBase 

DB = dataBase.DB

def insertUsuario(nombreEmpresa,descEmpresa,celularEmpresa,
          direccionEmpresa,correo,contrasenia):
    cursor = DB.cursor()
    cursor.execute(f"""INSERT INTO usuarios(nombreEmpresa, descEmpresa, celularEmpresa,
                                        direccionEmpresa, correo, contrasenia) 
	                VALUES( '{nombreEmpresa}','{descEmpresa}','{celularEmpresa}',
                            '{direccionEmpresa}', '{correo}','{contrasenia}')""")
    DB.commit()
    cursor.close()
  
def obtenerTodosDB():
    dataProducts = []
    cursor= DB.cursor(dictionary=True)
    cursor.execute('''
        SELECT * FROM usuarios;''')
    dataProducts = cursor.fetchall()
    DB.commit()
    cursor.close()
    return dataProducts