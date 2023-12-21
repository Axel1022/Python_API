# Importa FastAPI
from typing import List
from fastapi import APIRouter
from fastapi import HTTPException;
import sys
sys.path.append(r'C:\Users\IngCa\Desktop\Cursos\Python_API')
from app.data.dataUser import obtener_lista_usuarios
from app.utils.utilsUsers import buscarId, buscarUser
from app.models.modelUser import User
from fastapi.responses import JSONResponse

# Iniciar server: python -m uvicorn main:app --reload
# Url: http://127.0.0.1:8000/docs
# Documentacion: https://fastapi.tiangolo.com/es/tutorial/first-steps/

'''
Operaciones de ruta (GET, POST, PUT, DELETE...)
POST -> Para crear datos.
GET -> Para leer datos.
PUT -> Para actualizar datos.
DELETE -> Para borrar datos.
'''

# Crea una instancia de la aplicación
router = APIRouter();
userList = obtener_lista_usuarios();


# Devuelve una lista de usuarios en formato JSON
@router.get("/usersJson",response_model=List[User], status_code=200)
async def users_Json():
    '''
    Devuelve una lista de usuarios en formato JSON.

    Returns:
        JSONResponse: Un objeto JSONResponse con la lista de usuarios en formato JSON si se encuentran usuarios.
                      En caso contrario, lanza una excepción HTTP 404 indicando que no se encontraron usuarios.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si no se encuentran usuarios.

    '''
    if not userList:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios")
    else:
        return userList


# Devuelve un usuario por el ID
@router.get("/user/{id}",response_model=User, status_code=200)
async def user_id(id: int):
    '''
    Devuelve un usuario según su ID.

    Args:
        id (int): El ID del usuario a buscar.

    Returns:
        JSONResponse: Un objeto JSONResponse con la información del usuario en formato JSON si se encuentra.
                      En caso contrario, lanza una excepción HTTP 404 si no se encuentra el usuario.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si el usuario con el ID especificado no se encuentra.

    '''

    user_found = buscarUser(id, userList)
    if user_found:
        return user_found
    else:
        raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")

# Develve un usuario por parametros de consulta
"""
@app.get("/user/")
async def user_by_id(id: int = Query(..., description="ID of the user to retrieve")):
    user_fund = buscarId(id, userList )
    return user_fund;
"""

# Elimina un usuario por el ID
@router.delete("/user/{id}", status_code=200, response_model=dict)
async def user_delete(id: int):
    """
    Elimina un usuario según su ID.

    Args:
        id (int): El ID del usuario a eliminar.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje indicando si la eliminación fue exitosa.
                      En caso contrario, lanza una excepción HTTP 404 si no se encuentra el usuario.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si el usuario con el ID especificado no se encuentra.

    """
    user_found = buscarUser(id, userList)
    if user_found:
        userList.remove(user_found)
        return JSONResponse(content={"message": f"Usuario con ID {id} eliminado exitosamente"})
    else:
        raise HTTPException(status_code=404, detail=f"Usuario con ID {id} no encontrado")

# Añade un nuevo usuario
@router.post("/user",status_code=201, response_model=dict)
async def user_add(user: User):
    """
    Añade un nuevo usuario al sistema.

    Args:
        user (User): Los datos del nuevo usuario a añadir.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje indicando si el usuario fue añadido exitosamente.
                      En caso contrario, lanza una excepción HTTP 409 si el ID del usuario ya existe.

    Raises:
        HTTPException: Se lanza con un código de estado 409 si el ID del usuario ya existe.

    """
    id_found = buscarId(user.id, userList)
    if not id_found:
        userList.append(user)
        return JSONResponse(content={"message": f"Usuario {user.name} añadido exitosamente", "ID": f"{user.id}"})
    else:
        raise HTTPException(status_code=409, detail={"Error": "Usuario no añadido", "Descripción": f"El ID: {user.id} ya existe."})

#Actualizar
@router.put("/user", status_code=200, response_model=dict)
async def user_Update(user: User):
    """
    Edita un usuario en la lista basándose en su ID.

    Args:
        user (User): El usuario con los cambios.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje de confirmación si se realizó la edición correctamente.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si no se encontró el usuario.
    """
    user_fund = buscarId(user.id, userList )
    if user_fund:
        for i, Saved_user in enumerate(userList):
            if Saved_user.id == user.id:
                userList[i] = user
                return JSONResponse(content={"message": "Usuario actualizado correctamente"})
    else:
        raise HTTPException(status_code=404, detail=f"User with id {user.id} not found")

from fastapi import HTTPException

# Edita un usuario en la lista basándose en su ID
"""
@app.put("/users")
async def user_Update(idActual: int, user: User):
    '''
    Edita un usuario en la lista basándose en su ID.

    Args:
        idActual (int): El ID del usuario que se va a editar.
        user (User): El usuario con los cambios.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje de confirmación si se realizó la edición correctamente.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si no se encontró el usuario.
                      Se lanza con un código de estado 304 si el ID del nuevo usuario ya existe.
    '''

    user_fund_Actual = buscarId(idActual, userList )
    if user_fund_Actual:
        user_fund_New = buscarId(user.id, userList)
        if user_fund_New:
            raise HTTPException(status_code=304, detail={"Error": "Usuario no modificado", "Descripción": f"El ID: {user.id} ya existe."})

        for i, Saved_user in enumerate(userList):
            if Saved_user.id == idActual:
                userList[i] = user
                return {"message": "Usuario actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No existe un usuario con ID {idActual}")
"""
