# scraper.py
import re
import time
import requests
from bs4 import BeautifulSoup
from utils import get_random_headers, setup_logging

logger = setup_logging()

class DivarScraper:
    BASE_URL = "https://divar.ir/s/"

    def __init__(self, city="tehran", timeout=10, retries=2):
        self.city = city
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update(get_random_headers())

    def _fetch_page(self, query):
        url = f"{self.BASE_URL}{self.city}?q={query}"
        for attempt in range(self.retries):
            try:
                resp = self.session.get(url, timeout=self.timeout)
                if resp.status_code == 200:
                    return resp.text
                else:
                    logger.warning(f"HTTP {resp.status_code} for '{query}', attempt {attempt+1}")
            except Exception as e:
                logger.error(f"Request error: {e}, attempt {attempt+1}")
            time.sleep(2)
        return None

    def extract_prices(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        price_list = []
        cards = soup.find_all('div', class_='kt-post-card__description')
        if not cards:
            cards = soup.find_all('div', {'class': re.compile(r'post-card|kt-post-card')})

        for card in cards:
            text = card.get_text(separator=' ')
            match = re.search(r'(\d[\d,]*)\s*(تومان|Toman)', text)
            if match:
                price_str = match.group(1).replace(',', '').replace('٬', '')
                persian_digits = '۰۱۲۳۴۵۶۷۸۹'
                english_digits = '0123456789'
                trans = str.maketrans(persian_digits, english_digits)
                price_str = price_str.translate(trans)
                try:
                    price = int(price_str)
                    price_list.append(price)
                except:
                    continue
            if len(price_list) >= 20:
                break
        return price_list

    def get_average_price(self, query):
        html = self._fetch_page(query)
        if not html:
            logger.error(f"Failed to fetch data for '{query}'")
            return None
        prices = self.extract_prices(html)
        if not prices:
            logger.warning(f"No prices found for '{query}'")
            return None
        avg = sum(prices) / len(prices)
        logger.info(f"Found {len(prices)} items for '{query}'; avg = {avg:,.0f} Toman")
        return round(avg)