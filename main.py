from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hola FastAPI'}

@app.get("/url")
async def root():
    return {'url': 'google.com'}


