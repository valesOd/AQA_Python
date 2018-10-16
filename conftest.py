import pytest
import os
from selenium import webdriver

try:
    from utils.variable import global_web_driver as driver
except ImportError:
    from .utils.variable import global_web_driver as driver


@pytest.fixture(scope="function", autouse=True)
def my_fixture(request):
    import utils.variable
    if driver is None:
        utils.variable.global_web_driver = __driver_init()
    request.cls.driver = driver
    yield
    utils.variable.global_web_driver.close()


def __driver_init():
    if os.name == 'nt':
        web_driver = webdriver.Chrome("./utils/chromedriver.exe")
    else:
        web_driver = webdriver.Chrome("./utils/chromedriver")
    return web_driver
