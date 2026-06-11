# utils.py
import logging
from fake_useragent import UserAgent

def get_random_headers():
    ua = UserAgent()
    return {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br'
    }

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=level,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)