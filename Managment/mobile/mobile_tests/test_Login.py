import time

import pytest
from Managment.mobile.MobileLoginPage.Mobile_login_page import MobileLoginPageFunc
from Managment.mobile.Connection.Connection import Connection
from Managment.DB.BaseMongoDB2 import MongoDB

db = MongoDB("trado_qa","adminusers")

@pytest.mark.usefixtures('set_up_mobile')
class TestLogin(Connection):
    """test 1"""

    def test_login_success(self):
        driver = self.driver
        mobile = MobileLoginPageFunc(driver)
        mobile.enter_phone('1950000000')
        time.sleep(1)
        mobile.click_on_button()
        time.sleep(1)
        mobile.enter_phone_code("1234")
        time.sleep(1)
        mobile.click_on_button_login()
        title = driver.title
        assert title == "- trado"


    """test 2 """

    def test_login_success_with_code(self):
        driver = self.driver

        mobile = MobileLoginPageFunc(driver)
        mobile.enter_phone('0556622938')
        time.sleep(1)
        mobile.click_on_button()
        time.sleep(5)
        sms = db.find({"phone": "0556622938"})["loginCode"]
        mobile.enter_phone_code(f"{sms}")
        time.sleep(1)
        mobile.click_on_button_login()
        time.sleep(2)
        mobile.click_trado_store()
        title = driver.title
        assert title == "דשבורד - trado"


    """test 3 """

    def test_login_unsuccessfully_with_wrong_code(self):
        driver = self.driver
        print(driver.title)
        mobile = MobileLoginPageFunc(driver)
        mobile.enter_phone('1950000000')
        time.sleep(1)
        mobile.click_on_button()
        time.sleep(1)
        mobile.enter_phone_code("4321")
        time.sleep(1)
        mobile.click_on_button_login()
        value = driver.title
        assert value == '- trado'








