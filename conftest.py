import pytest
from selenium import webdriver
from utils.variable import global_web_driver as driver


@pytest.fixture(scope="function", autouse=True)
def my_fixture(request):
    import utils.variable
    if driver is None:
        utils.variable.global_web_driver = __driver_init()
    request.cls.driver = driver
    yield
    utils.variable.global_web_driver.close()


def __driver_init():
    return webdriver.Chrome("./utils/chromedriver.exe")
