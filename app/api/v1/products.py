from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductPut, ProductUpdate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(prefix="/api/v1/products", tags=["Products"])

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    payload: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    service = ProductService(db)
    return await service.create_product(payload)

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    service = ProductService(db)
    return await service.list_products(skip=skip, limit=limit, name=name)

@router.get("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    service = ProductService(db)
    return await service.get_product_by_id(id)

@router.put("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def replace_product(
    id: int,
    payload: ProductPut,
    db: AsyncSession = Depends(get_db)
):
    service = ProductService(db)
    return await service.replace_product(id, payload)

@router.patch("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(
    id: int,
    payload: ProductUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = ProductService(db)
    return await service.update_product_partial(id, payload)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    service = ProductService(db)
    await service.delete_product(id)
    return None