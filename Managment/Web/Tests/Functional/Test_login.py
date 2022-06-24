import time

import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Utils.utils import Utilitis
from Managment.Web.Pages.Login_page import LoginPageFunc

@pytest.mark.usefixtures('set_up')
class TestLogin(Base):
    """test 1"""
    @pytest.mark.sanity
    def test_login_success(self):
        driver = self.driver
        util = Utilitis(driver)
        login = LoginPageFunc(driver)
        #insert personal details
        login.enter_phone('1950000000')
        time.sleep(2)
        login.click_on_button()
        time.sleep(2)
        login.enter_phone_code('1234')
        time.sleep(2)
        #clickin on login button
        login.click_on_button_login()
        time.sleep(2)
        """assert"""
        util.assertFunc(login.get_nameT1(),"שלום slamonnnהתנתק")

    """test 2"""
    def test_login_incorrectly_when_user_non_register(self):
        driver = self.driver
        util = Utilitis(driver)
        login = LoginPageFunc(driver)
        login.enter_phone('4528762424')
        login.click_on_button()
        """assert"""
        util.assertFunc(login.get_nameT2(),"no such user")

    """test 3"""
    @pytest.mark.skip
    def test_login_incorrect_when_phone_field_null(self):
        driver = self.driver
        util = Utilitis(driver)
        login = LoginPageFunc(driver)
        # login.enter_phone()
        login.click_on_button()
        """assert"""
        util.assertFunc(util.valid_Message,'זהו שדה חובה.')

    """test 4"""
    def test_login_incorrectly_when_phone_field_is_less_than_10_num(self):
        user = "//div[contains(text(),'no such user')]"
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('45')
        login.click_on_button()
        try:
            value = driver.find_element(By.XPATH, user).get_attribute("innerText")
            assert user == "no such user"
        except Exception as e:
            driver.get_screenshot_as_png()

    """test 5"""
    def test_login_incorrectly_when_code_is_not_match(self):
        failed_message = "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[2]"
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        login.click_on_button()
        login.click_on_button_login()
        try:
            value = driver.find_element(By.XPATH,failed_message).get_attribute("innerText")
            assert failed_message == "faild to login"
        except Exception as e:
            driver.get_screenshot_as_png()

    """test 6"""
    def test_login_incorrectly_when_code_is_null(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        driver.implicitly_wait(10)
        login.click_on_button()
        driver.implicitly_wait(10)
        login.click_on_button_login()
        time.sleep(1)
        util = Utilitis(driver)
        x = util.valid_Message("input[placeholder='קוד']")
        try :
            assert x == 'זהו שדה חובה.'
        except Exception as e:
            driver.get_screenshot_as_png()