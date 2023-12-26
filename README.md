

# README - FastAPI Python API 🚧

## Información General 🐍

Este repositorio contiene el código de una API en construcción desarrollada con FastAPI y Python.
La API está diseñada para gestionar usuarios y productos, proporcionando operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre estos recursos.

## Estructura del Proyecto 📂

El proyecto está organizado en varios módulos para una mejor estructuración y mantenimiento:

- **`main.py`**: Punto de entrada de la aplicación FastAPI.
- **`app`**: Directorio que contiene los módulos relacionados con la lógica de la aplicación.
  - **`routers`**: Módulos que definen las rutas y operaciones de la API para usuarios y productos.
  - **`data`**: Módulos que proporcionan funciones para obtener listas de usuarios y productos (simuladas).
  - **`utils`**: Módulos con utilidades para manipulación de datos y búsqueda.
  - **`models`**: Definición de modelos de datos utilizando Pydantic.
- **`requirements.txt`**: Archivo que lista las dependencias del proyecto. Puedes instalarlas usando:
```bash
pip install -r requirements.txt
```

## Configuración y Ejecución 🚀

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias del proyecto ejecutando el siguiente comando en la terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. Copia el archivo `.env.example` a `.env` y configura las variables de entorno necesarias.
4. Inicia el servidor FastAPI ejecutando el siguiente comando:
   ```bash
   uvicorn main:app --reload
   ```
5. Accede a la documentación y prueba la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Funcionalidades de la API 🚧

### Usuarios

- **`GET /users`**: Obtiene una lista de usuarios en formato JSON.
- **`GET /users/{id}`**: Obtiene un usuario por su ID en formato JSON.
- **`DELETE /users/{id}`**: Elimina un usuario por su ID.
- **`POST /users`**: Añade un nuevo usuario al sistema.
- **`PUT /users`**: Edita un usuario en la lista basándose en su ID.

### Productos

- **`GET /products`**: Obtiene una lista de productos en formato JSON.
- **`GET /products/{id}`**: Obtiene un producto por su ID en formato JSON.
- **`DELETE /products/{id}`**: Elimina un producto por su ID.
- **`POST /products`**: Añade un nuevo producto al sistema.
- **`PUT /products/{id}`**: Edita un producto en la lista basándose en su ID.

## Instrucciones de Configuración Adicionales ⚙️

- Configura las variables de entorno necesarias en el archivo `.env` para la correcta ejecución de la aplicación.

## Ejemplos de Solicitudes y Respuestas 📝

A continuación, se proporcionan ejemplos de solicitudes y respuestas para cada endpoint.

### Obtener todos los usuarios

**Solicitud:**

```http
GET /users
```

**Respuesta:**

```json
[
  {"id": 1, "name": "Usuario 1"},
  {"id": 2, "name": "Usuario 2"}
]
```

## Despliegue 🌐

Para desplegar la aplicación en un entorno de producción, consulta la documentación oficial de FastAPI sobre despliegue.

## Contribuciones 🤝

¡Se agradecen las contribuciones! Si deseas contribuir, sigue las pautas mencionadas en la sección correspondiente del proyecto.

## Licencia 📄

Este proyecto está bajo la Licencia [MIT](LICENSE).

## Estado del Proyecto 📊

Actualmente, la API está en fase de desarrollo activo.

## Problemas Conocidos 🚨

- La funcionalidad de XYZ aún no ha sido implementada.

## Contacto 📧

- **Desarrollador 🧑‍💻:** Gary Alexander Campusano Paredes
- **LinkedIn: [Gary Alexander Campusano Paredes](https://www.linkedin.com/in/gary-alexander-campusano-paredes-87a28724a/)**
- **Correo Electrónico 📧:** ingcampusano@outlook.com

¡Gracias por tu interés en la API! Ten en cuenta que la API está en construcción y aún faltan implementar algunas funcionalidades. Estoy aprendiendo, así que cualquier sugerencia o corrección es bienvenida. 🚀
