import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://www.merinolaminates.com/en/product_category/merinolam/")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")
print(elem)
