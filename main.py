from fastapi import FastAPI
from app.routers import routerUser, routerProducts

# Crea una instancia de la aplicación
app = FastAPI()

#routers
app.include_router(routerUser.router)
app.include_router(routerProducts.router)
