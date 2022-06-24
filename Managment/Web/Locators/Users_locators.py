""" Locators for Users screen"""

class UsersLocators:

    user_nav_btn = "//span[contains(text(),'משתמשים')]"
    search_field = "(//input[@type='search'])[1]"



    #add users locators
    name = "//input[@placeholder='שם פרטי']"
    lastname = "//input[@placeholder='שם משפחה']"
    emil = "//input[@placeholder='דואר אלקטרוני']"
    phone = "//input[@placeholder='טלפון']"
    store = "//input[contains(@placeholder,'חנויות')]"
    store_ops = "//div[@class='input_autocompleteItem '][contains(text(),'{}')]"
    pick ="// body // div // span // div // div[2]"
    btnadd = "//input[@value='הוספה']"

    #assert locator
    varify = "//td[normalize-space()='{}']"
    eror_note = "div[class='form_note ']"
    store_list = ".input_autocompleteBox.input_open"
    erorStore = "input[placeholder='חנויות']"
    serName = "tbody tr:nth-child(1) td:nth-child(1)"
    serLastname = "tbody:nth-child(2) tr:nth-child(1) > td:nth-child(2)"
    serPhone = "tbody tr td:nth-child(1)"
    firstName = "tbody:nth-child(2) tr:nth-child(1) > td:nth-child(1)"

    #update locators
    update = "//tbody/tr[1]/td[1]"
    updt_btn = "input[value='עדכון']"
    head = "h4[class='title_title modal_title'] span"



