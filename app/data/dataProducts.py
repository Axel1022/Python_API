from app.models.modelProduct import Product

def obtener_lista_productos():
    ProductList = [
        Product(id=1, name = "Test1"),
        Product(id=2, name = "Test2"),
        Product(id=3, name = "Test3")
    ]
    return ProductList
'''
class Product(BaseModel):
    id : int;
    name : str;
'''
