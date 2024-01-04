from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password : str

users_db = {
    "leosegoli":
    {
    'username': 'leosegoli',
    'full_name': 'leonardo segoli',
    'email': 'leosegoli@gmail.com',
    'disabled': False,
    'password': '123456'
    },
    "mouredev":
    {
    'username': 'mouredev',
    'full_name': 'Brais Moure',
    'email': 'brais@gmail.com',
    'disabled': False,
    'password': '654321'

    },
    }

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
     

#crear criterio de dependencia asincrono
async def current_user(token: str = Depends(oauth2)):
    user = search_user_db(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Las credenciales son inválidas", 
            headers={"WWW-Authenticate": "Baerer"}
            )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="usuario inactivo"
            )
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400,detail='el usuario no es correcto')
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400,detail='la contraseña no es correcta')

    return {"acces_token": user.username,"token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user