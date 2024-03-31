# schemas.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class SaleBase(BaseModel):
    store: int
    weekly_sales: float
    holiday_flag: bool
    temperature: Optional[float] = None
    fuel_price: Optional[float] = None
    cpi: Optional[float] = None
    unemployment: Optional[float] = None

class SaleCreate(SaleBase):
    date: Optional[datetime] = None

class SaleUpdate(SaleBase):
    pass

class SaleSchema(SaleBase):
    id: int

    class Config:
        from_attributes = True
