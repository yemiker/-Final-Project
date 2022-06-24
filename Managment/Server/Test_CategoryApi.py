import requests
import pytest
from Managment.Web.Utils.utils import Utilitis


class TestCategories():
    """test 1"""
    def test_add_new_category_to_my_store_corrctly(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/section/create"
        body = {"name": "שושן", "fields": {"name": "שושי", "kind": "text"}, "departmentIds": ["4jp555dl4grgcjw"]}

        response = requests.post(URL, data=body)
        util.assertFunc(response.status_code,200)


    """test 2"""
    def test__add_new_category_to_my_store_incorrectly_when_category_field_null(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/section/update"
        body = {"name": "שושי", "fields": {"name": "שושי", "kind": "text"}}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 3"""
    def test_add_a_new_category_to_my_store_incorrectly_when_type_field_null(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/section/update"
        body = {"name": "שושן", "fields": {"name": "שושי"}, "departmentIds": ["4jp555dl4grgcjw"]}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 4"""
    def test_add_new_category_to_my_store_incorrectly_when_second_name_field_null(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/section/update"
        body = {"name": "שושן", "fields": {"kind": "text"}, "departmentIds": ["4jp555dl4grgcjw"]}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)

    """test 5"""
    def test_add_new_category_to_my_store_incorrectly_when_category_is_exist_with_same_data(self):
        util = Utilitis(self)
        URL = "https://qa-api.trado.co.il/api/section/update"
        body = {"name": "שושן", "fields": {"name": "שושי", "kind": "text"}, "departmentIds": ["4jp555dl4grgcjw"]}

        response = requests.post(URL, data=body)
        x = response.json()
        status_response = x["status"]
        util.assertFunc(status_response, 400)






