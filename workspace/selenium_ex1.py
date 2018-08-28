# selenium_ex1.py
# pip install selenium

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
browser.get("http://python.org")

pypi = browser.find_element_by_css_selector('#top > nav > ul > li.pypi-meta > a')
pypi.click()

time.sleep(5) # 5초 쉰다

browser.quit() # 종료
