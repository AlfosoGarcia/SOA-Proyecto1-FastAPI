from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.product import Product

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        result = await self.db.execute(select(Product).where(Product.id == product_id))
        return result.scalar_one_or_none()

    async def get_by_sku(self, sku: str) -> Optional[Product]:
        result = await self.db.execute(select(Product).where(Product.sku == sku))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10, name: Optional[str] = None) -> Sequence[Product]:
        query = select(Product)
        if name:
            query = query.where(Product.name.icontains(name))
        query = query.offset(skip).limit(limit)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def create(self, product: Product) -> Product:
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        return product

    async def update(self, product: Product, update_data: dict) -> Product:
        for key, value in update_data.items():
            setattr(product, key, value)
        await self.db.commit()
        await self.db.refresh(product)
        return product

    async def delete(self, product: Product) -> None:
        await self.db.delete(product)
        await self.db.commit()