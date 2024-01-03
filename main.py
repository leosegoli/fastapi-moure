from fastapi import FastAPI

from routers import products
from routers import users
from fastapi.staticfiles import StaticFiles

app = FastAPI()


#routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {'message': 'Hola FastAPI'}

@app.get("/url")
async def root():
    return {'url': 'google.com'}


