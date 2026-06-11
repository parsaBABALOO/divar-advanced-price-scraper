# main.py
import json
from scraper import DivarScraper

def main():
    print("\n🔍 Divar Advanced Price Scraper (Interactive)")
    print("---------------------------------------------")
    
    query = input("Enter product name (e.g., 'پراید', 'iphone', 'ps5'): ").strip()
    if not query:
        print("❌ Invalid product name.")
        return
    
    city = input("Enter city name (default 'tehran'): ").strip()
    if not city:
        city = "tehran"
    
    output_type = input("Output format (text/json) [default text]: ").strip().lower()
    if output_type not in ['text', 'json']:
        output_type = 'text'
    
    print("\n⏳ Fetching data from Divar...")
    
    scraper = DivarScraper(city=city)
    avg = scraper.get_average_price(query)
    
    if avg is None:
        if output_type == 'json':
            print(json.dumps({"error": "No data found", "query": query, "city": city}, ensure_ascii=False))
        else:
            print("❌ No valid ads found for this product.")
        return
    
    if output_type == 'json':
        result = {"query": query, "city": city, "average_price_toman": avg}
        print(json.dumps(result, ensure_ascii=False))
    else:
        print("\n🏠 Search Result:")
        print(f"   City: {city}")
        print(f"   Product: {query}")
        print(f"💰 Average price: {avg:,.0f} Toman")
    
    again = input("\nDo you want to search again? (y/n): ").strip().lower()
    if again in ['y', 'yes']:
        print("\n" + "-"*40)
        main()
    else:
        print("👋 Goodbye.")

if __name__ == "__main__":
    main()