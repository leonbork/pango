from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class WebScraper:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=options)

    def get_weather(self, city: str) -> tuple:
        url = f"https://www.timeanddate.com/weather/{city.lower().replace(' ', '-')}"
        self.driver.get(url)
        time.sleep(2)
        temp_text = self.driver.find_element(By.XPATH, '//div[@id="qlook"]/div[1]').text
        feels_like_text = self.driver.find_element(By.XPATH, '//div[@id="qlook"]/div[2]').text
        temperature = float(temp_text.split("\u00b0")[0])
        feels_like = float(feels_like_text.split("\u00b0")[0].split()[-1])
        return temperature, feels_like

    def close(self):
        self.driver.quit()