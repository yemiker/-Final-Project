import time
import pytest
from Managment.Web.Pages.Department_page import DepartmentPageFunc
from Managment.Web.Utils.utils import Utilitis
from Managment.Web.Base.BasePage import Base



@pytest.mark.usefixtures('connect_home_page')
class TestDepartment(Base):

    """Tests for departments UI"""
    def test_ui_for_department_screen(self):
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
        # Using the "assert" function
        print(add.ui_txt_for_page())
        util.assertFunc(add.ui_txt_for_page(),"הוספה\nייצוא\nמזהה\n\tשם\n\tתמונה\n\tתמונת רקע\n\tפעיל\n\tתאריך יצירה\n\nu6z3r13kkkv9cqk3\tוודקה\t\n\t\n\t✓\t\n07/02/21, 16:44\n\n461hdlknbycfhy\tנביעות\t\n\t\n\t✗\t\n10/04/21, 19:28\n\nu6z3r6pokm0lra0r\tקוניאק\t\n\t\n\t✓\t\n08/03/21, 15:10\n\nu6z3rgrckkzoqwou\tשוקולדים\t\n\t\n\t✓\t\n10/02/21, 19:06\n\npslidk0kp9nk6b0\tירוקו\t\n\t\n\t✓\t\n29/05/21, 14:10\n\nt4yw88klqifbu8\tבדיקה\t\n\t\n\t✓\t\n01/03/21, 13:39\n\n1k9pzmkz4i3awb\tקנאביס\t\n\t\n\t✓\t\n01/02/22, 21:15\n\nxfdpjewkz59964t\tבטון\t\n\t\n\t✓\t\n02/02/22, 09:55\n\n4jp555dl46ps70v\tfdgfd\t\n\t\n\t✓\t\n09/06/22, 10:44\n\n4jp555dl4birmvj\tyossi\t\n\t\n\t✓\t\n12/06/22, 19:27\n\n4jp555dl4cjmtpl\tסיגריות\t\n\t\n\t✓\t\n13/06/22, 12:39\n\n4jp555dl4cjpcbx\tטבק\t\n\t\n\t✓\t\n13/06/22, 12:41\n\n4jp555dl4cjqrn6\tטבק1\t\n\t\n\t✓\t\n13/06/22, 12:42\n\n4jp555dl4cjxrvq\tסבונים\t\n\t\n\t✓\t\n13/06/22, 12:47\n\n4jp555dl4ckigqp\tסבונים2\t\n\t\n\t✓\t\n13/06/22, 13:03\n\n4jp555dl4curhv3\tסבוני12\t\n\t\n\t✓\t\n13/06/22, 17:50\n\n4jp555dl4cvfr4h\tסבונים1\t\n\t\n\t✓\t\n13/06/22, 18:09\n\n4jp555dl4cvhva3\tסבונים11\t\n\t\n\t✓\t\n13/06/22, 18:11\n\n4jp555dl4cvmywv\tסבונים0\t\n\t\n\t✓\t\n13/06/22, 18:15\n\n4jp555dl4cvpe6x\tסבונים09\t\n\t\n\t✓\t\n13/06/22, 18:17\n\n4jp555dl4cw08c5\tסבונים111\t\n\t\n\t✓\t\n13/06/22, 18:25\n\n4jp555dl4d0ebo9\tסבוניםם\t\n\t\n\t✓\t\n13/06/22, 20:28\n\n4jp555dl4d5k2mx\tסבון\t\n\t\n\t✓\t\n13/06/22, 22:52\n\n4jp555dl4d9p4v1\tנייר\t\n\t\n\t✓\t\nאתמול, 00:48\n\n4jp555dl4d9qxox\tניירות\t\n\t\n\t✓\t\nאתמול, 00:50\n\n4jp555dl4dyosmy\tבישום\t\n\t\n\t✓\t\nאתמול, 12:28\n\n4jp555dl4e783xm\tשמפו\t\n\t\n\t✓\t\nאתמול, 16:27\n\n4jp555dl4e86937\tשמפו נגד קשקשים\t\n\t\n\t✓\t\nאתמול, 16:53\n\n4jp555dl4e8udjz\tקטל יד 2\t\n\t\n\t✓\t\nאתמול, 17:12\n\n4jp555dl4e8wz31\tקטל יד 3\t\n\t\n\t✓\t\nאתמול, 17:14\n\n4jp555dl4ec4jhs\tקטל יד 1\t\n\t\n\t✓\t\nאתמול, 18:44\n\n4jp555dl4ec8250\tתוספות\t\n\t\n\t✓\t\nאתמול, 18:47\n\n4jp555dl4ecdx3m\tתכשיטים\t\n\t\n\t✓\t\nאתמול, 18:51\n\n4jp555dl4ecg2y1\tשמפו פלוס\t\n\t\n\t✓\t\nאתמול, 18:53\n\n4jp555dl4ed3zhh\tדגנים\t\n\t\n\t✓\t\nאתמול, 19:12\n\n4jp555dl4edaxjx\tמוגגו\t\n\t\n\t✓\t\nאתמול, 19:17\n\n4jp555dl4eddrsc\tנעלים\t\n\t\n\t✓\t\nאתמול, 19:19\n\n4jp555dl4edh6hm\tמסכות\t\n\t\n\t✓\t\nאתמול, 19:22\nמציג \n לעמוד\nסה״כ: 38 שורות")


    def test_ui_for_department_screen_menuBar(self):
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
        # Using the "assert" function
        util.assertFunc(add.ui_txt_for_menu_bar(), "מחלקות")


    def test_ui_for_department_dropMenu_options(self):
        # Reboots the driver
        driver = self.driver
        # Definition of a variable that uses the methods of the Utils class
        util = Utilitis(driver)
        # Definition of a variable that uses the methods of the Department Page Func class
        add = DepartmentPageFunc(driver)
        # Using the click department button function
        add.click_department_button()
        time.sleep(3)
        util.addBtn(False)
        # sleep
        time.sleep(3)
        # Using the "assert" function
        util.assertFunc(add.ui_txt_for_dropMenu(1), "הוספה")
        util.assertFunc(add.ui_txt_for_dropMenu(2), "ייצוא")