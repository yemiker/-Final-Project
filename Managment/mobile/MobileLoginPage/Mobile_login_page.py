from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class MobileLoginPageFunc():
    def __init__(self, driver):
        self.driver = driver
        self.phone_field = "//div[@id='root']/div[1]/div[2]/div/span/form/div[1]/div/span/div/input"
        self.button_phon = "//div[@id='root']/div[1]/div[2]/div/span/form/input"
        self.code_field = "//div[@id='root']/div[1]/div[2]/div/span/form/div[1]/div[1]/span/div/input"
        self.button_login = "//div[@id='root']/div[1]/div[2]/div/span/form/input"
        self.trado_store_btn = "//div[@id='root']/div[1]/div[2]/div/div/div/div[2]/div[1]"
        self.prodcut_page_ = "//div[@id='root']/div[1]/div[2]/main/div[2]/div/div[1]/a[4]"



    def enter_phone(self, phone):
        pho = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, self.phone_field))
        )
        pho.clear()
        pho.send_keys(phone)

    def enter_phone_code(self, phone_code):
        code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, self.code_field))
        )
        code.clear()
        code.send_keys(phone_code)

    def click_on_button(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, self.button_phon))
        )
        btn.click()

    def click_on_button_login(self):
        log = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, self.button_login))
        )

        log.click()



    def click_trado_store(self):
        trado = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, self.trado_store_btn))
        )
        trado.click()


    def click_product_store_btn(self):
        store = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, self.prodcut_page_))
        )
        store.click()





