import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.BasePage import BasePage


class CreateIssue(BasePage):
    summary = (By.ID, 'summary')
    create_issue_submit = (By.ID, 'create-issue-submit')

