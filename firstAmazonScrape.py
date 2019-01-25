from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException


import re
# import pandas as pd
import os



# try:
#     print(driver.find_element_by_id("priceblock_ourprice").text)
# except:
#     print(driver.find_element_by_id("priceblock_dealprice").text)
# else:
#     print("it worked")
    # else statement will be executed if no erros occured and only for the except statement?



# search amazon Overwatch Legendary edition ps4
url = "https://www.amazon.com"
asin = ["B07D9QWSG1","B07DL2SY2B"]
prices = {}


for x in asin:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(x)
    driver.find_element_by_class_name("nav-input").click()
    driver.find_element_by_css_selector("h2.a-size-medium.s-inline.s-access-title.a-text-normal").click()
    try:
        # print(driver.find_element_by_class_name("buyingPrice").text)
        price = driver.find_element_by_class_name("buyingPrice").text
    except:
        # print(driver.find_element_by_class_name("price-large").text)
        price = driver.find_element_by_class_name("price-large").text
    prices[x] = price


print(prices)
driver.quit()
