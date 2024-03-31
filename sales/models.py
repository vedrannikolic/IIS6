from sqlalchemy import Column, Integer, Float, Boolean, Date, String
from core.database import Base  # Adjust the import path according to your project structure

class WalmartSales(Base):
    __tablename__ = "walmart_sales"
    id = Column(Integer, primary_key=True, index=True)
    Store = Column(Integer, index=True)
    Date = Column(Date)
    Weekly_sales = Column(Float)
    Holiday_flag = Column(Boolean)
    Temperature = Column(Float)
    Fuel_price = Column(Float)
    Cpi = Column(Float)
    Unemployment = Column(Float)

    def __repr__(self):
        # Customize this to display the information you find most useful
        return f"<WalmartSales store={self.store} date={self.date} sales={self.weekly_sales}>"
