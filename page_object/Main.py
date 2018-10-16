import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.BasePage import BasePage


class Main(BasePage):
    create_issue = (By.ID, 'create_link')




