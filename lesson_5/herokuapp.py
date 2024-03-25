from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/") 

for on_click in range(1, 6):
    driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()

delete_elements = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print(len(delete_elements))

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/") 

for on_click in range(1, 6):
    driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()

delete_elements = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print(len(delete_elements))

sleep(2)
