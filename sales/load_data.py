import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sales.models import WalmartSales
from core.config import get_settings

settings = get_settings()

# Your CSV file path
CSV_FILE_PATH = "/Users/vedrannikolic/Desktop/IIS6/data/Walmart_sales.csv"

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_sales_data(csv_file_path: str):
    # Load the CSV into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Rename DataFrame columns to match the WalmartSales model attribute names exactly
    df.rename(columns={
        'Store': 'Store',
        'Date': 'Date',
        'Weekly_Sales': 'Weekly_sales',
        'Holiday_Flag': 'Holiday_flag',
        'Temperature': 'Temperature',
        'Fuel_Price': 'Fuel_price',
        'CPI': 'Cpi',
        'Unemployment': 'Unemployment',
    }, inplace=True)

    # Convert the 'Date' column to the correct MySQL format (YYYY-MM-DD)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')

    # Convert the DataFrame to a list of dictionaries
    sales_data = df.to_dict(orient='records')
    
    db = SessionLocal()
    try:
        # Iterate over the sales data and add each entry to the session
        for sale in sales_data:
            db.add(WalmartSales(**sale))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    load_sales_data(CSV_FILE_PATH)
