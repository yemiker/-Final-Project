import time
import pytest
import os.path
from Managment.Web.Utils.utils import Utilitis
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Categories_page import CategoriesPageFunc
from Managment.DB.BaseMongoDB2 import MongoDB
db = MongoDB("trado_qa","sections")

@pytest.mark.usefixtures('connect_home_page')
class TestCategories(Base):
    """test 1"""
    @pytest.mark.sanity
    def test_add_new_category_to_my_store_correctly(self):
        driver = self.driver
        #using a func to connect the site
        util = Utilitis(driver)
        x = util.randomString()
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        #entering the categories page
        category.click_categories_navbar()
        #clicking on adding a category
        util.addBtn(True)
        time.sleep(2)
        #insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name(x)
        driver.implicitly_wait(10)
        #insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)
        #insert name field
        category.insert_field_name(x)
        driver.implicitly_wait(10)
        #select type
        category.type_option("טקסט")
        driver.implicitly_wait(10)
        #click on add
        category.click_on_category_add_button()
        time.sleep(3)
        driver.implicitly_wait(2)
        # util.assertFunc(category.get_text_name(),x)
        util.assertFunc(category.get_text_dep(),"קוניאק")
        # """ASSERT WITH DB"""
        # departmentIds = db.find({"name":x})
        # db_result = departmentIds["name"]
        # assert db_result == x

    """test 2"""
    @pytest.mark.skip
    def test_add_new_category_to_my_store_incorrectly_when_name_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        x = util.randomString()
        # util.connect_home_page()
        category = CategoriesPageFunc(driver)
        # entering the categories page
        time.sleep(5)
        # clicking on adding a category
        util.addBtn(True)
        time.sleep(5)
        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        # category.insert_new_category_name("גרבר")
        #insert department name
        category.insert_department_name("קוניאק")
        # insert name field
        category.insert_field_name(x)
        # select type
        category.type_option("טקסט")
        # click on add
        category.click_on_category_add_button()
        time.sleep(3)
        """assert"""
        util.assertFunc(category.get_required_message_name(),"נא למלא שדה זה")


    """test 3"""
    def test_add_new_category_to_my_store_incorrectly_when_category_field_null(self):
        driver = self.driver
        #using a func to connect the site
        util = Utilitis(driver)
        x = util.randomString()
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        #entering the categories page
        category.click_categories_navbar()
        #clicking on adding a category
        time.sleep(2)
        util.addBtn(True)
        time.sleep(2)
        driver.implicitly_wait(10)
        #insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)
        #insert category name
        category.click_status_active_op()
        time.sleep(5)
        category.insert_new_category_name(x)
        #insert name field
        category.insert_field_name(x)
        #select type
        category.type_option("טקסט")
        #click on add
        category.click_on_category_add_button()
        category.click_none()
        time.sleep(4)
        a = util.get_text("body > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)")
        """assert"""
        util.assertFunc(a,"נא למלא שדה זה")


    """test 4"""
    def test_add_new_category_to_my_store_incorrectly_when_second_name_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()
        # clicking on adding a category
        util.addBtn(True)
        time.sleep(2)
        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        # insert department name
        category.insert_department_name("קוניאק")
        # select type
        category.type_option("טקסט")
        time.sleep(5)
        # click on add
        category.click_on_category_add_button()
        time.sleep(7)
        category.click_on_category_add_button()
        time.sleep(7)
        """assert"""
        util.assertFunc(category.get_required_message_second_name_field() , "נא למלא שדה זה")

    """test 5"""
    def test_add_new_category_to_my_store_incorrectly_when_type_field_is_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()
        # clicking on adding a category
        util.addBtn(True)
        time.sleep(2)
        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        # insert department name
        category.insert_department_name("קוניאק")
        # insert name field
        category.insert_field_name("גרב")
        # # select type
        # category.type_option()
        time.sleep(3)
        # click on add
        category.click_on_category_add_button()
        time.sleep(5)
        """assert"""
        util.assertFunc(util.valid_Message(category.type_field),"זהו שדה חובה.")

        """test 6"""
    def test_add_new_category_to_my_store_incorrectly_when_all_fields_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()
        # clicking on adding a category
        util.addBtn(True)
        time.sleep(2)
        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.click_on_category_add_button()
        time.sleep(5)
        """assert"""
        util.assertFunc(util.valid_Message(category.type_field), "זהו שדה חובה.")

        """test 7"""
    def test_add_new_category_to_my_store_incorrectly_when_category_is_exist_with_same_data(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()
        # clicking on adding a category
        util.addBtn(True)
        time.sleep(2)
        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        time.sleep(3)
        # insert department name
        category.insert_department_name("קוניאק")
        time.sleep(3)
        # insert name field
        category.insert_field_name("גרב")
        time.sleep(3)
        # select type
        category.type_option("טקסט")
        time.sleep(3)
        # click on add
        category.click_on_category_add_button()
        time.sleep(3)
        """assert"""
        util.assertFunc(category.get_uniq_message(), "אחד או יותר מהשדות אינם ייחודיים")

        """test 8"""
    @pytest.mark.skip
    def test_search_for_specific_category(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        x = util.randomString()
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # category.click_status_active_op()
        time.sleep(3)
        # entering the categories page
        category.click_categories_navbar()
        time.sleep(5)
        #search for category
        category.search_category("אושי")
        time.sleep(5)
        """asssert"""
        util.assertFunc(category.get_indentify(),"4jp555dl4n0mk5b")

        """test 9"""
    def test_edit_category_incorrectly_when_type_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        x = util.randomString()
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()
        time.sleep(5)
        # search for category
        category.search_category("פרחים")
        time.sleep(5)
        category.click_indentify()
        time.sleep(5)
        category.insert_new_category_name(x)
        time.sleep(5)
        category.insert_field_name(x)
        time.sleep(5)
        # time.sleep(5)
        category.click_update_buttun()
        time.sleep(5)
        """assert"""
        util.assertFunc(util.valid_Message(category.type_field), "זהו שדה חובה.")

        """test 10"""
    def test_export_to_pc(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()
        time.sleep(5)
        util.exportBtn()
        time.sleep(5)
        expected_result = True
        result = os.path.exists(r"C:\Users\oshra\Downloads\קטגוריות  על - 21.06.22.csv")
        """assert"""
        util.assertFunc(result, expected_result)





























