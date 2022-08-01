from selenium import webdriver
from time import sleep
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)
class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)   # initlising parent class constructor

    # over-riding __call__ method of parent class
    def __call__(self, driver):
        print("Calling __call__ method of Child Class")
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            # Extra functionality that you are adding in child class
            # checking for enablement of the element
            return result.is_enabled()
        else:
            return False

# w = WebDriverWait(driver, 20)
 #v = _visibility_of_element_located(("xpath", "//div[text()='100%']"))
 #w.until(v, message="Progress bar was not loaded even after 20 seconds")
# print("DONE!")

def _wait(func):
    def wrapper(*args, **kwargs):
        # 1. Check if the element is loaded in the DOM
        # 2. Check if the element is visible on the webpage.
        # 3. Check if the element is enabled or not?
        instance = args[0]       # args = (("link text", "Register"),)
        locator = args[1]
        w = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        w.until(v, message="Progress bar was not loaded even after 20 seconds")
        # Original func gets executed (click_element, enter_text, select_item)
        return func(*args, **kwargs)
    return wrapper
class SeleniumWrapper: 
    def __init__ (self,driver):
        self.driver = driver
          

    @_wait      # click_element = _wait(click_element)
    def click_element(self,locator):
        self.driver.find_element(*locator).click()       # find_element("id", "fname")

    @_wait  # enter_text = _wait(enter_wait)
    def enter_text(self,locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

@_wait  # select_item = _wait(select_item)
def select_item(locator, *, item):
    element = self.driver.find_element(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise Exception

s = SeleniumWrapper(driver)       

s.click_element((By.LINK_TEXT, "Register"))
s.click_element((By.ID, "gender-male"))
s.enter_text((By.NAME, "FirstName"), value="hello")
s.enter_text((By.XPATH, "//input[@name='LastName']"), value="world")
s.enter_text((By.CSS_SELECTOR, "input[name='Email']"), value="hello.world@company.com")
s.enter_text((By.ID, "Password"), value="Password123")
s.enter_text((By.ID, "ConfirmPassword"), value="Password123")
s.click_element((By.ID, "register-button"))
driver.close()