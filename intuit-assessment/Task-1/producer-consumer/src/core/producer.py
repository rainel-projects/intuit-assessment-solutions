import time, random
from src.core.base import BaseThread
from src.shared.logger import logger
from src.shared.config import PRODUCER_DELAY

class Producer(BaseThread):
    def __init__(self, queue, total_items):
        super().__init__("Producer")
        self.queue = queue
        self.total_items = total_items

    def run(self):
        for item in range(1, self.total_items + 1):
            time.sleep(random.uniform(*PRODUCER_DELAY))
            self.queue.put(item)
            logger.info(f"[PRODUCE] {item} | Queue Size: {self.queue.qsize()}")

        self.queue.put(None)
        logger.info("Producer completed.")
