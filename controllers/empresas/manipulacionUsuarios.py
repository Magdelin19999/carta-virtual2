from models.empresas import setenciasSQLUsusarios as SQL

def datosFormulario(nombreEmpresa,descEmpresa,celularEmpresa,
          direccionEmpresa,correo,contrasenia):
    print('validar') 
    #print(SQL.obtenerTodosDB())
    SQL.insertUsuario(nombreEmpresa,descEmpresa,celularEmpresa,
          direccionEmpresa,correo,contrasenia)