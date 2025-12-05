import threading

class BaseThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.daemon = True  # optional: threads stop with app
