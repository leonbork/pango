from utilities.api_helpers import ApiHelper
from utilities.scraper import WebScraper
from utilities.db_helpers import DatabaseHelper
from modules.constants import CITIES, THRESHOLD
from modules.report_generator import generate_report

def run_pipeline():
    print("Starting weather data collection pipeline...")
    api = ApiHelper()
    scraper = WebScraper()
    db = DatabaseHelper()
    for city in CITIES:
        try:
            print(f"Processing {city}...")
            t_api, f_api = api.get_current_weather(city)
            t_web, f_web = scraper.get_weather(city)
            db.insert_weather_data(city, t_web, f_web, t_api, f_api)
        except Exception as e:
            print(f"Error processing {city}: {e}")
    scraper.close()
    data = db.fetch_all_data()
    generate_report(data, threshold=THRESHOLD)
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()