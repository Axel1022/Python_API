from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    userName: str
    fullName: str
    email: str
    desabled: bool

class UserDb(User):
    password: str

async def currentUser(token: str = Depends(oauth2)):
    user = verificarUserDB(token)
    if user:
        if user.desabled:
            return user
        else:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inavilitado")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )

ListUsersDb = {
    "ElmerCampu": {
        "userName": "ElmerCampu",
        "fullName": "Gary Alexander Campusano Paredes",
        "email": "ingcampusano@outlook.com",
        "desabled": True,
        "password": "333333"
    },
    "ElmerCampu2": {
        "userName": "ElmerCampu2",
        "fullName": "Gary Alexander Campusano Paredes",
        "email": "ingcampusano@outlook.com",
        "desabled": False,
        "password": "222222"
    },
    "ElmerCampu3": {
        "userName": "ElmerCampu3",
        "fullName": "Gary Alexander Campusano Paredes",
        "email": "ingcampusano@outlook.com",
        "desabled": False,
        "password": "111111"
    }
}

def verificarUser(userName: str):
    if userName in ListUsersDb:
        return User(**ListUsersDb[userName])

def verificarUserDB(userName: str):
    if userName in ListUsersDb:
        return UserDb(**ListUsersDb[userName])

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userDb = ListUsersDb.get(form.username)
    if userDb:
        user = verificarUserDB(form.username)
        if form.password == user.password:
            return {"access_token": user.userName, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña inválida")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")

@app.get("/users/me")
async def me(user: User = Depends(currentUser)):
    return user

