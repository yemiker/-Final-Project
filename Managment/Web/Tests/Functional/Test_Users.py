import pytest
import random
from selenium.webdriver.common.by import By
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Users_page import Userspagefunc
from Managment.Web.Locators.Users_locators import UsersLocators
from Managment.Web.Utils.utils import Utilitis
import os.path
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Managment.DB.BaseMongoDB2 import MongoDB
db = MongoDB("trado_qa", "users")





@pytest.mark.usefixtures('connect_home_page')
class TestUsers(Base):

    #1
    @pytest.mark.sanity
    def test_valid_addUser(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em+"@jd.com")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.store_option("dddd")
        user.add_btn()
        val = user.get_text1(user.varify,phone)
        sleep(2)
        data = db.find({'firstName':name})
        util.assertFunc(val,data['phone'])

    #2
    @pytest.mark.sanity
    def test_invalid_phone(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em + "@jd.com")
        phone = util.random_with_N_digits(7)
        user.addphone(phone)
        user.store_option("dddd")
        user.add_btn()
        val = util.get_text(UsersLocators.eror_note)
        util.assertFunc(val, 'מס׳ טלפון לא תקין')

    #3
    def test_invalid_email(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em + "jd")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.store_option("dddd")
        user.add_btn()
        emil = util.get_text(UsersLocators.eror_note)
        util.assertFunc(emil, 'דוא״ל לא תקין')

    #4
    @pytest.mark.sanity
    def test_valid_addUser_ALLnull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        user.addname("")
        user.addlastname("")
        user.addemil("")
        user.addphone(util.random_with_N_digits(10))
        user.add_btn()
        massege = util.valid_Message(UsersLocators.erorStore)
        util.assertFunc(massege, "Please fill out this field.")
        sleep(3)
        element = user.displayedElement(UsersLocators.store_list)
        util.assertFunc(element, "Element found")


    #5
    @pytest.mark.sanity
    def test_invalid_emailNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil("")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.store_option("dddd")
        user.add_btn()
        emil = util.get_text(UsersLocators.eror_note)
        util.assertFunc(emil ,'דוא״ל לא תקין')


    #6
    @pytest.mark.sanity
    def test_phoneNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em + "@jd.com")
        user.addphone("")
        user.store_option("dddd")
        user.add_btn()
        val = util.get_text(UsersLocators.eror_note)
        util.assertFunc(val ,'מס׳ טלפון לא תקין')


    #7
    @pytest.mark.sanity
    def test_storeNull(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        util.addBtn(True)
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em + "@jd.com")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.add_btn()
        element = user.displayedElement(UsersLocators.store_list)
        util.assertFunc(element,"Element found")
        massege = util.valid_Message(UsersLocators.erorStore)
        util.assertFunc(massege,"Please fill out this field.")


    #8
    @pytest.mark.sanity
    def test_serch_User_name(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        user.search_box("ישראל")
        sleep(2)
        name = util.get_text(UsersLocators.serName)
        util.assertFunc(name,"ישראל")
        data = db.find({'firstName': "ישראל"})
        util.assertFunc(name, data['firstName'])

    #9
    @pytest.mark.sanity
    def test_serch_User_lastname(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.search_box("אלמיהו")
        lastname = util.get_text(UsersLocators.serLastname)
        util.assertFunc(lastname,"אלמיהו")
        data = db.find({'lastName': "אלמיהו"})
        util.assertFunc(lastname, data['lastName'])


    #10
    def test_serch_User_phone(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        user.search_box("0549703147")
        phone = util.get_text(UsersLocators.serPhone)
        util.assertFunc(phone,"0549703147")
        data = db.find({'phone': "0549703147"})
        util.assertFunc(phone, data['phone'])

    #11
    @pytest.mark.regression
    def test_valid_update(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        user.update_click()
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em + "@jd.com")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.update_btn()
        sleep(2)
        firstName = util.get_text(UsersLocators.firstName)
        util.assertFunc(firstName,"יוסף")


    #12
    @pytest.mark.regression
    def test_update_when_store_null(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        sleep(2)
        user.update_click()
        name = util.randomString()
        user.addname(name)
        lastName = util.randomString()
        user.addlastname(lastName)
        em = util.randomString2letters()
        user.addemil(em + "@jd.com")
        phone = util.random_with_N_digits(10)
        user.addphone(phone)
        user.update_btn()
        massege = util.valid_Message(UsersLocators.erorStore)
        util.assertFunc(massege, "Please fill out this field.")
        sleep(2)
        element = user.displayedElement(UsersLocators.store_list)
        util.assertFunc(element, "Element found")

    #13
    @pytest.mark.regression
    def test_export_btn(self):
        driver = self.driver
        user = Userspagefunc(driver)
        util = Utilitis(driver)
        driver.implicitly_wait(10)
        user.userpage_btn()
        util.exportBtn()
        expected_result = True
        result = os.path.exists(r"/Users/dnylgmbr/Downloads/משתמשים - 22.06.22.csv")
        util.assertFunc(result, expected_result)


    # def test_one(self):
    #     driver = self.driver
    #     user = Userspagefunc(driver)
    #     util = Utilitis(driver)
    #     phone = util.random_with_N_digits(10)
    #     name = util.randomString()
    #     driver.implicitly_wait(10)
    #     user.userpage_btn()
    #     sleep(2)
    #     util.addBtn(True)
    #     user.fillInputfileds(name,phone)
    #     user.add_btn()
    #     val = user.get_text1(user.varify, phone)
    #     sleep(2)
    #     data = db.find({'firstName': name})
    #     util.assertFunc(val, data['phone'])
