import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Login_page import LoginPageFunc



@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    def test_ui_for_login_page(self):
        driver = self.driver
        ui = LoginPageFunc(driver)

        try :
            assert ui.get_logo() == "https://storage.cloud.google.com/trado_images/settings/value-2rnvbaw82gkimxzw8h?1607852736257"
            assert ui.phone_lable == "טלפון*"
            assert ui.button_phon == "//input[@value='שלח לי קוד']"

        except Exception as e:
            driver.get_screenshot_as_png()



