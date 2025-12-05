from src.repository.csv_loader import load_sales
from src.analysis.analytics_engine import AnalyticsEngine
from src.shared.logger import logger

DATA_PATH = "data/sales.csv"

if __name__ == "__main__":
    logger.info("Loading data...")
    records = load_sales(DATA_PATH)

    logger.info(f"Total Sales: {AnalyticsEngine.total_sales(records)}")

    logger.info("Sales by Region:")
    print(AnalyticsEngine.sales_by_region(records))

    logger.info("Top Category:")
    print(AnalyticsEngine.top_category(records))
