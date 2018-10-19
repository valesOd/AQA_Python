from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import allure

from page_object.BasePage import BasePage


class Issue(BasePage):
    priority = (By.ID, 'priority-field')
    submit = (By.ID, 'edit-issue-submit')
    summary = (By.ID, 'summary')
    assignee = (By.ID, 'assignee-field')
    edit = (By.ID, 'edit-issue')
    url = "http://jira.hillel.it:8080/browse/"

    @allure.step
    def go(self, name):
        self.driver.get(self.url + name)
        self.wait_until_visible(name)

    # def fill_field_with_wait(self, field, text):
    #     self.wait.until(
    #         expected_conditions.visibility_of_element_located(field))
    #     element = self.driver.find_element(field[0], field[1])
    #     element.click()
    #     element.clear()
    #     element.send_keys(text)
