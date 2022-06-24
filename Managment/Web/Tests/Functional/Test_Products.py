import time
import random
from datetime import date

import pytest
import allure
import os.path
from Managment.DB.BaseMongoDB2 import MongoDB
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Products_page import ProductsPageFunc
from Managment.Web.Utils.utils import Utilitis
db = MongoDB("trado_qa", "products")

@pytest.mark.usefixtures('connect_home_page')
class TestProducts(Base):
    """test 1 """

    @pytest.mark.sanity
    def test_add_a_new_product_to_my_store_corrctly2(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)
        # upload photo
        # pic = r'C:\Users\97253\Downloads\upload_test.png'
        # util.add_photo(pic)
        # set mandatory fields barcode, name ,price
        n = random.randint(1, 99)
        prod.fill_all_form_fields(f"100{n}1", f"product{n}", 2500)
        prod.click_next_btn()

        driver.refresh()
        util.searchField(f"100{n}1")

        value = prod.row_details("name")
        util.assertFunc(value, f"product{n}")
        # product_in_db = db.find_one_key("name",f"product{n}")
        # util.assertFunc(product_in_db,value)


    """test 2"""
    def test_add_a_new_product_to_my_store_incorrctly_when_barcode_field_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)

        prod.set_mandatory_fields_of_product("", "full", 100)
        prod.click_next_btn()
        expecte_result = "Please fill out this field."
        message = util.valid_Message(prod.barcode_field)
        util.assertFunc(message,expecte_result)

    """test 3 """
    def test_add_a_new_product_to_my_store_incorrctly_when_name_field_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)

        prod.set_mandatory_fields_of_product("03", "", 100)
        prod.click_next_btn()
        expecte_result = "Please fill out this field."
        message = util.valid_Message(prod.product_name_field)
        util.assertFunc(expecte_result,message)

    """test 4 """
    def test_add_a_new_product_to_my_store_incorrctly_when_price_field_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)
        # price field null
        prod.set_mandatory_fields_of_product("033", "qa", "")
        prod.click_next_btn()
        expecte_result = "Please fill out this field."
        message = util.valid_Message(prod.product_price)
        util.assertFunc(expecte_result,message)

    """test 5 """
    def test_add_a_new_product_to_my_store_incorrctly_when_all_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)
        # all fields null
        prod.set_mandatory_fields_of_product("", "", "")
        prod.click_next_btn()
        expecte_result = "Please fill out this field."
        message = util.valid_Message(prod.barcode_field)
        util.assertFunc(expecte_result,message)

    """test 6 stage 2 """

    def test_add_a_new_product_to_my_store_incorrctly_when_category_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)
        #stage 1
        prod.set_mandatory_fields_of_product("44", "test", "100")
        prod.click_next_btn()
        # stage 2 fill all fields apart from category option
        prod.kidom_option(0)
        prod.store_option("סופר כל רונן בע״מ")
        prod.click_next_btn()

        message = util.valid_Message(prod.cate_btn)
        expecte_result = "Please fill out this field."
        util.assertFunc(expecte_result,message)

    """test 7 stage 2 """

    @pytest.mark.sanity
    def test_add_a_new_product_to_my_store_incorrctly_when_store_field_are_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)
        #stage 1
        prod.set_mandatory_fields_of_product("44", "test", "100")
        prod.click_next_btn()
        #stage 2 fill all fields apart from store option
        prod.category_option("חטיפים")
        prod.click_dep_auto_option()
        prod.kidom_option(0)
        prod.click_next_btn()
        time.sleep(2)

        message = util.valid_Message(prod.store_btn)
        expecte_result = "Please fill out this field."
        util.assertFunc(expecte_result, message)

    """test 8 editing """

    @pytest.mark.sanity
    def test_search_for_specific_product_and_edit_a_product_info_to_my_store_corrctly(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        #search for a product to edit
        util.search_box("voadka4")
        #change date
        n = random.randint(1, 9)
        prod.insert_barcode_name(f"0{n}00{n}")
        prod.insert_product_price("120")
        time.sleep(5)
        prod.click_next_number_off_times(5)
        driver.refresh()

        util.searchField("voadka4")
        value = prod.row_details("barcode")
        util.assertFunc(value,f"0{n}00{n}")
        #DB assert
        product_in_db = db.find({"name":"voadka4"})
        db_barcode = product_in_db["barcode"]

        util.assertFunc(f"0{n}00{n}",db_barcode)

    """test 9 editing """

    @pytest.mark.sanity
    def test_edit_a_product_info_incorrctly_when_price_is_letters(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("testagin")
        # change date
        prod.insert_product_price("handred")
        message = util.valid_Message(prod.product_price)
        expected_result = "Please enter a number."
        prod.click_next_btn()
        util.assertFunc(message,expected_result)

    """test 10 editing """
    def test_edit_a_product_info_incorrctly_when_barcode_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("testagin")
        # change date
        prod.insert_barcode_name("")
        message = util.valid_Message(prod.barcode_field)

        expected_result = "Please fill out this field."
        prod.click_next_btn()
        util.assertFunc(message,expected_result)

    """test 11 editing """
    def test_edit_a_product_info_incorrctly_when_name_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("testagin")
        # change date
        prod.insert_product_name("")
        message = util.valid_Message(prod.product_name_field)

        expected_result = "Please fill out this field."
        prod.click_next_btn()
        util.assertFunc(message, expected_result)

    """test 12 editing """
    def test_to_edit_a_product_incorractly_when_catagory_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("017")

        prod.click_next_btn()
        prod.clear_category_field()

        prod.click_next_btn()
        message = util.valid_Message(prod.cate_btn)
        expected_result = "Please fill out this field."
        util.assertFunc(message,expected_result)

    """test 13 editing """
    def test_to_edit_a_product_incorractly_when_store_is_null(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("xfv")

        prod.click_next_btn()
        prod.clear_store_field()
        #make click no yvoan op to close store pop window
        prod.click_yvoan_op()

        prod.click_next_btn()
        message = util.valid_Message(prod.store_btn)
        expected_result = "Please fill out this field."
        util.assertFunc(message, expected_result)

    """test 14 editing """

    @pytest.mark.sanity
    def test_activate_product_status_succsessfully(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("prigat")
        #activate product status on
        prod.click_status_active_op()
        prod.click_next_number_off_times(5)
        driver.refresh()
        util.searchField("prigat")
        util.assertFunc(prod.row_details("status"),"✓")
        #DB assert
        expected_result = True
        db_result = db.find({"name":"prigat"})["active"]
        util.assertFunc(db_result,expected_result)

    """test 15 editing """
    def test_deactivate_product_status_succsessfully(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("prigat")
        # activate product status on
        prod.click_status_active_op()
        prod.click_next_number_off_times(5)
        util.searchField("prigat")
        util.assertFunc(prod.row_details("status"), '✗')
        # DB assert
        expected_result = False
        db_result = db.find({"name": "prigat"})["active"]
        print(db_result)
        util.assertFunc(db_result, expected_result)


    """test 16 editing """
    def test_search_product_that_dont_exist(self):

        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()

        util.searchField("fgfdhgfhghgfh")
        time.sleep(2)
        message = util.get_text(prod.amount_result)
        expected_result = "סה״כ: 0 שורות"

        util.assertFunc(message,expected_result)

    """test 17 editing """

    def test_search_for_specific_product_and_edit_a_product_exp_date_corrctly(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        # nev to products screen
        prod.click_products_btn()
        # search for a product to edit
        util.search_box("Charger")
        new_date = "07.26.2022"
        prod.insert_expiration_date(new_date)
        prod.click_next_number_off_times(5)
        product_in_db = db.find({"name":"Charger"})
        db_date = product_in_db["expirationDate"]
        #reversd date
        db_date= prod.revers_date(db_date,"up")
        #assert
        util.assertFunc(db_date,new_date)




    """test 18 editing """
    def test_export_file_to_pc(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        time.sleep(2)
        util.exportBtn()
        driver.implicitly_wait(30)
        time.sleep(5)
        today = date.today()
        x = prod.revers_date(today,"ex")
        expected_result = True
        txt = rf"C:\Users\97253\Downloads\מוצרים - {x}.csv"
        result = os.path.exists(txt)
        util.assertFunc(result,expected_result)



    """test 19 editing """
    @pytest.mark.skip
    def test_edit_product_description_succsessfully(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)

        # nev to products screen
        prod.click_products_btn()
        util.searchField("prigat")
        prod.click_write_desc_to_product()
        descprtion_to_write = "add new comment2"
        prod.write_desc_to_product(descprtion_to_write)
        prod.click_save_desc_changes()
        time.sleep(2)
        prod.click_write_desc_to_product()
        descprtion = util.get_text(prod.writing_box)
        data = db.find({"barcode": "04991"})
        expected_result = data['description'][3:-5]
        # validation with data base
        util.assertFunc(descprtion_to_write,expected_result)









