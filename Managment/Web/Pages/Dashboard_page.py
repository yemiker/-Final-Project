import allure
from Managment.Web.Locators.Dashboard_locators import DashboardLocators
from selenium.webdriver.common.by import By
from Managment.Web.Utils.utils import Utilitis
from time import sleep




class DashboardPageFunc():
    def __init__(self, driver):
        self.driver = driver
        self.finnens = DashboardLocators.finnens
        self.cupons_button = DashboardLocators.cupons_button
        self.orders = DashboardLocators.orders
        self.products = DashboardLocators.products
        self.sells = DashboardLocators.sells
        self.stores = DashboardLocators.stores
        self.users = DashboardLocators.users
        self.graf = DashboardLocators.graf
        self.allnav = DashboardLocators.allnav
        self.avg_sum = DashboardLocators.avg_sum
        self.order_sum = DashboardLocators.order_sum
        self.chart = DashboardLocators.chart


    @allure.step
    def click_cup(self):
        self.driver.find_element(By.XPATH,self.cupons_button).click()

    @allure.step
    def finnens_click(self):
        self.driver.find_element(By.XPATH,self.finnens).click()

    @allure.step
    def orders_click(self):
        self.driver.find_element(By.XPATH,self.orders).click()

    @allure.step
    def products_click(self):
        self.driver.find_element(By.XPATH,self.products).click()

    @allure.step
    def sells_click(self):
        self.driver.find_element(By.XPATH,self.sells).click()

    @allure.step
    def stores_click(self):
        self.driver.find_element(By.XPATH,self.stores).click()

    @allure.step
    def users_click(self):
        self.driver.find_element(By.XPATH,self.users).click()

    @allure.step
    def graf_display(self):
        self.driver.find_element(By.XPATH,self.graf).is_displayed()

    @allure.step
    def avrage(self):
        self.driver.find_element(By.XPATH,self.avg_sum).is_displayed()
        avg = self.driver.find_element(By.XPATH,self.avg_sum).text
        return avg

    @allure.step
    def order_(self):
        self.driver.find_element(By.XPATH, self.order_sum).is_displayed()
        sm = self.driver.find_element(By.XPATH, self.order_sum).text
        return sm

    @allure.step
    def chart_ui(self):
        self.driver.find_element(By.XPATH,self.chart).is_displayed()
        a = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(1)").text
        return a


    @allure.step
    def get_text(self,locator):
        text = self.driver.find_element(By.XPATH, locator).text
        return text







