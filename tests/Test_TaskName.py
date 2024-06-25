from utilities.Base import BaseClass
from pageobjects.Tasks import Tasks
from pageobjects.LoginPage import LoginPage
from pageobjects.HomePage import Logout


class Test_Verify_TaskName(BaseClass):

    def test_verify_tasks(self):
        log = self.getLogger()
        log.info("Task Scrip Statrted")
        loginpage = LoginPage(self.driver)
        self.waitforsometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforsometime()
        loginpage.clickonloginbutton()

        task = Tasks(self.driver)
        task.clickonTask()
        self.waitforsometime()
        log.info(task.sendtextfiltertaskbyName("MangaKonga"))

        self.waitforsometime()
        task.clcikonapplyfilter()
        self.waitforsometime()

        logout = Logout(self.driver)
        self.waitforsometime()
        logout.clickonlogoutbutton()
        self.waitforsometime()
        log.info("Tasks scrip Executed Successfully..")
