import os
import json
import time
import tarfile
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def unzip_chromium():
    with tarfile.open('./chromium.tar.xz', 'r') as tar_file:
        tar_file.extractall('/tmp/chromium/')

    os.system('chmod 777 /tmp/chromium/*')


def run_selenium(url):
    dir = os.path.dirname(os.path.abspath(__file__))
    try:
        driver_path = "/tmp/chromium/chromedriver"
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.binary_location = "/tmp/chromium/chrome"

        driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        driver.get(url)

        time.sleep(3)
        driver.save_screenshot("/tmp/screenshot.png")

    except Exception as e:
        print(e)


def handler(event, context):
    unzip_chromium()
    run_selenium('https://www.google.com/')


if __name__ == "__main__":
    unzip_chromium()
    run_selenium('https://www.google.com/')
