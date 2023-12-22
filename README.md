# README - FastAPI Python API 🚧

## Información General 🐍

Este repositorio contiene el código de una API en construcción desarrollada con FastAPI y Python. La API está diseñada para gestionar usuarios y productos, proporcionando operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre estos recursos.

## Estructura del Proyecto 📂

El proyecto está organizado en varios módulos para una mejor estructuración y mantenimiento:

- **`main.py`**: Punto de entrada de la aplicación FastAPI.
- **`app`**: Directorio que contiene los módulos relacionados con la lógica de la aplicación.
  - **`routers`**: Módulos que definen las rutas y operaciones de la API para usuarios y productos.
  - **`data`**: Módulos que proporcionan funciones para obtener listas de usuarios y productos (simuladas).
  - **`utils`**: Módulos con utilidades para manipulación de datos y búsqueda.
  - **`models`**: Definición de modelos de datos utilizando Pydantic.
- **`requirements.txt`**: Archivo que lista las dependencias del proyecto. Puedes instalarlas usando `pip install -r requirements.txt`.

## Configuración y Ejecución 🚀

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias del proyecto ejecutando el siguiente comando en la terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicia el servidor FastAPI ejecutando el siguiente comando:
   ```bash
   uvicorn main:app --reload
   ```
4. Accede a la documentación y prueba la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Funcionalidades de la API 🚧

### Usuarios

- **`GET /users`**: Obtiene una lista de usuarios en formato JSON.
- **`GET /users/{id}`**: Obtiene un usuario por su ID en formato JSON.
- **`DELETE /users/{id}`**: Elimina un usuario por su ID.
- **`POST /users`**: Añade un nuevo usuario al sistema.
- **`PUT /users`**: Edita un usuario en la lista basándose en su ID.

### Productos

- **`GET /products`**: Obtiene una lista de productos en formato JSON.

## Contribuciones 🤝

¡Se agradecen las contribuciones! Si deseas contribuir, sigue las pautas mencionadas en la sección correspondiente del proyecto.

## Contacto 📧

- **Desarrollador 🧑‍💻:** Gary Alexander Campusano Paredes
- **LinkedIn: [Gary Alexander Campusano Paredes](https://www.linkedin.com/in/gary-alexander-campusano-paredes-87a28724a/)**
- **Correo Electrónico 📧:** ingcampusano@outlook.com
- **Link del curso 🔗: [Youtube](https://www.youtube.com/watch?v=_y9qQZXE24A&list=PLpe6j6xtTf6jPgV1C8X38o_3Yvz_KCKUP&index=2&t=13115s&ab_channel=MoureDevbyBraisMoure/)**

¡Gracias por tu interés en la API! Ten en cuenta que la API está en construcción y aún faltan implementar algunas funcionalidades. Estoy aprendiendo, así que cualquier sugerencia o corrección es bienvenida. 🚀
