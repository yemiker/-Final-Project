import time
import allure
import pytest
import requests
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Dashboard_page import DashboardPageFunc
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Managment.DB.BaseMongoDB2 import MongoDB




@pytest.mark.usefixtures('connect_home_page')
class TestDashboard(Base):


    def test_navbar_btn(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        txt = ['קופונים', 'Finances', 'הזמנות', 'מוצרים', 'מבצעים', 'חנויות', 'משתמשים', 'Finances']
        util = Utilitis(driver)
        for i in range(1,8):
            if i == 2 :
                continue
            driver.find_element(By.XPATH,f"(//a[contains(@class,'dashboard_count')])[{i}]").click()
            time.sleep(2)
            header = util.get_text(DashboardLocators.text)
            util.assertFunc(header,txt[i-1])
            driver.back()
            time.sleep(2)

    def test_product_number(self):
        first_num = self.driver.find_element(By.CSS_SELECTOR,DashboardLocators.prodct_num).get_attribute("innerText")
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
        self.driver.refresh()
        sec_num = self.driver.find_element(By.CSS_SELECTOR,DashboardLocators.prodct_num).get_attribute("innerText")
        assert int(first_num) == int(sec_num)-1



    def test_Users_number(self):
        driver = self.driver
        util = Utilitis(driver)
        num1 = driver.find_element(By.CSS_SELECTOR,DashboardLocators.users_num).get_attribute("innerText")
        url = 'https://qa-api.trado.co.il/api/user/create'
        myobj = {"firstName": "sbchjh",
                 "lastName": "ss",
                 "email": "j@j.com",
                 "phone": util.random_with_N_digits(10),
                 "storeIds": ["4jp555dl46qzoyz"]
                 }
        res = requests.post(url, json=myobj)
        assert res.status_code == 200
        driver.refresh()
        num2 = driver.find_element(By.CSS_SELECTOR,DashboardLocators.users_num).get_attribute("innerText")
        util.assertFunc(int(num1),int(num2)-1)











