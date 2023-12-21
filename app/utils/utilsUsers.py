from fastapi import HTTPException;
from app.models import modelUser

def buscarId(id: int, user_list):
    """
    Busca un usuario por ID en la lista de usuarios.

    Args:
        id (int): ID del usuario a buscar.
        user_list (list): Lista de usuarios.

    Returns:
        dict: True o False
    """
    for user in user_list:
        if user.id == id:
            return True
    return False

def buscarUser(id: int, user_list):
    """
    Busca un usuario por ID en la lista de usuarios.

    Args:
        id (int): ID del usuario a buscar.
        user_list (list): Lista de usuarios.

    Returns:
        dict: Usuario encontrado o False.
    """
    for i, user in  enumerate(user_list):
        if user.id == id:
            return user_list[i]
    return False
