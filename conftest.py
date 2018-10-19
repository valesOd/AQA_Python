import pytest
import os
import allure
from selenium import webdriver

try:
    from utils.variable import global_web_driver as driver
except ImportError:
    from .utils.variable import global_web_driver as driver


@pytest.fixture(scope="function")
def get_driver(request):
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    import utils.variable
    sr_driver = utils.variable.global_web_driver
    if rep.when == 'call' and rep.failed and sr_driver is not None:
        allure.attach(sr_driver.get_screenshot_as_png(),
                      name=item.name,
                      attachment_type=allure.attachment_type.PNG)
