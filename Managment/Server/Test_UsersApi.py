import pytest
import requests
from Managment.Web.Base.BasePage import Base
from Managment.DB.BaseMongoDB2 import MongoDB
db = MongoDB("trado_qa", "users")
from Managment.Web.Utils.utils import Utilitis

class TestApi():

    def test_api_addUsers(self):
        url = 'https://qa-api.trado.co.il/api/user/create'
        myobj = {"firstName":"sbchjh",
                 "lastName":"ss",
                 "email":"d@jS.com",
                 "phone":Utilitis(self).random_with_N_digits(10),
                 "storeIds":["4jp555dl46qzoyz"]
                 }
        res = requests.post(url, json=myobj)
        status = res.json()
        rsults = status['status']
        assert rsults == 200


    def test_api_addUsers_invalid_email(self):
        url = 'https://qa-api.trado.co.il/api/user/create'
        myobj = {"firstName":"sbchjh",
                 "lastName":"avi",
                 "email":"d@j",
                 "phone":Utilitis(self).random_with_N_digits(10),
                 "storeIds":["4jp555dl46qzoyz"]
                 }
        res = requests.post(url, json=myobj)
        status = res.json()
        result = status['message']
        assert result == "not unique"


    def test_api_addUsers_invalid_storeID(self):
        url = 'https://qa-api.trado.co.il/api/user/create'
        myobj = {"firstName":"sbchjh",
                 "lastName":"bs",
                 "email":"d@jd.com",
                 "phone":Utilitis(self).random_with_N_digits(10),
                 }
        res = requests.post(url, json=myobj)
        status = res.json()
        print(status)
        x = status['message']
        assert x == "not unique"



    def test_api_updateUsers(self):
        url = 'https://qa-api.trado.co.il/api/user/update'
        myobj = {"firstName":"assad",
                 "lastName":"ss",
                 "email":"d@j.com",
                 "phone":Utilitis(self).random_with_N_digits(10)
                 }
        x = requests.post(url, json=myobj)
        print(x.text)
        assert x.status_code == 200