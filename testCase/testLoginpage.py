
import pytest
from pageObject.login_page import LoginPage
from DataSet import test_data

@pytest.mark.usefixtures("browser_setup")
class TestLoginFeature:

    def test_login_ellen(self):
        self.login = LoginPage(self.driver)
        self.login.go_login_tab()
        self.login.go_to_login_to_application(test_data.uname,test_data.pwd)
        self.login.logout_from_application()
#login successfully or login fail msg should be seen ...assignmnet

