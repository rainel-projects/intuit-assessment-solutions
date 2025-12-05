import csv
from src.models.sale_record import SaleRecord

def load_sales(file_path):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        return [SaleRecord(r["order_id"], r["region"], r["sales"], r["category"]) for r in reader]
