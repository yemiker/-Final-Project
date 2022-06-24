import pytest
from appium import webdriver



class Connection:

    @pytest.fixture(autouse=True)
    def set_up_mobile(self):
        print("Initiating Chrome driver")
        desired_cap = {
            "deviceName": "Galaxy A03 Core",
            # "udid": "192.168.4.17:5555",
            "udid": "R7ST10H384H",
            "platformName": "Android",
            "platformVersion": "11",
            "browserName": "Chrome"

        }

        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723/wd/hub",
            desired_capabilities=desired_cap
        )

        self.driver.get("https://qa-admin.trado.co.il")

        print("Application Started....")

        yield self.driver

        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()