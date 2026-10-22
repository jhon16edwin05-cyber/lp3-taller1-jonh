"""
Punto de entrada de la aplicación.

Ejecutar con:
    python run.py
"""

import os

from app import create_app

# La configuración se selecciona con la variable de entorno FLASK_CONFIG
# ("development", "production" o "testing"). Si no existe, se usa
# "development". Ver app/config.py
app = create_app(os.getenv("FLASK_CONFIG", "development"))

if __name__ == "__main__":
    # ejecutar la aplicación en modo debug=True mientras
    # desarrollas (recarga automática + mensajes de error detallados).
    app.run(debug=True)
    pass

