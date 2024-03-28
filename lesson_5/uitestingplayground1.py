from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

# Клик по кнопке без ID(Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid") 

for button in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

sleep(2)

# Клик по кнопке без ID(Firefox)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid") 

for button in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

sleep(2)
driver.quit()
