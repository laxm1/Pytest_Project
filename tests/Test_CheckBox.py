from pageobjects.CheckBox import CheckBox

from utilities.Base import BaseClass

class Test_CheckBox(BaseClass):

    def test_verify_checkbox_selected_or_not(self):
        checkbox = CheckBox(self.driver)
        self.waitforsometime()
        checkbox.clickoncheckbox()
