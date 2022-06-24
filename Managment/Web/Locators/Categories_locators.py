""" Locators for Categories screen"""

class CategoriesLocators:

    categories_nav_btn = "//nav[1]/div[2]/a[21]"
    search_categ_btn = "(//input[@type='search'])[1]"
    options = "(//i[@class='fa fa-ellipsis-v icon_icon '])"
    add_btn = "(//span[contains(text(),'הוספה')])[1]"
    name_field = "//input[@tabletype='string']"
    department_filed = "//input[contains(@placeholder,'מחלקות')]"
    fields_name = "(//input[@placeholder='שם'])[2]"
    type_field = "input[placeholder='סוג']"
    type_ops = "//div[contains(text(),'{}')]"
    add_submit = "//input[@value='הוספה']"
    product_status_op = "//span[@class='checkbox_checkboxCircle']"
    add_categ_button = "input[value='הוספה']"
    assert_name = "//tbody/tr/td[2]"
    assert_dep = "//body[1]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/div[1]"
    required_message_name = "//div[contains(@class,'formItem_name')]//div[contains(@class,'form_note')][normalize-space()='']"
    required_message_second_name_field = "//div[@class='form_note ']"
    required_message_type_field = "//div[@class='form_note ']"
    uniq_message = "//div[@class='form_message']"

    search_name = "//td[contains(text(),'שושנים')]"
    search_categ = "//div[contains(text(),'קוניאק')]"
    update_buttun = "//input[@value='עדכון']"
    indentify = "//td[normalize-space()='4jp555dl4n0mk5b']"
    status = "//tbody/tr[1]/td[4]"
    ui_categ_page = "//div[@class='pages_children']"



