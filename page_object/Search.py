import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.BasePage import BasePage


class Search(BasePage):
    count_of_issue = (By.CSS_SELECTOR, '.results-count-total')
    searcher_query_field = (By.ID, 'searcher-query')
    searcher_issue_button = (By.CSS_SELECTOR, 'button[original-title="Search for issues"]')
    url = "http://jira.hillel.it:8080/issues/?jql=text%20~%20\"emptypage\""
