# Practical 4
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque

class WebCrawler:
    def __init__(self, seed_url, max_pages=100):
        self.seed_url = seed_url
        self.max_pages = max_pages
        self.visited_urls = set()
        self.queue = deque([(seed_url, 0)])

    def crawl(self):
        while self.queue and len(self.visited_urls) < self.max_pages:
            url, depth = self.queue.popleft()
            if url in self.visited_urls: continue
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    self.visited_urls.add(url)
                    self.index_page(url, response.text)
                    if depth < 2:
                        self.extract_links(response.text, depth + 1)
            except Exception as e:
                print(f"Error fetching URL {url}: {e}")

    def extract_links(self, html, depth):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                self.queue.append((href, depth))
            else:
                base_url = urlparse(self.seed_url)
                full_url = urljoin(f"{base_url.scheme}://{base_url.netloc}", href)
                self.queue.append((full_url, depth))

    def index_page(self, url, content):
        print(f"Indexing page: {url}")

# Example usage
crawler = WebCrawler(seed_url='https://example.com', max_pages=5)
crawler.crawl()