import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..Locators.Products_locators import ProductsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPageFunc:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.dasbord_products_btn = ProductsLocators.dasbord_products_btn
        self.product_status_op = ProductsLocators.product_status_op
        self.desc_boxs = ProductsLocators.desc_boxs
        self.barcode_field = ProductsLocators.barcode_field
        self.product_name_field = ProductsLocators.product_name_field
        self.product_price = ProductsLocators.product_price
        self.date_field = ProductsLocators.date_field
        self.next_btn = ProductsLocators.next_btn
        self.back_btn = ProductsLocators.back_btn
        self.cate_btn = ProductsLocators.cate_btn
        self.cate_op = ProductsLocators.cate_op
        self.store_btn = ProductsLocators.store_btn
        self.store_op = ProductsLocators.store_op
        self.dep_btn = ProductsLocators.dep_btn
        self.dep_auto_op = ProductsLocators.dep_auto_op
        self.kidom_field = ProductsLocators.kidom_field
        self.kidom_op = ProductsLocators.kidom_op
        self.yvoan_makbil = ProductsLocators.yvoan_makbil
        self.wight_btn = ProductsLocators.wight_btn
        self.wight_avg_per_unit_field = ProductsLocators.wight_avg_per_unit_field
        self.wight_unit_scale_btn = ProductsLocators.wight_unit_scale_btn
        self.scale_op = ProductsLocators.scale_op
        self.boxes_amout_field = ProductsLocators.boxes_amout_field
        self.amout_field = ProductsLocators.amout_field
        self.min_amout_field = ProductsLocators.min_amout_field
        self.city_field = ProductsLocators.city_field
        self.street_field = ProductsLocators.street_field
        self.home_num_field = ProductsLocators.home_num_field
        self.contact_num_field = ProductsLocators.contact_num_field
        self.row_res_details = ProductsLocators.row_res_details
        self.add_description_btn = ProductsLocators.add_description_btn
        self.writing_box = ProductsLocators.writing_box
        self.save_changes_btn = ProductsLocators.save_changes_btn
        self.all_desc_box = ProductsLocators.all_desc_box
        self.amount_result = ProductsLocators.amount_result
        self.table_column = ProductsLocators.table_column
        self.option_content = ProductsLocators.option_content
        self.all_form_stage_conntent = ProductsLocators.all_form_stage_conntent
        self.quit_form_btn = ProductsLocators.quit_form_btn

    @allure.step("get all 5 form stages ")
    def form_conntent(self):
        b = {}
        f = []
        stage_5 = self.driver.find_element(By.CSS_SELECTOR,self.all_form_stage_conntent.format(5)).text.split("\n")
        for i in range(1,6):
            if i == 5:
                b[stage_5[0]] = stage_5[1]
                continue
            x = self.driver.find_element(By.CSS_SELECTOR,self.all_form_stage_conntent.format(i))
            text = x.text.split("\n")
            b[text[0]] = text[1]
            if i == 1:
                self.set_mandatory_fields_of_product("dff", "dsfsdf", 12)
                self.click_next_btn()
            elif i == 2:
                self.category_option("חטיפים")
                self.click_dep_auto_option()
                self.store_option("סופר כל רונן בע״מ")
                self.click_next_btn()
            elif i == 3:
                self.set_boxes_amout_data("12","22","2")
                self.click_next_btn()
            elif i == 4:
                self.set_address_data("","","","0542245936")
                self.click_next_btn()
            else:
                self.click_quit_btn()
                break

            after_text = x.text.split("\n")
            f.append(after_text[0] +" "+ after_text[1])
        return b

    @allure.step("fill all form fields ")
    def fill_all_form_fields(self, barcode, name, price):
        self.set_mandatory_fields_of_product(barcode, name, price)
        self.click_next_btn()

        self.category_option("חטיפים")
        self.click_dep_auto_option()
        self.store_option("סופר כל רונן בע״מ")
        self.click_next_btn()

        self.set_boxes_amout_data("12", "22", "2")
        self.click_next_btn()

        self.set_address_data("bra", "zil", "55", "0542245936")
        self.click_next_btn()

    @allure.step("get all table columns ")
    def column_conntent_text(self):
        columns = []
        for i in range(1,18):
            time.sleep(1)
            x = self.driver.find_element(By.CSS_SELECTOR, self.table_column.format(i))
            columns.append(x.get_attribute("innerText"))
            # print(x.get_attribute("innerText"))

        return columns

    @allure.step("get all options content ")
    def option_content_text(self):
        ops = []

        for i in range(1,6):
            x = self.driver.find_element(By.XPATH, self.option_content.format(i))
            time.sleep(1)
            ops.append(x.text)
        return ops

    @allure.step("Click quit button")
    def click_quit_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.quit_form_btn))
        ).click()

    @allure.step("Click product on navbar")
    def click_products_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.dasbord_products_btn))
        ).click()

    @allure.step("Click next button ")
    def click_next_btn(self):
        action = ActionChains(self.driver)

        next = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.next_btn))
        )
        action.move_to_element(next).click(next).perform()

    @allure.step("Click back button")
    def click_back_btn(self):
        back_action = ActionChains(self.driver)
        back = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,self.back_btn))
        )
        back_action.move_to_element(back).click(back).perform()

    @allure.step("Click active button")
    def click_status_active_op(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.product_status_op))
        ).click()

    @allure.step("Insert barcode name to form")
    def insert_barcode_name(self, barcode_data=None):
        barcode = self.driver.find_element(By.CSS_SELECTOR, self.barcode_field)
        barcode.clear()
        barcode.send_keys(barcode_data)

    @allure.step("Insert product name to form")
    def insert_product_name(self, product_data=None):
        product = self.driver.find_element(By.CSS_SELECTOR, self.product_name_field)
        product.clear()
        product.send_keys(product_data)

    @allure.step("Insert product price to form")
    def insert_product_price(self, price_data=None):
        price = self.driver.find_element(By.CSS_SELECTOR, self.product_price)
        price.clear()
        price.send_keys(price_data)

    @allure.step("Set all mandatory fields to form")
    def set_mandatory_fields_of_product(self, barcode_data, product_name, product_price_data):
        self.barcode_data = barcode_data
        self.product_name = product_name
        self.product_price_data = product_price_data
        self.driver.find_element(By.CSS_SELECTOR, self.barcode_field).send_keys(self.barcode_data)

        self.driver.find_element(By.CSS_SELECTOR, self.product_name_field).send_keys(self.product_name)

        self.driver.find_element(By.CSS_SELECTOR, self.product_price).send_keys(self.product_price_data)

    @allure.step("Insert product expiration date to form")
    def insert_expiration_date(self, expiration_date):
        self.expiration_date = expiration_date

        date = self.driver.find_element(By.CSS_SELECTOR, self.date_field)
        date.clear()
        time.sleep(2)
        date.send_keys(self.expiration_date)

    @allure.step("Select category option")
    def category_option(self, op):
        self.category = self.driver.find_element(By.CSS_SELECTOR, self.cate_btn)
        self.category.click()

        options = self.driver.find_element(By.XPATH, self.cate_op.format(op))
        options.click()

    @allure.step("Clear data from category field")
    def clear_category_field(self):
        self.category = self.driver.find_element(By.CSS_SELECTOR, self.cate_btn)
        self.category.clear()

    @allure.step("Select department option")
    def dep_option(self, op):
        self.department = self.driver.find_element(By.CSS_SELECTOR, self.dep_btn)
        self.department.click()

        options = self.driver.find_elements(By.XPATH, self.store_op)
        options[op].click()

    @allure.step("Click department first option")
    def click_dep_auto_option(self):
        self.driver.find_element(By.XPATH, self.dep_auto_op).click()

    @allure.step("Click on Yvoan option")
    def click_yvoan_op(self):
        action_yvoan = ActionChains(self.driver)

        yvoan = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.yvoan_makbil))
        )
        action_yvoan.move_to_element(yvoan).click(yvoan).perform()

    @allure.step("Select store option")
    def store_option(self, op):
        self.store = self.driver.find_element(By.CSS_SELECTOR, self.store_btn)
        self.store.click()


        options = self.driver.find_element(By.XPATH, self.store_op.format(op))
        options.click()

    @allure.step("Clear data from store field")
    def clear_store_field(self):
        self.category = self.driver.find_element(By.CSS_SELECTOR, self.store_btn)
        self.category.clear()

    @allure.step("Select kidon option")
    def kidom_option(self, op):
        kidom = self.driver.find_element(By.XPATH, self.kidom_field)
        kidom.click()

        options = self.driver.find_elements(By.XPATH, self.kidom_op)
        options[op].click()

    @allure.step("Click wight option and set data")
    def set_wight_op_on_with_data(self, op, wight):
        self.driver.find_element(By.XPATH, self.wight_btn).click()
        avg_wight = self.driver.find_element(By.XPATH, self.wight_avg_per_unit_field)
        avg_wight.clear()
        avg_wight.send_keys(wight)
        unit_scale = self.driver.find_element(By.XPATH, self.wight_unit_scale_btn)
        unit_scale.clear()
        unit_scale.click()
        options = self.driver.find_element(By.XPATH, self.scale_op.format(op))
        options.click()

    @allure.step("Set Boxes amount to form ")
    def set_boxes_amout_data(self, boxes, amount, min):
        boxes_amount = self.driver.find_element(By.XPATH, self.boxes_amout_field)
        boxes_amount.clear()
        boxes_amount.send_keys(boxes)

        total_amount = self.driver.find_element(By.XPATH, self.amout_field)
        total_amount.clear()
        total_amount.send_keys(amount)

        min_amount = self.driver.find_element(By.XPATH, self.min_amout_field)
        min_amount.clear()
        min_amount.send_keys(min)

    @allure.step("Set address data to form")
    def set_address_data(self, city, street, home, contact):
        city_input = self.driver.find_element(By.XPATH, self.city_field)
        city_input.clear()
        city_input.send_keys(city)

        street_input = self.driver.find_element(By.XPATH, self.street_field)
        street_input.clear()
        street_input.send_keys(street)

        home_num_input = self.driver.find_element(By.XPATH, self.home_num_field)
        home_num_input.clear()
        home_num_input.send_keys(home)

        contact_num_input = self.driver.find_element(By.XPATH, self.contact_num_field)
        contact_num_input.clear()
        contact_num_input.send_keys(contact)

    @allure.step("Add description details to a product to form")
    def description_details(self, desc):
        description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.desc_boxs))
        )
        description.clear()
        description.send_keys(desc)

    @allure.step("Get specific information on product ")
    def row_details(self, op):
        time.sleep(2)
        bar = self.driver.find_element(By.CSS_SELECTOR, self.row_res_details.format(1)).text
        name = self.driver.find_element(By.CSS_SELECTOR, self.row_res_details.format(3)).text
        price = self.driver.find_element(By.CSS_SELECTOR, self.row_res_details.format(4)).text[1:]
        status = self.driver.find_element(By.CSS_SELECTOR, self.row_res_details.format(10))
        data = [bar, name, price,status]
        if op == "barcode":
            return bar

        elif op == "name":
            return name
        elif op == "price":
            return price
        elif op == "status":
            return status.get_attribute("innerText")

        else:
            return data

    @allure.step("Click next button number of times ")
    def click_next_number_off_times(self,times):
        for i in range(times):
            self.click_next_btn()
        time.sleep(2)

    @allure.step("Click on write description to product")
    def click_write_desc_to_product(self):
        add_action = ActionChains(self.driver)
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.add_description_btn))
        )

        add_action.move_to_element(add_btn).click(add_btn).perform()

    @allure.step("Write comment on product")
    def write_desc_to_product(self,write):

        write_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.writing_box))
        )
        write_box.send_keys(write)

    @allure.step("Click save on changes")
    def click_save_desc_changes(self):
        save = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.save_changes_btn))
        )

        save.click()

    def revers_date(self, date, op):
        d = str(date)
        d = d[:10].split("-")
        if op == "up":
            d = d[1] + "." + d[2] + "." + d[0]
        else:
            d = d[2] + "." + d[1] + "." + d[0][2:]
        return d


