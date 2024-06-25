from utilities.Base import BaseClass

from pageobjects.LoginPage import LoginPage

from pageobjects.Invalid_Loginpage import Invalid_LoginPage


class Test_Invalid_LoginPage(BaseClass):

    def test_verify_invalid_loginpge(self):
        invalidloginpage = LoginPage(self.driver)
        self.waitforsometime()
        invalidloginpage.setusername("prasannna")
        invalidloginpage.setpassword("123456")
        self.waitforsometime()
        invalidloginpage.clickonloginbutton()
        self.waitforsometime()
        invalidloginpageerrormsg = Invalid_LoginPage(self.driver)
        self.waitforsometime()
        invalidloginpageerrormsg.verify_error_msg()
        self.waitforsometime()
