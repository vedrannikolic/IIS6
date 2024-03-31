from sqlalchemy.orm import Session
from .models import WalmartSales
from .schemas import SaleCreate, SaleSchema, SaleUpdate

def create_sale(db: Session, sale: SaleCreate) -> WalmartSales:
    db_sale = WalmartSales(**sale.model_dump())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def update_sale(db: Session, sale_id: int, sale: SaleUpdate) -> WalmartSales:
    db_sale = db.query(WalmartSales).filter(WalmartSales.id == sale_id).first()
    if not db_sale:
        return None
    for var, value in sale.model_dump(exclude_unset=True).items():
        setattr(db_sale, var, value)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sales(db: Session, skip: int = 0, limit: int = 100) -> list[SaleSchema]:
    sales_records = db.query(WalmartSales).offset(skip).limit(limit).all()
    return [SaleSchema.from_orm(record) for record in sales_records]


