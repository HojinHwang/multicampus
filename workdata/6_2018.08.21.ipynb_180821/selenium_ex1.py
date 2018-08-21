# pip install selenium
# beatifulsoup로 안읽힐때 selenium 사용

from selenium import webdriver
import time

# selenium 다운 , 폴더위치 적기
browser = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
browser.get('https://python.org/')

# 크롤링 후 자동 넘어가기 pypi로
pypi = browser.find_element_by_css_selector('#top > nav > ul > li.pypi-meta > a')
pypi.click()

time.sleep(5) # 5초 쉰다

browser.quit() # 종료

