from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.models.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId


router = APIRouter(prefix="/userdb",
                   tags=["userdb"],)


users_list = []


@router.get("/{id}")
async def user(id: str):
    return search_user('_id', ObjectId(id))


@router.get("/", response_model=list[User])
async def user():
    return users_schema(db_client.users.find())
    


@router.get("/")
async def user():
    return search_user('_id', ObjectId(id))

    


def search_user(field: str , key: str):
    try:
        user = db_client.users.find_one({field: key})
        new_user =  User(**user_schema(user))
        print("se encontro por consola")
        return new_user
    except:
        return "{'error': 'no se encontró el usuario'}"
    

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user('email',user.email)) == User:
        raise HTTPException(status_code=203,detail='el usuario ya existe')

    user_dict = dict(user)

    del user_dict['id']

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({'_id':id}))
 
    return User(**new_user)


@router.put("/", response_model=User)
async def user(user : User):
    user_dict = dict(user)
    del user_dict['id']

    try:
        db_client.users.find_one_and_replace({'_id': ObjectId(user.id)}, user_dict)
        
    except:
        return "{'error': 'no se actualizó el usuario'}"
    
    return search_user('_id', ObjectId(user.id))



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.find_one_and_delete({'_id': ObjectId(id)})
    if not found:
        return "{'error': 'no se elimino'}"
    
