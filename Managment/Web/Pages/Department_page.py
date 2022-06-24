from Managment.Web.Locators.Department_locators import Department_Locators
from selenium.webdriver.common.by import By
from Managment.Web.Utils.utils import Utilitis
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


class DepartmentPageFunc:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.department_button = Department_Locators.departmet_button
        self.name_field = Department_Locators.name_field
        self.background_photo = Department_Locators.background_photo
        self.add_button = Department_Locators.add_button
        self.activ_button = Department_Locators.activ_button
        self.assert_name_txt_Position_1 = Department_Locators.assert_name_txt_Position_1
        self.assert_name_txt_Position_2 = Department_Locators.assert_name_txt_Position_2
        self.assert_txt_error = Department_Locators.assert_txt_error
        self.Identifier_txt_position2 = Department_Locators.Identifier_txt_position2
        self.assert_txt_search_error = Department_Locators.assert_txt_search_error
        self.ui_txt = Department_Locators.ui_txt
        self.menuBar = Department_Locators.menuBar
        self.update_button = Department_Locators.update_button
        self.assert_img = Department_Locators.assert_img
        self.dropMenu_option_department = Department_Locators.dropMenu_option_department
        self.img_src_position_2 = Department_Locators.img_src_position_2
        self.assert_img_background = Department_Locators.assert_img_background


    def click_department_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.department_button).click()

    def enter_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR,self.name_field).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.name_field).send_keys(name)

    def add_background_photo(self,name):
        self.driver.find_element(By.XPATH,self.background_photo).send_keys(name)

    def click_on_add_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.add_button).click()

    def click_on_active_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.activ_button).click()

    def assertDepartment(self, x):
        if x == True:
            return self.driver.find_element(By.XPATH,self.assert_name_txt_Position_1).get_attribute('innerText')
        else:
            return self.driver.find_element(By.XPATH, self.assert_name_txt_Position_2).get_attribute('innerText')

    def assertDepartmentError(self):
        return self.driver.find_element(By.XPATH,self.assert_txt_error).get_attribute('innerText')

    def searchIdentifier(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.Identifier_txt_position2).get_attribute('innerText')

    def searchDepartmentIncorrectly(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.assert_txt_search_error).get_attribute('innerText')

    def ui_txt_for_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ui_txt).get_attribute('innerText')

    def ui_txt_for_menu_bar(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.menuBar).get_attribute('innerText')

    def ui_txt_for_dropMenu(self,x):
            return self.driver.find_element(By.CSS_SELECTOR, self.dropMenu_option_department.format(x)).get_attribute('innerText')


    def click_on_department(self):
        self.driver.find_element(By.CSS_SELECTOR, self.Identifier_txt_position2).click()

    def click_on_update_button(self):
        self.driver.find_element(By.CLASS_NAME, self.update_button).click()

    def assert_img_src_photo(self,x):
        if x == True:
            return self.driver.find_element(By.CSS_SELECTOR, self.assert_img).get_attribute("src")
        else:
            return self.driver.find_element(By.CSS_SELECTOR, self.assert_img_background).get_attribute("src")

















