# Importa FastAPI
from typing import List
from fastapi import APIRouter
import sys
sys.path.append(r'C:\Users\IngCa\Desktop\Cursos\Python_API')
from app.data.dataProducts import obtener_lista_productos

router = APIRouter();
productList = obtener_lista_productos();

@router.get("/products")
async def getProduct():
    return productList
