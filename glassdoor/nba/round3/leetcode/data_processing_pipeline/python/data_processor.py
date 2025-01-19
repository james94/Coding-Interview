import threading
from queue import Queue
import time
import random

from data_processor_abstract import DataProcessorAbstract

"""
This solution addresses several key points:

- Uses multiple threads for concurrent processing, improving efficiency
- Handles synchronization using a queue and lock
- It's scalable, allowing for a variable number of consumer threads
- Properly handles the termination of threads using sentinel values

Time Complexity: O(n), where n is the number of data items, each processed once

Space Complexity: O(n) for storing input data and results
"""
class DataProcessor(DataProcessorAbstract):
    """
    Encapsulates our multithreaded pipeline
    """
    def __init__(self, num_threads):
        super(DataProcessorAbstract, self).__init__()

        self.queue = Queue()
        self.result = []
        self.num_threads = num_threads
        self.lock = threading.Lock()

    def producer(self, data):
        """
        Puts data items into the queue and adds sentinel values (None)
        to signal the end of data
        """
        for item in data:
            self.queue.put(item)

        for _ in range(self.num_threads):
            self.queue.put(None)

    def consumer(self):
        """
        Continuously takes items from the queue, processes them, and adds
        the results to the shared 'result' list. It stops when it encounters
        a sentinel value.

        We use lock to ensure thread-safe appending to 'result' list
        """
        while True:
            item = self.queue.get()

            if item is None:
                break

            processed_item = self.process_item(item)

            with self.lock:
                self.result.append(processed_item)

            self.queue.task_done()
    
    def process_item(self, item):
        # Simulate processing time
        time.sleep(random.uniform(0.1, 0.5))
        return f"Processed: {item['name']} - {item['team']} - {item['stats']}"

    def run(self, data):
        """
        Orchestrates the pipeline:
            - Starts a producer thread to feed data into the queue
            - Starts multiple consumer threads (specified by 'num_threads')
            to process data concurrently
            - Waits for all threads to complete before returning the result 
        """
        producer_thread = threading.Thread(target=self.producer, args=(data,))
        producer_thread.start()

        consumer_threads = []

        for _ in range(self.num_threads):
            t = threading.Thread(target=self.consumer)
            t.start()

            consumer_threads.append(t)

        producer_thread.join()
        for t in consumer_threads:
            t.join()

        return self.result