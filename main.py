from flask import *

app = Flask(__name__)
@app.get('/')
def home():
     return render_template('productos/index.html')
    
@app.get('/inicio-sesion/')
def inicioSesion():
    return render_template('empresas/sing.html')

app.run(debug=True)