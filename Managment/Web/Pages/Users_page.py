from telnetlib import EC

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Managment.Web.Locators.Users_locators import UsersLocators
from selenium.webdriver.common.by import By
from Managment.Web.Utils.utils import Utilitis
from time import sleep




class Userspagefunc():
    def __init__(self, driver):
        self.driver = driver
        self.user_nav_btn = UsersLocators.user_nav_btn
        self.name = UsersLocators.name
        self.lastname = UsersLocators.lastname
        self.emil = UsersLocators.emil
        self.phone = UsersLocators.phone
        self.store = UsersLocators.store
        self.store_ops = UsersLocators.store_ops
        self.pick = UsersLocators.pick
        self.btnadd = UsersLocators.btnadd
        self.varify = UsersLocators.varify
        self.update = UsersLocators.update
        self.updt_btn = UsersLocators.updt_btn
        self.head = UsersLocators.head
        self.store_list = UsersLocators.store_list
        self.search_field = UsersLocators.search_field

    @allure.step
    def userpage_btn(self):
        self.driver.find_element(By.XPATH, self.user_nav_btn).click()

    @allure.step
    def addname(self,name):
        self.driver.find_element(By.XPATH,self.name).clear()
        self.driver.find_element(By.XPATH,self.name).click()
        self.driver.find_element(By.XPATH,self.name).send_keys(name)

    @allure.step
    def addlastname(self,lastname):
        self.driver.find_element(By.XPATH,self.lastname).clear()
        self.driver.find_element(By.XPATH,self.lastname).click()
        self.driver.find_element(By.XPATH,self.lastname).send_keys(lastname)

    @allure.step
    def addemil(self,emil):
        self.driver.find_element(By.XPATH,self.emil).clear()
        self.driver.find_element(By.XPATH,self.emil).click()
        self.driver.find_element(By.XPATH,self.emil).send_keys(emil)

    @allure.step
    def addphone(self,phone):
        self.driver.find_element(By.XPATH,self.phone).clear()
        self.driver.find_element(By.XPATH,self.phone).click()
        self.driver.find_element(By.XPATH,self.phone).send_keys(phone)

    @allure.step
    def store_option(self, op):
        self.driver.find_element(By.XPATH, self.store).click()

        options = self.driver.find_element(By.XPATH, self.store_ops.format(op))
        options.click()

    @allure.step
    def store_option_click(self):
        self.driver.find_element(By.XPATH, self.store).click()

    @allure.step
    def add_btn(self):
        self.driver.find_element(By.XPATH,self.btnadd).click()

    @allure.step
    def get_text1(self,locator,x):
        text = self.driver.find_element(By.XPATH, locator.format(x)).text
        return text

    @allure.step
    def update_click(self):
        self.driver.find_element(By.XPATH,self.update).click()
        # win = self.driver.find_element(By.CSS_SELECTOR,self.head).text
        # assert win == "משתמש"

    @allure.step
    def update_btn(self):
        self.driver.find_element(By.CSS_SELECTOR,self.updt_btn).click()


    def displayedElement(self,loctor):
        element = self.driver.find_element(By.CSS_SELECTOR,loctor)
        if element.is_displayed():
            return ("Element found")
        else:
            return ("Element not found")


    def search_box(self,name):
        self.name = name

        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.search_field)))

        search.send_keys(self.name)
        search.send_keys(Keys.RETURN)


    def fillInputfileds(self,name,phone):
        lastName = Utilitis.randomString(self)
        em = Utilitis.randomString2letters()
        self.driver.find_element(By.XPATH, self.name).clear()
        self.driver.find_element(By.XPATH, self.name).click()
        self.driver.find_element(By.XPATH, self.name).send_keys(name)
        self.driver.find_element(By.XPATH, self.lastname).clear()
        self.driver.find_element(By.XPATH, self.lastname).click()
        self.driver.find_element(By.XPATH, self.lastname).send_keys(lastName)
        self.driver.find_element(By.XPATH, self.emil).clear()
        self.driver.find_element(By.XPATH, self.emil).click()
        self.driver.find_element(By.XPATH, self.emil).send_keys(em + "@jd.com")
        self.driver.find_element(By.XPATH, self.phone).clear()
        self.driver.find_element(By.XPATH, self.phone).click()
        self.driver.find_element(By.XPATH, self.phone).send_keys(phone)
        self.driver.find_element(By.XPATH, self.store).click()
        options = self.driver.find_element(By.XPATH, self.store_ops.format("dddd"))
        options.click()

