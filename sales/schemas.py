# schemas.py
from typing import Optional
from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    store: int
    date: date
    weekly_sales: float
    holiday_flag: bool
    temperature: Optional[float] = None
    fuel_price: Optional[float] = None
    cpi: Optional[float] = None
    unemployment: Optional[float] = None

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    pass

class SaleSchema(SaleBase):
    id: int

    class Config:
        from_attributes = True
