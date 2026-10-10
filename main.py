from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.v1.products import router as products_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creación automática de tablas al iniciar
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Product Catalog & Inventory Microservice",
    version="1.0.0",
    description="API RESTful asíncrona con arquitectura en capas y SQLAlchemy 2.0",
    lifespan=lifespan
)

app.include_router(products_router)