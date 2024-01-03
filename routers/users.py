from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#crear una api para usuarios
router = APIRouter()

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
@router.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "{'error': 'no se encontró el usuario'}"

#por query
@router.get("/user/")
async def user(id: int):
    return search_user(id)

@router.get("/users/", status_code=201)
async def user():
    return users_list

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "{'error': 'no se encontró el usuario'}"


#si queremos agragar usuarios
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        #el raise propaga la excepcion, no lo la lanza y la retorna
        raise HTTPException(status_code=204,detail='el usuario ya existe')
        #return {'error': 'el usuario ya existe'}

    else:
        users_list.append(user)
        return {'message': 'se agrego el usuario'}



#actualizar el usuario
@router.put("/user")
async def user(user : User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index]= user
            found = True
            return {'message': 'se actualizó el usuario'}

    if not found:
        return "{'error': 'no se actualizó el usuario'}"

@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return "{'message': 'se elimino el usuario'}"
    if not found:
        return "{'error': 'no se elimino'}"
    
