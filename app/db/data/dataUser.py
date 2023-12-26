from app.db.models.modelUser import User

def obtener_lista_usuarios():
    usersList = [
        User(id=1, name="Alexander", surname="Campusano", url="www.campusano.com", age=15),
        User(id=2, name="Gary", surname="Campusano", url="www.campusano.com", age=15),
        User(id=3, name="David", surname="Campusano", url="www.campusano.com", age=15),
        User(id=4, name="Carmelo", surname="Campusano", url="www.campusano.com", age=15)
    ]
    return usersList
