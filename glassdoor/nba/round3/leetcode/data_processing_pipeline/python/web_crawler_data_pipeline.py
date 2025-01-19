# from abc import ABC, abstractmethod

from data_processor import DataProcessor

import requests
import threading
from bs4 import BeautifulSoup

class WebCrawlerDataPipeline(DataProcessor):
    """
    Handles the multi-threaded crawling of web pages.
    Initializes with a start URL and the number of threads to use.
    """
    def __init__(self, start_url, num_threads=5):
        super().__init__(num_threads=num_threads)

        self.start_url = start_url
        self.queue.put(self.start_url)
        self.processed_urls = set()

    # producer is from url

    def crawl(self):
        """
        Is the main worker function for each thread, processing URLs from the queue
        """
        while True:
            url = self.queue.get()

            if url is None:
                break

            self.process_item(url)

            self.queue.task_done()

    def consumer(self):
        self.crawl()
    
    def extract_data(self, url, soup):
        """
        Prints the URL and title of each crawled page
        """
        # Simulating data extraction
        player_name = soup.find("h1", class_="player-name")
        player_stats = soup.find("div", class_="player-stats")
        if player_name and player_stats:
            data = {
                "url": url,
                "name": player_name.text.strip(),
                "stats": player_stats.text.strip()
            }

            with self.lock:
                self.result.append(data)

    def enqueue_links(self, soup):
        """
        Finds all links on a page and adds them to the queue if they're within the same domain
        """
        for link in soup.find_all("a", href=True):
            if link["href"].startswith("/players/"):
                full_url = f"https://www.nba.com{link['href']}"
                if full_url not in self.processed_urls:
                    self.queue.put(full_url)

    def process_url(self, url):
        """
        Handles the actual crawling of each URL, extracting information and enqueueing new links
        """
        if url not in self.processed_urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    self.extract_data(url, soup)
                    self.enqueue_links(soup)

                    with self.lock:
                        self.processed_urls.add(url)
            except Exception as e:
                print(f"Error processing {url}: str(e)")


    def process_item(self, item):
        self.process_url(item)

    def run(self):
        """
        Starts the specified number of threads and waits for them to complete
        """
        threads = []

        for _ in range(self.num_threads):
            t = threading.Thread(target=self.consumer)
            t.start()
            threads.append(t)

        for _ in range(self.num_threads):
            self.queue.put(None)

        for t in threads:
            t.join()

        return self.result
        