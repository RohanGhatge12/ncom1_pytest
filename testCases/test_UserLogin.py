import time

from selenium import webdriver

from pageObjects.LoginPage import LoginClass
from utilities.readconfigfile import Readconfig


class Test_Login:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()

    def test_verify_url_001(self, setup):
        self.driver = setup
        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_fail.png")
            assert False

    def test_user_login_002(self, setup):
        self.driver = setup
        self.lp = LoginClass(self.driver)
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login()
        if self.lp.Verify_Login_Stauts() == "Login Pass":
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_pass.png")
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_fail.png")
            assert False

# pytest -v -n=2 --html=HtmlReports/myreport.html\

# test_emp_add
# test_emp_edit
# test_emp_search
#
# -k test_emp
