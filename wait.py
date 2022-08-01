from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
def _wait(func):
    def wrapper(*args, **kwargs):
        # 1. Check if the element is loaded in the DOM
        # 2. Check if the element is visible on the webpage.
        # 3. Check if the element is enabled or not?
        locator = args[0]       # args = (("link text", "Register"),)
        w = WebDriverWait(driver, 20)
        v = visibility_of_element_located(locator)
        w.until(v, message="Progress bar was not loaded even after 20 seconds")
        # Original func gets executed (click_element, enter_text, select_item)
        return func(*args, **kwargs)
    return wrapper