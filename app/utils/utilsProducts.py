from fastapi import HTTPException;
import db.models.modelProduct

def buscarId(id: int, produc_list):
    """
    Busca un producto por ID en la lista de productos.

    Args:
        id (int): ID del producto a buscar.
        produc_list (list): Lista de productos.

    Returns:
        dict: True o False
    """
    for produc in produc_list:
        if produc.id == id:
            return True
    return False

def buscarproduc(id: int, produc_list):
    """
    Busca un producto por ID en la lista de productos.

    Args:
        id (int): ID del producto a buscar.
        produc_list (list): Lista de productos.

    Returns:
        dict: producto encontrado o False.
    """
    for i, produc in  enumerate(produc_list):
        if produc.id == id:
            return produc_list[i]
    return False
