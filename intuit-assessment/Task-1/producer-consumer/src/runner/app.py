from src.utils.queue_factory import create_queue
from src.core.producer import Producer
from src.core.consumer import Consumer
from src.shared.config import TOTAL_ITEMS

if __name__ == "__main__":
    print("\n🚀 Starting Producer-Consumer Simulation...\n")

    queue = create_queue()

    producer = Producer(queue, TOTAL_ITEMS)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("\n✔ Simulation Complete.\n")
