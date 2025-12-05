Producer–Consumer Concurrency Simulation (Python)
⚙️ Take-Home Assessment — Intuit SWE-1
📌 Overview

This project implements the classic Producer–Consumer pattern using:

Python threading module

A blocking queue for safe shared data exchange

Controlled shutdown signaling between threads

Logging for visibility of execution flow

Clean modular folder structure for maintainability

The program simulates concurrent data transfer, where the Producer generates items and places them into a shared queue, and the Consumer retrieves and processes them.

🏗️ Architecture & Design Decisions
Component	Responsibility
Producer thread	Generates data and pushes items into queue
Consumer thread	Retrieves items and stores them in destination container
Queue (blocking)	Ensures thread-safe communication and synchronization
Graceful shutdown signal (None)	Notifies consumer to stop when work is complete
Config + Logger	Improves readability, debugging, and scalability

Python’s queue.Queue internally handles locks, wait/notify, and thread coordination — making it ideal for this pattern.

📂 Folder Structure
producer-consumer/
│
├── src/
│   ├── core/
│   │   ├── producer.py
│   │   ├── consumer.py
│   │   └── base.py
│   │
│   ├── shared/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── runner/
│   │   └── app.py
│   │
│   └── utils/
│       └── queue_factory.py
│
├── tests/
│   └── test_flow.py
│
├── README.md
└── requirements.txt

▶ How to Run

From inside the project folder, run:

py -m src.runner.app


✔ No additional dependencies required.
✔ Works with Python 3.8+

🧪 Sample Output
🚀 Starting Producer-Consumer Simulation...

[08:18:14] INFO → [PRODUCE] 1 | Queue Size: 1
[08:18:15] INFO → [CONSUME] 1 | Queue Size: 0
[08:18:15] INFO → [PRODUCE] 2 | Queue Size: 1
...
Producer completed.
Consumer received shutdown signal.
Final stored items: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

✔ Simulation Complete.

✔ Requirements Met
Requirement	Status
Producer–Consumer simulation	✔
Thread synchronization	✔
Blocking queue usage	✔
Communication between threads	✔
Graceful shutdown mechanism	✔
Readable + maintainable structure	✔
Supports future scaling	✔