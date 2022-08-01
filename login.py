from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from framework8.selenium_wrapper import SeleniumWrapper
from config import Config

driver = Chrome(Config.DRIVER_PATH)
driver.get(Config.URL)
driver.maximize_window()
sleep(3)

s = SeleniumWrapper(driver)

s.click_element((By.LINK_TEXT, "Log in"))
s.enter_text((By.ID, "Email"), value="hello.world@company.com")
s.enter_text((By.ID, "Password"), value="Password123")
s.click_element((By.XPATH, "//input[@value='Log in']"))