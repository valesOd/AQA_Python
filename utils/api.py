import requests
from .variable import *
from .tools import Tools


class Api:

    @staticmethod
    def login_api(login, passwd):
        return requests.get(auth_url + 'issue/XH-144', auth=(login, passwd))


    @staticmethod
    def create_issue_api(file_name):
        return requests.request("POST", auth_url + 'issue/', data=Tools.read_file(file_name),
                                headers=auth_headers)


    @staticmethod
    def search_issue_api(search_jql):
        return requests.request("GET", auth_url + 'search?jql=' + search_jql, auth=(auth_user, auth_passwd))


    @staticmethod
    def update_issue_api(file_name, issue_id):
        return requests.request("PUT", auth_url + 'issue/' + issue_id, data=Tools.read_file(file_name),
                                headers=auth_headers)
