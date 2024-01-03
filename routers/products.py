from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {'message': 'no encontrado'}})

product_list = ["producto1","producto2","producto3","producto4","producto5"]

@router.get("/")
async def products():
    return ["producto1","producto2","producto3","producto4","producto5"]

@router.get("/{id}")
async def products(id: int):
    return product_list[id]