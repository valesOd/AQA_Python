import pytest
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium import webdriver


class BasePage(object):

    def __init__(self):
        import utils.variable
        self.driver = utils.variable.global_web_driver
        self.wait = WebDriverWait(self.driver, 180)

    def click_button(self, button):
        self.wait.until(
            expected_conditions.visibility_of_element_located(button))
        element = self.driver.find_element(button[0], button[1])
        element.click()

    def fill_field(self, field, text):
        self.wait.until(
            expected_conditions.visibility_of_element_located(field))
        element = self.driver.find_element(field[0], field[1])
        element.click()
        element.clear()
        element.send_keys(text)

    def wait_until_visible(self, text):
        return self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + text + "')]"))).text

    def wait_equal_value(self, field, value):
        count = "0"
        try:
            self.wait.until(expected_conditions.text_to_be_present_in_element(field, value))
            count = self.driver.find_element(field[0], field[1]).text
        except TimeoutException:
            count = "0"
        finally:
            return count

    def go(self, text):
        self.driver.get(text)
