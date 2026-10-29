# Lenguaje de Programación 3 - Taller 1

![commits](https://badgen.net/github/commits/clubdecomputacion/lp3-taller1?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/clubdecomputacion/lp3-taller1)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor 
#JONH EDWIN ORDOÑEZ MUÑOZ

- [@jedwin](https://www.github.com/jhon16edwin05)

## Descripción del Proyecto
#API REST desarrollada en Python utilizando Flask, Flask-RESTful y Flask-SQLAlchemy. Permite la gestión completa de videos (crear, consultar, actualizar de forma parcial, listar y eliminar) con persistencia de datos en una base de datos SQLite.


## Instalación

Morbi quam lectus, tempus sit amet mi non, facilisis dignissim erat. Aenean tortor libero, rhoncus eu eleifend ut, volutpat id nisi. Ut porta eros at ante rutrum pharetra. Integer nec nulla dictum, vestibulum ligula id, hendrerit ex. Morbi eget tortor metus.

1. Clonar el proyecto
```bash
git clone https://github.com/clubdecomputacion/lp3-taller1.git
```

2. Revisar la [`GUIA.md`](docs/GUIA.md)

3. Crea y activa tu entorno virtual:

   Bash
   python3 -m venv venv
   source venv/bin/activate

4. INstalacion de dependencias

pip install -r requirements.txt

5. Ejecuta el proyecto

   python3 run.py

6. Uso de la API

GET	/api/videos	Obtiene la lista de todos los videos registrados. la opcion que se le agrego de mejora

 GET 	/api/videos/<id>	Consulta un video específico por su ID.
 PUT 	/api/videos/<id>	Crea un nuevo video asignándole un ID en la URL.
 PATCH	/api/videos/<id>	Actualiza de forma parcial los campos de un video.
 DELETE	/api/videos/<id>	Elimina un video existente.

7. En el Paso 12 se implementó la siguiente mejora:

Añadir un endpoint para obtener todos los videos (GET /api/videos): Permite listar en formato JSON todos los registros almacenados en la base de datos de manera conjunta.

