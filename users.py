from fastapi import FastAPI
from pydantic import BaseModel

#crear una api para usuarios
app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id= 1, name='Brais',surname='moure',url='moure.com',age=12),
              User(id= 2, name='leo',surname='sego',url='modfrase.com',age=155),
              User(id= 3, name='Braiss',surname='mourke',url='mouasdare.com',age=132)]


#por url
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "{'error': 'no se encontró el usuario'}"

#por query
@app.get("/user/")
async def user(id: int):
    return search_user(id)
   

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "{'error': 'no se encontró el usuario'}"


@app.get("/usersjson")
async def usersjson():
    return [{'name': 'Brais','surname': 'moure','url':'moure.com','age': 12},
            {'name': 'leo','surname': 'segoli','url': 'leo.com','age': 44},
            {'name': 'jon','surname': 'glan','url':'jon.com','age': 72}]



#si queremos agragar usuarios
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {'error': 'el usuario ya existe'}

    else:
        users_list.append(user)
