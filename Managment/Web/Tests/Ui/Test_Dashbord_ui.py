import time
import allure
import pytest
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Dashboard_page import DashboardPageFunc
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from Managment.Web.Utils.utils import Utilitis

@pytest.mark.usefixtures('connect_home_page')
class TestDashboardUI(Base):

    @pytest.mark.sanity
    def test_ui(self):
        driver = self.driver
        dash = DashboardPageFunc(driver)
        util = Utilitis(driver)
        dash.graf_display()
        sum = dash.avrage()
        util.assertFunc(sum ,'₪8835.04')
        ord = dash.order_()
        util.assertFunc(ord ,"10")
        chr = dash.chart_ui()
        util.assertFunc(chr ,"492")

    def test_ui_navbar(self):
        driver = self.driver
        util = Utilitis(driver)
        div = driver.find_element(By.CSS_SELECTOR ,'div[class="dashboard_counts"]')
        ls_a = div.find_elements(By.TAG_NAME ,'a')
        actuals = [[] ,[]]
        expecteds = [['קופונים', 'Finances', 'הזמנות', 'מוצרים', 'מבצעים', 'חנויות', 'משתמשים', 'Finances']
                     ,['7', '1', '328', '203', '21', '59', '220', '2']]
        for i in ls_a:
            title = i.find_element(By.CSS_SELECTOR,'span[class="dashboard_title"]').text
            num = i.find_element(By.CSS_SELECTOR ,'span[class="dashboard_countNumber"]').text
            actuals[0].append(title)
            actuals[1].append(num)
        for enum ,etitle ,anum ,atitle in zip(expecteds[1] ,expecteds[0] ,actuals[1] ,actuals[0]):
            util.assertFunc(enum ,anum)
            util.assertFunc(etitle ,atitle)