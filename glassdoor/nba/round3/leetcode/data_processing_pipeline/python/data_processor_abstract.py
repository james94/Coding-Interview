from abc import ABC, abstractmethod

class DataProcessorAbstract(ABC):
    def __init__(self, num_threads):
        pass

    @abstractmethod
    def producer(self, data):
        pass

    @abstractmethod
    def consumer(self):
        pass
    
    @abstractmethod
    def process_item(self, item):
        pass

    @abstractmethod
    def run(self):
        pass
