import requests
import pytest
from Managment.Web.Utils.utils import Utilitis

class TestLogin():
    """test 1"""
    def test_valid_login_when_user_exist_in_system(self):
        util = Utilitis(self)
        URL = " https://qa-api.trado.co.il/api/admin-user/login"
        body = {"phone": "1950000000", "code": "1234"}
        response = requests.post(URL, data=body)
        util.assertFunc(response.status_code,200)

    "test 2"
    def test_invalid_login_when_user_isnt_exist_in_system(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/admin-user/logincode"
        body = {"{phone": "1234577777"}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 3"""
    def test_invalid_login_when_phone_field_null(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/admin-user/logincode"
        body = { }

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 4"""
    def test_invalid_login_when_phone_field_less_than_10_num(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/admin-user/logincode"
        body = {"{phone": "1234"}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 5"""
    def test_invalid_login_when_code_is_isnt_match(self):
        util = Utilitis(self)
        URL = " https://qa-api.trado.co.il/api/admin-user/login"
        body = {"phone": "1950000000", "code": "0000"}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 6"""
    def test_invalid_login_when_code_null(self):
        util = Utilitis(self)
        URL = " https://qa-api.trado.co.il/api/admin-user/login"
        body = {"phone": "1950000000", "code": ""}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)







