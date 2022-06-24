""" General Locators for Utils"""

class Utils_Locators:
    search_field = "(//input[@type='search'])[1]"
    options_btn = ".fa.fa-ellipsis-v.icon_icon"
    add_btn = "//span[contains(text(),'הוספה')]"
    export_btn = "(//span[contains(text(),'ייצוא')])[1]"
    desc_boxs = "//input[@placeholder='תיאור']"
    present_res = "paging_select"
    res_amount = "//div[normalize-space()='{}']"
    table_res = "//table[1]/tbody[1]/tr[1]"
    photo_field = "(//input[contains(@type,'file')])[1]"

