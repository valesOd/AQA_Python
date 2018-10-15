from selenium import webdriver
import unittest
import pytest
import allure
from selenium.webdriver.common.by import By

from page_object.Issue import Issue
from page_object.Search import Search
from page_object.BasePage import BasePage
from page_object.Login import Login
from page_object.Main import Main

from page_object.CreateIssue import CreateIssue


class TestUI:

    @pytest.mark.parametrize("res, name", [
        ('1', "Summary after update"),
    ])
    @allure.title('Test-Search-Issue')
    def test_search_issue(self, res, name):
        base_page = BasePage()
        login_page = Login()
        login_page.loginAs("Sergey_Valevskyi", "Sergey_Valevskyi")
        base_page.go(Search.url)
        base_page.fill_field(Search.searcher_query_field, name)
        base_page.click_button(Search.searcher_issue_button)
        assert res == base_page.wait_equal_value(Search.count_of_issue, res)
