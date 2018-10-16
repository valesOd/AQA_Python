from selenium import webdriver
import unittest
import pytest
from selenium.webdriver.common.by import By

from page_object.Issue import Issue
from page_object.Search import Search
from page_object.BasePage import BasePage
from page_object.Login import Login
from page_object.Main import Main

from page_object.CreateIssue import CreateIssue


class TestUI:

    @pytest.mark.parametrize("res,login,passwd", [
        (
                'Sorry, your username and password are incorrect - please try again.', "Sergey_Valevskyi1",
                "Sergey_Valevskyi"),
        (
        'Sorry, your username and password are incorrect - please try again.', "Sergey_Valevskyi", "Sergey_Valevskyi1"),
        ('Projects', "Sergey_Valevskyi", "Sergey_Valevskyi"),
    ])
    def test_login(self, res, login, passwd):
        login_page = Login()
        login_page.go("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        login_page.fill_field(Login.user_name, login)
        login_page.fill_field(Login.user_password, passwd)
        login_page.click_button(Login.login)

        assert res in login_page.wait_until_visible(res)

    @pytest.mark.parametrize("res,summary", [
        ('has been successfully created.', "Seva new issue UI"),
        ('Summary must be less than 255 characters.',
         "Serhii new issue with too long summery.Serhii new issue with too long summery.Serhii new issue with too long summery.Serhii new issue with too long summery.Serhii new issue with too long summery.Serhii new issue with too long summery.Serhii new issue with too long summery.Serhii new issue with too long summery."),
        ('You must specify a summary of the issue.', ""),
    ])
    def test_create_issue(self, res, summary):
        base_page = BasePage()
        login_page = Login()
        login_page.loginAs("Sergey_Valevskyi", "Sergey_Valevskyi")
        base_page.click_button(Main.create_issue)
        base_page.fill_field(CreateIssue.summary, summary)
        base_page.click_button(CreateIssue.create_issue_submit)
        assert res in base_page.wait_until_visible(res)

    @pytest.mark.parametrize("res, name", [
        ('5', "Serhii"),
        ('0', "Seva test"),
        ('1', "Summary after update"),
    ])
    def test_search_issue(self, res, name):
        base_page = BasePage()
        login_page = Login()
        login_page.loginAs("Sergey_Valevskyi", "Sergey_Valevskyi")
        base_page.go(Search.url)
        base_page.fill_field(Search.searcher_query_field, name)
        base_page.click_button(Search.searcher_issue_button)
        assert res == base_page.wait_equal_value(Search.count_of_issue, res)

    @pytest.mark.parametrize(" name, field, value", [
        ("AQAPYTHON-7928", Issue.priority, "High"),
        ("AQAPYTHON-7928", Issue.summary, "New summary"),
        ("AQAPYTHON-7928", Issue.assignee, "Sergey_Valevskyi"),
    ])
    def test_update_issue(self, name, field, value):
        res = "has been updated."
        base_page = BasePage()
        login_page = Login()
        login_page.loginAs("Sergey_Valevskyi", "Sergey_Valevskyi")
        issue_page = Issue()
        issue_page.go(name)
        base_page.click_button(issue_page.edit)
        base_page.fill_field(field, value)
        base_page.click_button(issue_page.submit)
        assert res in base_page.wait_until_visible(res)
