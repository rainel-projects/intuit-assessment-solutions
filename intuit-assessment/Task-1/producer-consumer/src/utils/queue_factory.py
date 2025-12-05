from queue import Queue
from src.shared.config import BUFFER_SIZE

def create_queue():
    return Queue(maxsize=BUFFER_SIZE)
