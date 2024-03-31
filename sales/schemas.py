# schemas.py
from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    store: int
    date: date
    weekly_sales: float
    holiday_flag: bool
    temperature: float
    fuel_price: float
    cpi: float
    unemployment: float

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    pass

class SaleSchema(SaleBase):
    id: int

    class Config:
        orm_mode = True
