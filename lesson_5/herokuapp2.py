from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

# Модальное окно(Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'div.modal-footer').click()
sleep(1)

# Модальное окно(Firefox)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'div.modal-footer').click()
sleep(1)
driver.quit()
