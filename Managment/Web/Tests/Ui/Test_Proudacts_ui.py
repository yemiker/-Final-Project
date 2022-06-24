import time
import pytest
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Products_page import ProductsPageFunc
from Managment.Web.Utils.utils import Utilitis


@pytest.mark.usefixtures('connect_home_page')
class TestProducts(Base):
    def test_ui_for_product_column_table(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        prod.click_products_btn()
        column = ['ברקוד', 'תמונה', 'שם', 'מחיר', 'קידום', 'קטגוריה על', 'מחלקה', 'סוג כשרות', 'חנות', 'פעיל', 'כתובת הזמנה', 'מידע נוסף', 'יצרן', 'יבואן מקביל', 'מותג', 'תאריך יצירה', 'תיאור']

        web_table_column = prod.column_conntent_text()

        util.assertFunc(column,web_table_column)


    def test_ui_for_product_option_conntent(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        prod.click_products_btn()
        util.addBtn(False)
        options = ['הוספה', 'ייצוא', 'add by brand', 'ייבוא', 'תבנית']
        web_options = prod.option_content_text()
        util.assertFunc(options,web_options)

    def test_form_stages_text(self):
        driver = self.driver
        util = Utilitis(driver)
        prod = ProductsPageFunc(driver)
        prod.click_products_btn()
        time.sleep(1)
        util.addBtn(True)
        form_stages = ["מוצר","מוצר - מידע נוסף","יחידות","פרטי משלוח","סיום"]
        web_form = prod.form_conntent()

        util.assertFunc(form_stages,list(web_form.values()))







