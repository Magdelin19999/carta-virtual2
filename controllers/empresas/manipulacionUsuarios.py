from hashlib import md5


from models.empresas import setenciasSQLUsusarios as SQL
from models.mensaje import mensaje as sendMensaje
from controllers.token import generar


def datosFormulario(nombreEmpresa, descEmpresa, celularEmpresa,
                    direccionEmpresa, correo, contrasenia,logoEmpresa):

    contrasenia = encriptarContraseña(contrasenia)
    logoEmpresa= imagenPath(logoEmpresa)
    resultado = SQL.insertUsuario(nombreEmpresa, descEmpresa, celularEmpresa,
                                  direccionEmpresa, correo, contrasenia,logoEmpresa)

    if (isinstance(resultado, int) == True):
        print('Enviar mensaje del usuario')
        keyToken = generar.generarKey(resultado)
        sendMensaje.mensaje(correo, resultado, keyToken)


def returnID(token):
    return generar.returnID(token)

def activacion(id):
    return SQL.obtenerDBID(id)

def eliminarNoActivo(id):
    SQL.eliminarID(id)
    
def tokenCambioContra(id):
    keyToken = generar.generarKey(id)


def encriptarContraseña(contrasenia):
    return md5(contrasenia.encode("utf-8")).hexdigest()

def inicioSesion(correo, contrasenia):
    return (SQL.obtenerEmpresa(correo, encriptarContraseña(contrasenia)))

def cerrarSesion():
    SQL.cerrarSesion()

def imagenPath(imagen):
    nombre_imagen = (imagen.filename).replace(" ", "")
    path = f'static/img/temp/{nombre_imagen}'
    print('\n\n\n\n\n',path)
    imagen.save(path)
    ''' with open(path, 'rb') as file:
        binaryData = file.read()
    return binaryData '''
    return path

