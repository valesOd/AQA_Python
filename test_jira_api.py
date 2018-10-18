import pytest
import requests
import allure

from utils.tools import Tools
from random import randint
from utils.api import Api


@pytest.mark.parametrize("res,login,passwd", [
    (401, "Sergey_Valevskyi1", "Sergey_Valevskyi"),
    (401, "Sergey_Valevskyi", "Sergey_Valevskyi1"),
    (200, "Sergey_Valevskyi", "Sergey_Valevskyi"),
])
@allure.title('Test-Login-API')
def test_login(res, login, passwd):
    assert res == Api.login_api(login, passwd).status_code


@pytest.mark.parametrize("res,file_name", [
    (201, "create_issue.json"),
    (400, "create_issue_without_issue_type.json"),
    (400, "create_issue_with_too_long_summery.json"),
])
@allure.title('Test-Create-Issue-API')
def test_create_issue(res, file_name):
    assert res == Api.create_issue_api(file_name).status_code


@pytest.mark.parametrize("res,jql", [
    (1, 'project%20%3D%20AQAPYTHON%20AND%20key%20%3D%20AQAPYTHON-7928'),
    (0, 'project%20%3D%20AQAPYTHON%20AND%20text%20~%20"Seva test"'),
    (5, 'project%20%3D%20AQAPYTHON%20AND%20text%20~%20Serhii')
])
@allure.title('Test-Search-Issue-API')
def test_search_issue(res, jql):
    assert res == Api.search_issue_api(jql).json()['total']


@pytest.mark.parametrize("res,file_name,id", [
    (204, 'update_priority.json', 'AQAPYTHON-7932'),
    (204, 'update_issue_assignee.json', 'AQAPYTHON-7932'),
    (204, 'update_summery.json', 'AQAPYTHON-7932')
])
@allure.title('Test-Update-Issue-API')
def test_update_issue(res, file_name, id):
    assert res == Api.update_issue_api(file_name,id).status_code


@allure.title('Test-Login-API')
def test_random():
    assert randint(1, 2) == 2
