import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from Managment.Web.Pages.Login_page import LoginPageFunc

class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://qa-admin.trado.co.il/#/login")
        self.driver.maximize_window()

        yield self.driver

        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()

    @pytest.fixture
    def connect_home_page(self):
        driver = self.driver
        login = LoginPageFunc(driver)
        login.enter_phone('1950000000')
        self.driver.implicitly_wait(10)
        login.click_on_button()
        self.driver.implicitly_wait(10)
        login.enter_phone_code('1234')
        login.click_on_button_login()
        yield self.driver