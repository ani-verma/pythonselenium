from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium_wrapper import SeleniumWrapper
from config import Config

# def test_login(setup):
#     s = SeleniumWrapper(setup)
#     s.click_element((By.LINK_TEXT, "Log in"))
#     s.enter_text((By.ID, "Email"), value="hello.world@company.com")
#     s.enter_text((By.ID, "Password"), value="Password123")
#     s.click_element((By.XPATH, "//input[@value='Log in']"))

class TestSpam:
    def test_spam(self, hello):
        print("Executing spam")
    
    def test_2(self, hello):
        print("executing test_2")

class TestDemo:
    def test_demo(self, hello):
        print("Executing Demo")