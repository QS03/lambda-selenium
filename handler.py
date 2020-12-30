import os
import json
from datetime import datetime
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def handler(event, context):
    run_scrapper('https://google.com')


def run_scrapper(url):

    try:
        print(f"Started at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")

        dir = os.path.dirname(os.path.abspath(__file__))
        driver_path = dir + "/bin/chromedriver"
        chrome_options = Options()

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")

        chrome_options.binary_location = dir + "/bin/headless-chromium"
        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        driver.get(url)

        driver.save_screenshot("/tmp/screenshot.png")
        size = os.path.getsize("/tmp/screenshot.png")
        print(f"Image size: {size}")

        print(f"Completed at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    run_scrapper('https://google.com')
