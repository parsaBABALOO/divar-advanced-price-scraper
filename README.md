# Divar Advanced Price Scraper 🏠📊

A professional interactive CLI tool to scrape average prices from Divar.ir (Iranian classifieds) with English prompts, JSON output, and auto‑retry.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/requests-latest-green.svg)](https://pypi.org/project/requests/)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4.12+-orange.svg)](https://pypi.org/project/beautifulsoup4/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Features

- ✅ Interactive English CLI – asks you for product, city, and output format  
- ✅ Scrapes real listing prices from Divar.ir  
- ✅ Persian digit conversion (automatically handles ۱۲۳ → 123)  
- ✅ Output as plain text or JSON – easy to integrate into other scripts  
- ✅ Random User‑Agent and retry logic to avoid blocks  
- ✅ Sample HTML file included (divar_sample.html) – you can test parsing offline  

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| main.py | Interactive CLI entry point |
| scraper.py | Core scraping logic (DivarScraper class) |
| utils.py | Random headers and logging setup |
| divar_sample.html | A saved copy of Divar search results (for testing/development) |
| requirements.txt | Python dependencies |
| README.md | This file |

---

## 🚀 Installation & Usage

### 1. Clone the repository

`bash
git clone https://github.com/YOUR_USERNAME/divar-advanced-price-scraper.git
cd divar-advanced-price-scraper

### 2. Install dependencies
`bash
pip install -r requirements.txt

### 3. Run the Scraper
`bash
python main.py

### Example output
Text format
🏠 Search Result:
   City: tehran
   Product: iphone
💰 Average price: 35,500,000 Toman

JSON format
{
  "query": "iphone",
  "city": "tehran",
  "average_price_toman": 35500000
}

🧪 Offline testing with the included HTML file

The repository contains divar.html – a real saved page from Divar search results.
You can use it to test price extraction without an internet connection:

from scraper import DivarScraper

scraper = DivarScraper()
with open("divar.html", "r", encoding="utf-8") as f:
    html = f.read()
prices = scraper.extract_prices(html)
print(prices)

---

⚠️ Important notes

· Divar may change its HTML structure over time. If scraping stops working, update the CSS class patterns in scraper.py (kt-post-card__description, etc.).
· This tool is for educational and personal use only. Respect Divar's terms of service and do not send too many requests in a short time.
· For production or heavy usage, consider using proxies and rotating IPs.

---

🤝 Contributing

Issues and pull requests are welcome. Please make sure to test any changes with the sample HTML file.

---

👤 Author

Your Name : PARSA BABALOO

🔗 Other project: PBX-Crypto Forecasting Engine

---

⭐ If this tool helped you, please give it a star!
