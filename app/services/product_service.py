from typing import Sequence, Optional
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductPut, ProductUpdate

class ProductService:
    def __init__(self, db: AsyncSession):
        self.repository = ProductRepository(db)

    async def create_product(self, schema: ProductCreate) -> Product:
        existing = await self.repository.get_by_sku(schema.sku)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with SKU '{schema.sku}' already exists."
            )
        new_product = Product(**schema.model_dump())
        return await self.repository.create(new_product)

    async def get_product_by_id(self, product_id: int) -> Product:
        product = await self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found."
            )
        return product

    async def list_products(self, skip: int = 0, limit: int = 10, name: Optional[str] = None) -> Sequence[Product]:
        return await self.repository.get_all(skip=skip, limit=limit, name=name)

    async def replace_product(self, product_id: int, schema: ProductPut) -> Product:
        product = await self.get_product_by_id(product_id)
        
        if schema.sku != product.sku:
            existing_sku = await self.repository.get_by_sku(schema.sku)
            if existing_sku:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with SKU '{schema.sku}' already exists."
                )

        return await self.repository.update(product, schema.model_dump())

    async def update_product_partial(self, product_id: int, schema: ProductUpdate) -> Product:
        product = await self.get_product_by_id(product_id)
        update_data = schema.model_dump(exclude_unset=True)

        if "sku" in update_data and update_data["sku"] != product.sku:
            existing_sku = await self.repository.get_by_sku(update_data["sku"])
            if existing_sku:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with SKU '{update_data['sku']}' already exists."
                )

        return await self.repository.update(product, update_data)

    async def delete_product(self, product_id: int) -> None:
        product = await self.get_product_by_id(product_id)
        await self.repository.delete(product)