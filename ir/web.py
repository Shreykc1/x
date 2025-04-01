import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, depth=0, max_depth=1, visited=None):
    if visited is None:
        visited = set()
    if depth > max_depth or url in visited:
        return
    visited.add(url)
    try:
        html = requests.get(url).text
        print("Crawled:", url)
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all("a", href=True):
            crawl(urljoin(url, a["href"]), depth+1, max_depth, visited)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

crawl('https://mithibai.ac.in/')
