from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

import re
# import pandas as pd
import os

url = "https://www.staples.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

barcode = "263155"


search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys(barcode)
driver.find_element_by_id("search-search-btn").click()
print(driver.find_element_by_class_name("delivery-info__price").text)


driver.quit()
