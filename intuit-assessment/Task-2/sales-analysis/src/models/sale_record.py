class SaleRecord:
    def __init__(self, order_id, region, sales, category):
        self.order_id = int(order_id)
        self.region = region
        self.sales = float(sales)
        self.category = category

    def __repr__(self):
        return f"<SaleRecord {self.order_id} - {self.region} - {self.sales}>"
