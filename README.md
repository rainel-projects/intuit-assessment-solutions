💼 Intuit SWE-1 Take-Home Assessment
Submitted by: Veda R
📌 Overview

This repository contains my completed solutions for the Intuit Software Engineer 1 take-home assignments. Both tasks are implemented in Python, as the instructions allowed completion in either Java or Python.

The solutions demonstrate:

Functional programming and data analysis

Concurrency and synchronization

Clean modular architecture

Error-handling and code readability

Real-world engineering practices (logging, structure, clarity)

🧠 Assignment Summary
Assignment	Description	Language	Status
Task 1	Producer-Consumer concurrency simulation	Python	✔ Completed
Task 2	Sales CSV analysis using functional programming (streams/lambdas)	Python	✔ Completed
🧵 Task 1 — Producer–Consumer Simulation
Purpose

Implements the classic Producer–Consumer pattern demonstrating:

Thread synchronization

Blocking queue interaction

Controlled shutdown signaling

Logging for execution visibility

📁 Folder Structure
producer-consumer/
│
├── src/
│   ├── core/
│   │   ├── producer.py
│   │   ├── consumer.py
│   │   └── base.py
│   │
│   ├── shared/
│   │   └── logger.py
│   │
│   ├── utils/
│   │   └── queue_factory.py
│   │
│   └── runner/
│       └── app.py
│
└── data/ (optional for logging/output storage)

▶ Run Command

From repository root:

py -m producer_consumer.src.runner.app

🧪 Sample Output
🚀 Starting Producer-Consumer Simulation...
[INFO] [PRODUCE] 1
[INFO] [CONSUME] 1
...
Producer completed.
Consumer received shutdown signal.
✔ Simulation Complete.

📊 Task 2 — Sales Data Analysis (Streams / Functional Programming)
Purpose

Reads a CSV and performs analytical queries using:

map, reduce, filter, lambda

Functional programming patterns

Grouping and aggregation similar to Java Streams

📁 Folder Structure
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
│   ├── shared/
│   │   └── logger.py
│   │
│   └── runner/
│       └── app.py

▶ Run Command
py -m sales_analysis.src.runner.app

🧪 Sample Output
📊 Running Sales Analytics...

Total Sales: 4500.0
Sales by Region: {'North': 1800.0, 'South': 2300.0, 'West': 400.0}
Top Category: ('Electronics', 3300.0)

✔ Analysis Complete.

✔ Requirement Coverage Matrix
Requirement	Task 1	Task 2
Threading / Concurrency	✔	—
Blocking Queue usage	✔	—
Functional programming	—	✔
Lambda expressions	—	✔
Aggregation & grouping	—	✔
Clean structured code	✔	✔
Modular repository	✔	✔
Logging & traceability	✔	✔
🚀 Possible Enhancements (If Extended)

CLI arguments for custom queries

Web interface for Task 2 visualization

Multiple producers/consumers extension

Pandas or database export option
