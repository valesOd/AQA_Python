from selenium.webdriver.common.by import By
import allure
from page_object.BasePage import BasePage


class Login(BasePage):
    user_name = (By.ID, 'login-form-username')
    user_password = (By.ID, 'login-form-password')
    login = (By.ID, 'login')

    @allure.step
    def loginAs(self, login, passwd):
        self.go("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        self.fill_field(self.user_name, login)
        self.fill_field(self.user_password, passwd)
        self.click_button(self.login)
        self.wait_until_visible("Projects")

