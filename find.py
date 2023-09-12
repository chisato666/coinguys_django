import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver


chromedriver ='/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html"

driver.get(url)

#btcs= driver.find_elements_by_class_name("hidden-phone")

coins = driver.find_element_by_xpath("/html/body/div[5]/table[1]/tbody/tr[1]/td[4]")
print(coins.text)


# for btc in btcs:
#    print(btc.text)

