from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = set_chrome_driver()


url = 'https://google.com'

driver.get(url)

element = driver.find_element(By.CLASS_NAME, 'gLFyf')

element.send_keys('nasdaq:nkla site:https://www.prnewswire.com/')

element.submit()

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

list = soup.select(".DKV0Md")

for item in list:

  print(item.text)

# print(soup)

driver.quit()

