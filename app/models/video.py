
"""
Modelo de datos para Video.

Cada instancia de VideoModel representa una fila de la tabla 'videos'.
"""

from . import db


class VideoModel(db.Model):
    """Modelo para representar un video.

    Atributos:
        id (int): identificador único del video
        name (str): nombre (título) del video
        views (int): número de vistas (reproducciones)
        likes (int): número de "me gusta"
    """

    # Nombre de la tabla en la base de datos
    __tablename__ = "videos"

    # Definición de columnas
    id = db.Column(db.Integer, primary_key=True)

    # 1: Definir la columna 'name': texto de máximo 100 caracteres
    #         que no puede ser nulo.
    name = db.Column(db.String(100), nullable=False)

    # 2: Definir la columna 'views': entero que no puede ser nulo.
    views = db.Column(db.Integer, nullable=False)

    # 3: Definir la columna 'likes': entero que no puede ser nulo.
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Representación en texto del objeto (útil para depurar)."""
        return (
            f"Video(id={self.id}, name={self.name}, "
            f"views={self.views}, likes={self.likes})"
        )

