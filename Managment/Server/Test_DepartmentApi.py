import random
import requests

url_create = "https://qa-api.trado.co.il/api/department/create"
url_filter = "https://qa-api.trado.co.il/api/department/filter"
url_update = "https://qa-api.trado.co.il/api/department/update"


class Test_Department_Api():
    def test_Adding_a_department_success_in_active_mode(self):
        # Define a variable for a random directory
        i = random.random()
        print(round(i,2))
        # A random name is created each time
        body = {"name": f"sofa{round(i, 2)}", "active": "true"}
        # get request payload
        response = requests.post(url_create, json=body)
        payload = response.json()
        result = payload["payload"]
        print(result)
        assert response.status_code == 200
        assert result["name"] == f"sofa{round(i, 2)}"
        assert result["active"] == True
        assert result["createdAtExists"] == 1


    def test_Adding_a_department_success_in_inactive_mode(self):
        # Define a variable for a random directory
        i = random.random()
        print(round(i, 2))
        # A random name is created each time
        body = {"name": f"sofa{round(i, 2)}", "active": "false"}
        # get request payload
        response = requests.post(url_create, json=body)
        print(response.json())
        payload = response.json()
        result = payload["payload"]
        print(result)
        assert response.status_code == 200
        assert result["name"] == f"sofa{round(i, 2)}"
        assert result["active"] == False
        assert result["createdAtExists"] == 1


    def test_Adding_a_department_incorrectly_when_name_field_is_null_in_active_mode(self):
        body = {"active": "true"}
        # get request payload
        response = requests.post(url_create, json=body)
        print(response.json())
        assert response.status_code == 400


    def test_Adding_a_department_incorrectly_when_name_field_is_exists(self):
        body = {"name": "וודקה", "active": "true"}
        response = requests.post(url_create, json=body)
        print(response.json())
        assert response.json()["message"] == 'not unique'
        assert response.json()["status"] == 400


    def test_search_a_department_correctly(self):
        body = {'search': "סבון"}
        response = requests.post(url_filter, json=body)
        print(response.json())
        payload = response.json()
        data = payload["payload"]
        result = data["data"]
        body = result[0]
        assert response.status_code == 200
        assert body['name'] == 'סבון'


    def test_search_a_department_incorrectly_When_the_product_does_not_exist(self):
        i = random.random()
        body = {"search": f"wowo{round(i,2)}"}
        response = requests.post(url_filter, json=body)
        payload = response.json()
        result = payload["payload"]
        print(result)
        assert response.status_code == 200
        assert result['count'] == 0

    def test_Update_a_department_correctly(self):
        # name': "מטענים", 'active': 'false', 'id': "4jp555dl4grc8zw
        body = {'name': "מטענים1", 'active': 'true', 'id': "4jp555dl4grc8zw1"}
        response = requests.post(url_update, json=body)
        print(response.json())
        result = response.json()["payload"]
        assert response.status_code == 200
        assert result["name"] == "מטענים1"
        assert result["active"] == True
        assert result["id"] == "4jp555dl4grc8zw1"






