# Pruebas de la API de Videos

Las pruebas se ejecutaron en la aplicación Flask usando el cliente de pruebas (`app.test_client()`) en modo `testing` para validar los endpoints de `Video`.

## 1. Crear un video (PUT) — caso exitoso

- **Solicitud:** `PUT /api/videos/1`
- **Cuerpo:**
  ```json
  {"name": "Tutorial de Flask", "views": 0, "likes": 0}
  ```
- **Código esperado:** 201
- **Código obtenido:** 201
- **Respuesta:**
  ```json
  {"id": 1, "name": "Tutorial de Flask", "views": 0, "likes": 0}
  ```
- **Evidencia:** Se verificó mediante la ejecución del cliente de pruebas de Flask, donde la creación del recurso devolvió `201 Created`.

## 2. Consultar un video (GET) — caso exitoso

- **Solicitud:** `GET /api/videos/1`
- **Código esperado:** 200
- **Código obtenido:** 200
- **Respuesta:**
  ```json
  {"id": 1, "name": "Tutorial de Flask", "views": 0, "likes": 0}
  ```
- **Evidencia:** El endpoint de lectura devolvió el video creado con status `200 OK`.

## 3. Actualizar un video (PATCH) — caso exitoso

- **Solicitud:** `PATCH /api/videos/1`
- **Cuerpo:**
  ```json
  {"views": 2500, "likes": 200}
  ```
- **Código esperado:** 200
- **Código obtenido:** 200
- **Respuesta:**
  ```json
  {"id": 1, "name": "Tutorial de Flask", "views": 2500, "likes": 200}
  ```
- **Evidencia:** La actualización parcial modificó solo los campos enviados y respondió con `200 OK`.

## 4. Eliminar un video (DELETE) — caso exitoso

- **Solicitud:** `DELETE /api/videos/1`
- **Código esperado:** 204
- **Código obtenido:** 204
- **Respuesta:**
  ```json
  ""
  ```
- **Evidencia:** La eliminación del recurso respondió con `204 No Content` y quedó removido correctamente.

## 5. Error 400 — falta un campo obligatorio en PUT

- **Solicitud:** `PUT /api/videos/10`
- **Cuerpo:**
  ```json
  {"name": "Video incompleto", "views": 1}
  ```
- **Código esperado:** 400
- **Código obtenido:** 400
- **Respuesta:**
  ```json
  {"message": {"likes": "El número de likes del video es requerido"}}
  ```
- **Evidencia:** `reqparse` rechazó la solicitud porque faltaba el campo `likes`, devolviendo `400 Bad Request`.

## 6. Error 404 — video no existe

- **Solicitud:** `GET /api/videos/999`
- **Código esperado:** 404
- **Código obtenido:** 404
- **Respuesta:**
  ```json
  {"message": "No se encontró un video con el ID 999"}
  ```
- **Evidencia:** Cuando se consultó un ID inexistente, la función `abort_if_video_doesnt_exist()` respondió con `404 Not Found`.

## 7. Error 409 — conflicto al crear un video duplicado

- **Solicitud:** `PUT /api/videos/2`
- **Cuerpo:**
  ```json
  {"name": "Video duplicado", "views": 99, "likes": 1}
  ```
- **Código esperado:** 409
- **Código obtenido:** 409
- **Respuesta:**
  ```json
  {"message": "Ya existe un video con el ID 2"}
  ```
- **Evidencia:** Se intentó crear un video con un ID que ya existía en la base de datos y el recurso respondió con `409 Conflict`.

## Resumen

Se validaron todos los métodos principales de la API:

- `GET`: éxito y error 404
- `PUT`: éxito y error 400/409
- `PATCH`: éxito
- `DELETE`: éxito

La API responde conforme a la especificación del taller y mantiene el comportamiento esperado para las solicitudes válidas e inválidas.
