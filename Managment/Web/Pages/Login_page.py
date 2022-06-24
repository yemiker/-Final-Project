from Managment.Web.Locators.Login_locators import Login_Locators
from selenium.webdriver.common.by import By


class LoginPageFunc():
    def __init__(self, driver):
        self.driver = driver
        self.phone_field = Login_Locators.phone_field
        self.code_field = Login_Locators.code_field
        self.button_phon = Login_Locators.button_phon
        self.button_login = Login_Locators.button_login
        self.trado_logo = Login_Locators.trado_logo
        self.phone_lable = Login_Locators.phone_lable
        self.nameT1 = Login_Locators.nameT1
        self.nameT2 = Login_Locators.nameT2
        self.user2 = Login_Locators.user2


    def enter_phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR, self.phone_field).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.phone_field).send_keys(phone)

    def enter_phone_code(self, phone_code):
        self.driver.find_element(By.CSS_SELECTOR, self.code_field).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.code_field).send_keys(phone_code)

    def click_on_button(self):
        self.driver.find_element(By.XPATH, self.button_phon).click()

    def click_on_button_login(self):
        self.driver.find_element(By.XPATH, self.button_login).click()

    def get_logo(self):
        return self.driver.find_element(By.XPATH, self.trado_logo).get_attribute('src')

    def get_phone_lable(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.phone_lable).get_attribute('defaultValue')

    def get_nameT1(self):
        return self.driver.find_element(By.XPATH,self.nameT1).get_attribute("innerText")

    def get_nameT2(self):
        return self.driver.find_element(By.XPATH, self.nameT2).get_attribute("innerText")

    def get_user2(self):
        return self.driver.find_element(By.XPATH, self.user2).get_attribute("innerText")

    def test(self):
        pass