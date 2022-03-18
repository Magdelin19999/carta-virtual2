from pprint import pprint
from models.empresas import mensaje as sendMensaje,setenciasSQLUsusarios as SQL

def datosFormulario(nombreEmpresa,descEmpresa,celularEmpresa,
                  direccionEmpresa,correo,contrasenia):
    
    contrasenia = encriptarContraseña(contrasenia)  
    resultado = SQL.insertUsuario(nombreEmpresa,descEmpresa,celularEmpresa,
                                    direccionEmpresa,correo,contrasenia)
    
    if(isinstance(resultado, int)==True):
          print('Enviar mensaje del usuario')
          sendMensaje.mensaje(correo,resultado)
          

def activacion(id):
    print(f'recibio activacion {id}')
    return SQL.obtenerDBID(id)
  
def encriptarContraseña(contrasenia):
    print('Encriptando contraseña')
    return contrasenia 

def inicioSesion(correo, contrasenia):
    mensaje =''
    print(SQL.obtenerEmpresa(correo, contrasenia))
    print('inicio de sesion')