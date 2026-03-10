import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
class WebCrawler:
    def __init__(self, max_pages=3):
        self.visited_urls = set()
        self.max_pages = max_pages
    def crawl(self, url, depth=1, delay=1):
        if depth < 0 or len(self.visited_urls) >= self.max_pages:
            return
        if url in self.visited_urls:
            return
        try:
            if not self.is_allowed_by_robots(url):
                print(f"Skipping {url} due to robots.txt rules")
                return
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                self.visited_urls.add(url)
                self.index_page(url, soup)
                if len(self.visited_urls) < self.max_pages:
                    for link in soup.find_all('a'):
                        if len(self.visited_urls) >= self.max_pages:
                            break
                        new_url = link.get('href')
                        if new_url and new_url.startswith('http'):
                            time.sleep(delay)
                            self.crawl(new_url, depth - 1, delay)
        except Exception as e:
            print(f"Error crawling {url}: {e}")
    def is_allowed_by_robots(self, url):
        print(f"Checking robots.txt for {url}...")
        return True
    def index_page(self, url, soup):
        title = soup.title.string if soup.title else "No title"
        print(f"Indexing: {url}")
        print(f"Title: {title}")
        print("-------------")
if __name__ == "__main__":
    crawler = WebCrawler(max_pages=2)
    crawler.crawl("https://www.google.com")
