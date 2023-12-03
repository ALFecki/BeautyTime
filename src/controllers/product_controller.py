from fastapi import APIRouter, Depends, Path
from services.product_service import ProductService
from schemas.product.product_create_schema import ProductSchemaCreate
from schemas.product.product_update_schema import ProductSchemaUpdate


router = APIRouter(prefix="/api/product", tags=["product"])


@router.get("/")
async def get_all_products(service=Depends(ProductService)):
    return await service.get_all()


@router.get("/{id}")
async def get_product_by_id(
    id: int = Path(example=1, description="ID искомого продукта"),
    service=Depends(ProductService),
):
    return await service.get_by_id(id)


@router.post("/")
async def create_product(
    create_schema: ProductSchemaCreate, service=Depends(ProductService)
):
    return await service.create(create_schema)


@router.patch("/{id}")
async def update_product(
    update_schema: ProductSchemaUpdate,
    id: int = Path(example=1, description="ID обновляемого продукта"),
    service=Depends(ProductService),
):
    return await service.update(id, update_schema)


@router.delete("/{id}")
async def delete_product(
    id: int = Path(example=1, description="ID удаляемого продукта"),
    service=Depends(ProductService),
):
    return await service.delete(id)
