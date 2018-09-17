import pytest
import requests

from tools import Tools

auth_user = 'Sergey_Valevskyi'
auth_passwd = 'Sergey_Valevskyi'
auth_url = "http://jira.hillel.it:8080/rest/api/2/"
auth_headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic U2VyZ2V5X1ZhbGV2c2t5aTpTZXJnZXlfVmFsZXZza3lp"
}

@pytest.mark.parametrize("res,login,passwd", [
    (401, "Sergey_Valevskyi1", "Sergey_Valevskyi"),
    (401, "Sergey_Valevskyi", "Sergey_Valevskyi1"),
    (200, "Sergey_Valevskyi", "Sergey_Valevskyi"),
])
def test_login(res, login, passwd):
    assert res == requests.get(auth_url + 'issue/XH-144', auth=(login, passwd)).status_code


@pytest.mark.parametrize("res,file_name", [
    (201, "create_issue.json"),
    (400, "create_issue_without_issue_type.json"),
    (400, "create_issue_with_too_long_summery.json"),
])
def test_create_issue(res, file_name):
    assert res == requests.request("POST", auth_url + 'issue/', data=Tools.read_file(file_name),
                                   headers=auth_headers).status_code


@pytest.mark.parametrize("res,jql", [
    (1, 'project%20%3D%20AQAPYTHON%20AND%20key%20%3D%20AQAPYTHON-7928'),
    (0, 'project%20%3D%20AQAPYTHON%20AND%20text%20~%20"Seva test"'),
    (5, 'project%20%3D%20AQAPYTHON%20AND%20text%20~%20Serhii')
])
def test_find_issue(res, jql):
    assert res == requests.request("GET", auth_url + 'search?jql=' + jql,
                                   auth=(auth_user, auth_passwd)).json()['total']

@pytest.mark.parametrize("res,file_name,id", [
     (204, 'update_priority.json', 'AQAPYTHON-7932'),
     (204, 'update_description.json', 'AQAPYTHON-7932'),
     (204, 'update_summery.json', 'AQAPYTHON-7932')
])
def test_update_issue(res, file_name, id):
    assert res == requests.request("PUT", auth_url + 'issue/' + id, data=Tools.read_file(file_name),
                                   headers=auth_headers).status_code
