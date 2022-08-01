from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
driver = Chrome("./chromedriver.exe")


driver.get("https://www.myntra.com/")
sleep(5)
driver.maximize_window()

actions = ActionChains(driver)
profile=driver.find_element_by_xpath("//span[text()='Profile']")
actions.move_to_element(profile).perform()
sleep(1)
driver.find_element_by_xpath("//a[text()='login / Signup']").click()
