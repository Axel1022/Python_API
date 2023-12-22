from fastapi import FastAPI
from app.routers import routerUser, routerProducts

# Crea una instancia de la aplicación
app = FastAPI()

# Iniciar server: python -m uvicorn main:app --reload
# Url: http://127.0.0.1:8000/docs
# Documentacion: https://fastapi.tiangolo.com/es/tutorial/first-steps/

#routers
app.include_router(routerUser.router)
app.include_router(routerProducts.router)
app.mount
