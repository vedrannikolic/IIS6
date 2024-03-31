from sqlalchemy import Column, Integer, Float, Boolean, Date, String
from core.database import Base  # Adjust the import path according to your project structure

class WalmartSales(Base):
    __tablename__ = "walmart_sales"
    id = Column(Integer, primary_key=True, index=True)
    store = Column(Integer, index=True)
    date = Column(Date)
    weekly_sales = Column(Float)
    holiday_flag = Column(Boolean)
    temperature = Column(Float)
    fuel_price = Column(Float)
    cpi = Column(Float)
    unemployment = Column(Float)

    def __repr__(self):
        # Customize this to display the information you find most useful
        return f"<WalmartSales store={self.Store} date={self.Date} sales={self.Weekly_sales}>"
