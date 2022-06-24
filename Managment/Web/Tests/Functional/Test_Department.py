import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Department_page import DepartmentPageFunc
from selenium.webdriver.support import expected_conditions as EC
from Managment.Web.Utils.utils import Utilitis
from Managment.DB.BaseMongoDB2 import MongoDB

DB = MongoDB("trado_qa", "departments")


@pytest.mark.usefixtures('connect_home_page')
class TestDepartment(Base):


    """Test for department export"""
    def test_Export_departments_properly_success(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # Using the "export button" function
        util.exportBtn()
        time.sleep(3)

    """Tests for Creating a new department"""
    def test_Adding_a_department_success(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # Using the "add button" function
        time.sleep(3)
        util.addBtn(True)
        time.sleep(5)
        # Using the "random string" function
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\logo-linkedin-4096.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "searchField" function
        util.searchField(name)
        time.sleep(3)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), name)
        # Using the "assert" function for DB
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)

    def test_Create_a_new_department_invalid_when_all_fields_are_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(3)
        # Using the "add button" function
        util.addBtn(True)
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    def test_Create_a_new_department_invalid_when_a_name_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn(True)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\R.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    def test_Create_a_new_department_correctly_when_image_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn(True)
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\logo-linkedin-4096.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "searchField" function
        util.searchField(name)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), name)
        # Using the "assert" function for DB
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)

    def test_Create_a_new_department_correctly_when_a_Background_photo_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn(True)
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "searchField" function
        util.searchField(name)
        time.sleep(2)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), name)
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)

    def test_Create_a_new_department_invalid_when_name_and_image_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn(True)
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\logo-linkedin-4096.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    def test_Create_a_new_department_correctly_when_Background_photo_and_image_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn(True)
        # Using the "random string" function
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "click on add button" function
        add.click_on_add_button()
        # Using the "searchField" function
        util.searchField(name)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(True), name)
        # Using the "assert" function for DB
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)


    def test_Create_a_new_department_invalid_when_Background_photo_and_name_field_is_null(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "add button" function
        util.addBtn(True)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "click on add button" function
        add.click_on_add_button()
        driver.implicitly_wait(10)
        # Using the "assert" function
        util.assertFunc(add.assertDepartmentError(), 'נא למלא שדה זה')

    """Tests for departments search"""
    def test_Valid_search_when_Identifier_correctly(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        # Using the "searchField" function
        util.searchField('חלב')
        # Using the "assert" function
        util.assertFunc(add.searchIdentifier(), '4jp555dl4gtcums')

    @pytest.mark.skip
    def test_Search_properly_when_products_are_available(self):
        driver = self.driver
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        util = Utilitis(driver)
        util.secachItemValidation()

    def test_Invalid_search_when_Identifier_incorrect(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(2)
        id = util.randomString()
        # Using the "searchField" function
        util.searchField(id)
        # Using the "assert" function
        time.sleep(2)
        util.assertFunc(add.searchDepartmentIncorrectly(), 'סה״כ: 0 שורות')

    def test_Invalid_search_when_name_incorrect(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        #sleep
        time.sleep(3)
        item = util.randomString()
        item = [item]
        for j in item:
            util.searchField(j)
            time.sleep(6)
            assert (add.searchDepartmentIncorrectly(), 'סה״כ: 0 שורות')

        """Tests for departments update"""

    def test_Update_all_fields_properly_in_active_mode(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        time.sleep(4)
        # Using the "click_on_active_button" function
        add.click_on_active_button()
        # Using the "random string" function
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\R.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        time.sleep(2)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), name)
        # Using the "assert" function for DB
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)

    def test_Update_all_fields_properly_in_inactive_mode(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "random string" function
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\R.png''')
        # Using the "add background photo" function
        add.add_background_photo(r'''C:\Users\R.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        time.sleep(2)
        util.assertFunc(add.assertDepartment(False), name)
        # Using the "assert" function for DB
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)

    def test_Update_properly_when_an_update_is_made_only_in_the_Name_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)

        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "random string" function
        name = util.randomString()
        # Using the "enter name" function
        add.enter_name(name)
        # Using the "click on update button" function
        add.click_on_update_button()
        time.sleep(5)
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), name)
        # Using the "assert" function for DB
        body = DB.find({'name':name})
        result = body['name']
        print(result)
        util.assertFunc(result,name)

    def test_Update_properly_when_no_update_is_made(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assertDepartment(False), 'QfnoRRgLDR')
        # Using the "assert" function for DB
        body = DB.find({'name':'QfnoRRgLDR'})
        result = body['name']
        print(result)
        util.assertFunc(result,'QfnoRRgLDR')

    def test_Update_properly_when_an_update_is_made_only_in_the_photo_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "add photo" function
        util.add_photo(r'''C:\Users\logo-linkedin-4096.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        time.sleep(6)
        print(add.assert_img_src_photo(True))
        util.assertFunc(add.assert_img_src_photo(True),'https://storage.cloud.google.com/trado_images/department/4jp555dl4grc8zwpslie6ckppafmkm-1655367955340')

    def test_Update_properly_when_an_update_is_made_only_in_the_Background_photo_field(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        # sleep
        time.sleep(3)
        add.click_on_department()
        # Using the "add photo" function
        add.add_background_photo(r'''C:\Users\logo-linkedin-4096.png''')
        # Using the "click on update button" function
        add.click_on_update_button()
        # Using the "assert" function
        util.assertFunc(add.assert_img_src_photo(False),'https://storage.cloud.google.com/trado_images/department/4jp555dl4gt31kypslie6ckppafmkm-1655370885238')



























