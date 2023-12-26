from app.models.modelProduct import Product

def obtener_lista_productos():
    productList = [
        Product(id=1, name="Laptop", description="Powerful laptop for productivity", price=999.99),
        Product(id=2, name="Smartphone", description="High-end smartphone with advanced features", price=699.99),
        Product(id=3, name="Headphones", description="Noise-canceling headphones for immersive audio", price=149.99),
        Product(id=4, name="Smartwatch", description="Fitness tracker with smartwatch features", price=199.99)
    ]
    return productList
