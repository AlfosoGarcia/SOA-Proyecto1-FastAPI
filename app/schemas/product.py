from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, NonNegativeFloat, NonNegativeInt

class ProductBase(BaseModel):
    sku: str = Field(..., min_length=1, max_length=50, example="PROD-001")
    name: str = Field(..., min_length=1, max_length=100, example="Laptop Gamer")
    price: NonNegativeFloat = Field(..., example=1250.50)
    stock: NonNegativeInt = Field(..., example=10)

class ProductCreate(ProductBase):
    pass

class ProductPut(ProductBase):
    pass

class ProductUpdate(BaseModel):
    sku: Optional[str] = Field(None, min_length=1, max_length=50)
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    price: Optional[NonNegativeFloat] = None
    stock: Optional[NonNegativeInt] = None

class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)