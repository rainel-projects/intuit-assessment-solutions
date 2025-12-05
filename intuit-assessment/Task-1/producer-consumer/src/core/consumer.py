import time, random
from src.core.base import BaseThread
from src.shared.logger import logger
from src.shared.config import CONSUMER_DELAY

class Consumer(BaseThread):
    def __init__(self, queue):
        super().__init__("Consumer")
        self.queue = queue
        self.storage = []

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                logger.info("Consumer received shutdown signal.")
                break

            time.sleep(random.uniform(*CONSUMER_DELAY))
            self.storage.append(item)
            logger.info(f"[CONSUME] {item} | Queue Size: {self.queue.qsize()}")

        logger.info(f"Final stored items: {self.storage}")
