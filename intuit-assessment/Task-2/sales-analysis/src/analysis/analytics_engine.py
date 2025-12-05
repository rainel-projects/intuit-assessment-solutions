from functools import reduce
from itertools import groupby

class AnalyticsEngine:

    @staticmethod
    def total_sales(records):
        return reduce(lambda total, r: total + r.sales, records, 0)

    @staticmethod
    def sales_by_region(records):
        records_sorted = sorted(records, key=lambda r: r.region)
        return {
            region: reduce(lambda total, r: total + r.sales, group, 0)
            for region, group in groupby(records_sorted, key=lambda r: r.region)
        }

    @staticmethod
    def top_category(records):
        records_sorted = sorted(records, key=lambda r: r.category)
        totals = {
            category: reduce(lambda total, r: total + r.sales, group, 0)
            for category, group in groupby(records_sorted, key=lambda r: r.category)
        }
        return max(totals.items(), key=lambda x: x[1])
