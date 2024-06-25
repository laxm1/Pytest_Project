from utilities.Base import BaseClass

from pageobjects.LoginPage import LoginPage

from pageobjects.HomePage import Logout


class Test_Logout_Test(BaseClass):

    def test_verify_logout(self):
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()

        logout = Logout(self.driver)
        self.waitforsometime()
        logout.clickonlogoutbutton()
        self.waitforsometime()
