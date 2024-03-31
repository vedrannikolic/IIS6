from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from pymysql import OperationalError
from core.database import get_db, SessionLocal
from sales.models import WalmartSales

app = FastAPI()
origins = [
    "http://127.0.0.1:5500",  # Your frontend origin
    # Add other origins as needed
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/sales")
def read_sales():
    return {"msg": "This is a test"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        # Attempt a simple database operation, e.g., fetching the first record of a table
        result = db.query(WalmartSales).first()
        return {"status": "success", "data": result}
    except OperationalError:
        return {"status": "error", "message": "Failed to connect to the database"}
