import pytest
import requests
from Managment.DB.BaseMongoDB2 import MongoDB
db = MongoDB("trado_qa", "products")

class TestProductAPI():


    """test 1 """
    def test_api_create_prodact_correctly(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"001995","name":"air-pods","price":500,
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m","parallelImporter":'true',
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 20
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"name":"air-pods"})
        db_result = product_in_db["price"]
        myobj_result = myobj["price"]
        assert myobj_result == db_result

    """test 2"""
    def test_api_create_prodact_incorrectly_when_prodact_name_null(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"001927","price":500,"name":"",
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m","parallelImporter":'true',
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"barcode":"001927"})
        expected_result = None

        assert expected_result == product_in_db

    """test 3 """
    def test_api_create_prodact_incorrectly_when_prodact_barcode_null(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"","price":500,"name":"test_barcode_null",
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m","parallelImporter":'true',
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"name":"test_barcode_null"})

        expected_result = None

        assert expected_result == product_in_db

    """test 4"""
    def test_api_create_prodact_incorrectly_when_prodact_price_null(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"","price":"","name":"test_price_null",
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m","parallelImporter":'true',
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        result = response.json()
        """assert with DB"""
        product_in_db = db.find({"name":"test_price_null"})
        expected_result = None

        assert expected_result == product_in_db

    """test 5"""

    @pytest.mark.skip
    def test_api_create_prodact_incorrectly_when_prodact_category_null(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"756756765","price":54,"name":"test_category_null",
          "active":True,"expirationDate":"2022-06-22",
          "description":"change desc","priority":2,
          "parallelImporter":'true',"sectionId": "",
          "departmentId": "xfdpjewkz59964t", "storeId": "2p8ys40kl0eyvk1m",
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        result = response.json()
        """assert with DB"""
        product_in_db = db.find({"name":"test_category_null3"})

        expected_result = None

        assert expected_result == product_in_db

    """test 6 """
    def test_api_create_prodact_incorrectly_when_prodact_store_null(self):
        url = "https://qa-api.trado.co.il/api/product/create"

        myobj = {"barcode":"756756765","price":54,"name":"test_store_null",
          "active":"true","expirationDate":"2022-06-22",
          "description":"change desc","priority":2,
          "parallelImporter":'true',"sectionId": "u6z3rgrckkzoqiay",
    "departmentId": "xfdpjewkz59964t", "storeId": "",
          "units":{"unitsInCarton":"1","amount":"100","minimumOrderCartonsCount":"1"},
          "deliveryOrderPlace":{"city":"eilt","street":"sumsum","number":"2"},
          "contactInfo":{"contactNumber":"0556622111"},"fields":{}}

        response = requests.post(url, json=myobj)
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"name":"test_store_null"})
        expected_result = None

        assert expected_result == product_in_db

    """test 7 """
    def test_api_update_prodact_actice_status_correctly(self):
        status = True
        url = "https://qa-api.trado.co.il/api/product/update"
        myobj = {"barcode":"001994",
                 "name":"Charger",
                 "price":555,
                 "active":status,
                 "expirationDate":"2022-06-22T00:00:00.000Z",
                 "description":"52 inches",
                 "priority":1,"parallelImporter":False,"sectionId":"u6z3rgrckkzoqiay",
          "departmentId":"xfdpjewkz59964t","storeId":"2p8ys40kl0eyvk1m",
                 "units":{"unitsInCarton":"100","amount":"20","minimumOrderCartonsCount":"10"},
                 "deliveryOrderPlace":{"city":"lod","street":"tech","number":"100"},
                 "contactInfo":{"contactNumber":"0542259745"},
                 "id":"4jp555dl4kbaw8h","fields":{}
                 }

        response = requests.post(url, json=myobj)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 20
        result = response.json()

        """assert with DB"""
        product_in_db = db.find({"name": "Charger"})
        db_result = product_in_db["active"]

        assert db_result == status






