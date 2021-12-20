from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv = Service('chromedriver.exe')
drv = webdriver.Chrome(service=serv)
drv.get('http://google.com/ncr')
search_bar = drv.find_element(By.NAME, 'q')
search_bar.send_keys('selenide')
search_bar.send_keys(Keys.ENTER)
assert 'selenide.org' in drv.find_element(By.TAG_NAME, 'cite').text
drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
assert 'selenide.org' in drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]').text
drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
assert 'selenide.org' in drv.find_element(By.TAG_NAME, 'cite').text
drv.close()
