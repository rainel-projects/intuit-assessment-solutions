Sales Data Analysis — Functional Programming Assignment
🧩 Intuit SWE-1 Take-Home Assessment — Assignment 2
📌 Overview

This project demonstrates functional programming concepts in Python by performing analytical operations on sales data stored in a CSV file.

The solution uses:

Lambda expressions

map(), filter(), and reduce()

itertools.groupby() for grouping

Functional-style aggregation

Modular, scalable architecture

This aligns with the assignment objective:

“Perform data analysis using appropriate APIs with functional programming and stream-like operations.”

🏗️ Project Structure
sales-analysis/
│
├── data/
│   └── sales.csv
│
├── src/
│   ├── models/
│   │   └── sale_record.py
│   │
│   ├── repository/
│   │   └── csv_loader.py
│   │
│   ├── analysis/
│   │   └── analytics_engine.py
│   │
│   ├── utils/
│   │   └── validators.py   (optional future utility)
│   │
│   ├── shared/
│   │   └── logger.py
│   │
│   └── runner/
│       └── app.py
│
├── tests/
│   └── test_analytics.py   (placeholder for unit tests)
│
├── README.md
└── requirements.txt

🧪 Sample CSV (data/sales.csv)
order_id,region,sales,category
1001,North,1200,Electronics
1002,South,800,Clothing
1003,North,600,Electronics
1004,West,400,Furniture
1005,South,1500,Electronics

▶ How to Run

From inside the project directory, run:

py -m src.runner.app


(Windows py launcher as requested.)

📌 Output Example
🚀 Running Sales Analytics...

[09:42:01] INFO → Loading data...
[09:42:01] INFO → Total Sales: 4500.0

[09:42:01] INFO → Sales by Region:
{'North': 1800.0, 'South': 2300.0, 'West': 400.0}

[09:42:01] INFO → Top Category:
('Electronics', 3300.0)

✔ Analysis Complete.

🧠 Functional Operations Used
Concept	Implementation
Lambda expressions	Used for sorting, reductions, grouping
Reduce operation	Summing sales values
Grouping	itertools.groupby()
Stream-like chaining	Sorting → grouping → aggregation
Data representation	Custom SaleRecord model class
✔ Assignment Requirements Coverage
Requirement	Status
Functional programming	✔
Stream-style operations	✔
Lambda expressions	✔
CSV data ingestion	✔
Aggregation & grouping	✔
Clean modular structure	✔
Testing-ready architecture	✔
🚀 Future Improvements (Optional Enhancements)

Add CLI arguments: --region, --category, or --top-n

Export results to JSON or database

Add visualization (Matplotlib/Pandas)

Implement more queries (min, max, AVG sales)

🏁 Summary

This solution demonstrates the ability to:

Process structured data from CSV

Apply functional-style transformations

Use clean modular architecture

Produce analytical insights using Python’s functional programming tools

It is designed for clarity, maintainability, and scalability — matching real engineering standards.