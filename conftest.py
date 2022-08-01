from time import sleep
from selenium.webdriver import Chrome
from config import Config
from pytest import fixture

@fixture(scope="function")
def setup():
    print("Running Setup")
    driver = Chrome(Config.DRIVER_PATH)
    print(driver)
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(3)
    yield driver
    print("Closing Browser")
    driver.close()

@fixture(scope="class")
def hello():
    print("hello world")
    yield "hi there"
    print("Bye world")