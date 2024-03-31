from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sales.models import WalmartSales
from sales.schemas import SaleCreate, SaleSchema, SaleUpdate
from sales.services import create_sale, delete_sale, update_sale, get_sales
from core.database import get_db
from datetime import datetime, date

router = APIRouter(
    prefix="/sales",
    tags=["Sales"],
    responses={404: {"description": "Not found"}},
)

@router.post('', response_model=SaleSchema)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    if not sale.date:
        sale.date = datetime.now()
    db_sale = WalmartSales(**sale.model_dump(exclude_unset=True))
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.patch('/{sale_id}', response_model=SaleSchema)
def update_sale_route(sale_id: int, sale: SaleUpdate, db: Session = Depends(get_db)):
    updated_sale = update_sale(db=db, sale_id=sale_id, sale=sale)
    if updated_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated_sale

@router.get('', response_model=List[SaleSchema])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        sales = get_sales(db=db, skip=skip, limit=limit)
        return sales  # FastAPI handles serialization based on response_model
    except Exception as e:
        print(f"Error fetching sales: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete('/{sale_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_sale_route(sale_id: int, db: Session = Depends(get_db)):
    success = delete_sale(db=db, sale_id=sale_id)
    if not success:
        raise HTTPException(status_code=404, detail="Sale not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
