from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

# Форма авторизации(Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login") 

username = '#username'
username_input = driver.find_element(By.CSS_SELECTOR, username)
sleep(1)
username_input.send_keys('tomsmith')
sleep(1)

password = '#password'
password_input = driver.find_element(By.CSS_SELECTOR, password)
sleep(1)
password_input.send_keys('SuperSecretPassword!')
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
sleep(1)

# Форма авторизации(Firefox)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login") 

username = '#username'
username_input = driver.find_element(By.CSS_SELECTOR, username)
sleep(1)
username_input.send_keys('tomsmith')
sleep(1)

password = '#password'
password_input = driver.find_element(By.CSS_SELECTOR, password)
sleep(1)
password_input.send_keys('SuperSecretPassword!')
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
sleep(1)
driver.quit()
