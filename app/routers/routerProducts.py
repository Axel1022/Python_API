# Importa FastAPI
from typing import List
from fastapi import APIRouter
import sys
sys.path.append(r'C:\products\IngCa\Desktop\Cursos\Python_API')
from app.data.dataProducts import obtener_lista_productos
from fastapi import HTTPException;
#import utils.utilsProducts
from app.models.modelProduct import Product
from fastapi.responses import JSONResponse

'''
Operaciones de ruta (GET, POST, PUT, DELETE...)
POST -> Para crear datos.
GET -> Para leer datos.
PUT -> Para actualizar datos.
DELETE -> Para borrar datos.
'''

router = APIRouter(prefix="/products", tags=["products"], responses={404:{"message":"No encontrado"}});
productList = obtener_lista_productos();

# Devuelve una lista de productos en formato JSON
@router.get("/",response_model=List[Product], status_code=200)
async def products():
    '''
    Devuelve una lista de productos en formato JSON.

    Returns:
        JSONResponse: Un objeto JSONResponse con la lista de productos en formato JSON si se encuentran productos.
                      En caso contrario, lanza una excepción HTTP 404 indicando que no se encontraron productos.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si no se encuentran productos.

    '''
    if not productList:
        raise HTTPException(status_code=404, detail="No se encontraron productos")
    else:
        return productList

# Devuelve un producto por el ID
@router.get("/{id}",response_model=Product, status_code=200)
async def product_id(id: int):
    '''
    Devuelve un producto según su ID.

    Args:
        id (int): El ID del producto a buscar.

    Returns:
        JSONResponse: Un objeto JSONResponse con la información del producto en formato JSON si se encuentra.
                      En caso contrario, lanza una excepción HTTP 404 si no se encuentra el producto.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si el producto con el ID especificado no se encuentra.

    '''

    product_found = buscarproduct(id, productList)
    if product_found:
        return product_found
    else:
        raise HTTPException(status_code=404, detail=f"producto con ID {id} no encontrado")

# Elimina un producto por el ID
@router.delete("/{id}", status_code=200, response_model=dict)
async def product_delete(id: int):
    """
    Elimina un producto según su ID.

    Args:
        id (int): El ID del producto a eliminar.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje indicando si la eliminación fue exitosa.
                      En caso contrario, lanza una excepción HTTP 404 si no se encuentra el producto.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si el producto con el ID especificado no se encuentra.

    """
    product_found = buscarproduct(id, productList)
    if product_found:
        productList.remove(product_found)
        return JSONResponse(content={"message": f"producto con ID {id} eliminado exitosamente"})
    else:
        raise HTTPException(status_code=404, detail=f"producto con ID {id} no encontrado")

@router.post("/",status_code=201, response_model=dict)
async def product_add(product: Product):
    """
    Añade un nuevo producto al sistema.

    Args:
        product (product): Los datos del nuevo producto a añadir.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje indicando si el producto fue añadido exitosamente.
                      En caso contrario, lanza una excepción HTTP 409 si el ID del producto ya existe.

    Raises:
        HTTPException: Se lanza con un código de estado 409 si el ID del producto ya existe.

    """
    id_found = buscarId(product.id, productList)
    if not id_found:
        productList.append(product)
        return JSONResponse(content={"message": f"producto {product.name} añadido exitosamente", "ID": f"{product.id}"})
    else:
        raise HTTPException(status_code=409, detail={"Error": "producto no añadido", "Descripción": f"El ID: {product.id} ya existe."})

#Actualizar
@router.put("/", status_code=200, response_model=dict)
async def product_Update(product: Product):
    """
    Edita un producto en la lista basándose en su ID.

    Args:
        product (product): El producto con los cambios.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje de confirmación si se realizó la edición correctamente.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si no se encontró el producto.
    """
    product_fund = buscarId(product.id, productList )
    if product_fund:
        for i, Saved_product in enumerate(productList):
            if Saved_product.id == product.id:
                productList[i] = product
                return JSONResponse(content={"message": "producto actualizado correctamente"})
    else:
        raise HTTPException(status_code=404, detail=f"product with id {product.id} not found")

@router.put("/{id}", status_code=200, response_model=dict)
async def product_Update(idActual: int, product: Product):
    '''
    Edita un producto en la lista basándose en su ID.

    Args:
        idActual (int): El ID del producto que se va a editar.
        product (product): El producto con los cambios.

    Returns:
        JSONResponse: Un objeto JSONResponse con un mensaje de confirmación si se realizó la edición correctamente.

    Raises:
        HTTPException: Se lanza con un código de estado 404 si no se encontró el producto.
                      Se lanza con un código de estado 304 si el ID del nuevo producto ya existe.
    '''

    product_fund_Actual = buscarId(idActual, productList )
    if product_fund_Actual:
        product_fund_New = buscarId(product.id, productList)
        if product_fund_New:
            raise HTTPException(status_code=304, detail={"Error": "producto no modificado", "Descripción": f"El ID: {product.id} ya existe."})

        for i, Saved_product in enumerate(productList):
            if Saved_product.id == idActual:
                productList[i] = product
                return {"message": "producto actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail=f"No existe un producto con ID {idActual}")

#Funciones'

def buscarproduct(id: int, produc_list):
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
