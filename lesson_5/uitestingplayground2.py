from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr") 
sleep(1)
for button in range(1, 4):  
    driver.find_element(By.CSS_SELECTOR, 'button.btn.class3').click()
sleep(1)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr") 
sleep(1)
for button in range(1, 4):  
    driver.find_element(By.CSS_SELECTOR, 'button.btn.class3').click()
sleep(1)
