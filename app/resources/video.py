"""
Recursos (rutas) de la API de Videos.

Un Resource de Flask-RESTful asocia una ruta con un método de Python por
cada método HTTP: get(), put(), patch(), delete().
"""

from flask_restful import Resource, reqparse, abort, fields, marshal_with

from ..models import db
from ..models.video import VideoModel

# Campos que se incluyen al serializar un VideoModel como JSON.
# Lo usa el decorador @marshal_with en cada método.
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}

# Parser para el cuerpo de las solicitudes PUT (crear video):
# los tres campos son obligatorios.
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="El nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="El número de vistas del video es requerido", required=True)
video_put_args.add_argument("likes", type=int, help="El número de likes del video es requerido", required=True)

# Parser para el cuerpo de las solicitudes PATCH (actualizar video):
# los tres campos son opcionales, solo se actualiza lo que llegue.
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")


def abort_if_video_doesnt_exist(video_id):
    result = VideoModel.query.filter_by(id=video_id).first()
    if result is None:
        abort(404, message=f"No se encontró un video con el ID {video_id}")
    return result


class Video(Resource):
    """Recurso para gestionar un video individual (ruta /api/videos/<video_id>).

    Métodos:
        get: obtener un video por ID
        put: crear un video con un ID específico
        patch: actualizar un video existente
        delete: eliminar un video existente
    """

    @marshal_with(resource_fields)
    def get(self, video_id):
        return abort_if_video_doesnt_exist(video_id)

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()

        if VideoModel.query.filter_by(id=video_id).first() is not None:
            abort(409, message=f"Ya existe un video con el ID {video_id}")

        video = VideoModel(
            id=video_id,
            name=args["name"],
            views=args["views"],
            likes=args["likes"],
        )
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = abort_if_video_doesnt_exist(video_id)

        if args["name"] is not None:
            result.name = args["name"]
        if args["views"] is not None:
            result.views = args["views"]
        if args["likes"] is not None:
            result.likes = args["likes"]

        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, video_id):
        result = abort_if_video_doesnt_exist(video_id)
        db.session.delete(result)
        db.session.commit()
        return "", 204

