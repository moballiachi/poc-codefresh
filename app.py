from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Obtiene una variable de entorno para demostrar que la app puede leer configuración
    env_var = os.environ.get('DEMO_ENV_VAR', 'Valor por defecto (no configurado)')
    return f"<h1>Hola Codefresh!</h1><p>Esta es una app demo sencilla.</p><p>Valor de la variable de entorno DEMO_ENV_VAR: <b>{env_var}</b></p>"

if __name__ == '__main__':
    # Usamos 0.0.0.0 para que sea accesible desde fuera del contenedor
    app.run(debug=True, host='0.0.0.0', port=5000)