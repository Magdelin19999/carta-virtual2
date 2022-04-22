from hashlib import md5
from models.empresas import setenciasSQLUsusarios as SQL
from models.mensaje import mensaje as sendMensaje
from controllers.token import generar

def datosFormulario(nombreEmpresa,descEmpresa,celularEmpresa,
                  direccionEmpresa,correo,contrasenia):
    
    contrasenia = encriptarContraseña(contrasenia)  
    resultado = SQL.insertUsuario(nombreEmpresa,descEmpresa,celularEmpresa,
                                    direccionEmpresa,correo,contrasenia)
    
    if(isinstance(resultado, int)==True):
        print('Enviar mensaje del usuario')
        keyToken = generar.generarKey(resultado)
        sendMensaje.mensaje(correo,resultado,keyToken)
          
def returnID(token):
    return generar.returnID(token)

def activacion(id):
    print(f'recibio activacion {id}')
    return SQL.obtenerDBID(id)
  
def encriptarContraseña(contrasenia):
    print('Encriptando contraseña')
    
    return md5(contrasenia.encode("utf-8")).hexdigest() 

def inicioSesion(correo, contrasenia):
    mensaje =''
    print('inicio de sesion')
    return (SQL.obtenerEmpresa(correo, encriptarContraseña(contrasenia)))
    

def  cerrarSesion():
    SQL.cerrarSesion()