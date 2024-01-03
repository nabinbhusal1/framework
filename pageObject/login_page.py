import time

from pageObject.basePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    loginTab = (By.XPATH, "//div[@id='app']//self::div[@class='c-header__right']/button")
    registerNowButton = (By.XPATH, "//a[contains(text(),'Register now')]")
    forgotPassword = (By.XPATH, "//a[contains(text(),'Forgot password?')]")

    usernameXpath = (By.XPATH, "//input[@id='Input_Username']")
    passwordXpath = (By.XPATH, "//input[@id='Input_Password']")
    toggleXpath = (By.XPATH, "//form[@id='signin-form']//div[3]/label/i")

    loginButton = (By.XPATH, "//form[@id='signin-form']//self::button")
    bookCover = (
        By.XPATH, "//ul[starts-with(@class,'c-projects')]/li[1]/div//self::div[@class='c-book c-book--default']")
    timeLine = (By.XPATH,
                "//ul[starts-with(@class,'c-projects')]/li[1]/div//self::div[@class='o-flex']//self::button[starts-with(@class,'c-project__btn c-btn c-btn- c-btn')]")

    logout = (By.XPATH, "//span[contains(text(),'arrow_drop_down')]")
    logout1 = (By.XPATH, "//div[contains(text(),'Logout')]")
    loginTab2 = (By.XPATH, "(//button[contains(text(),' Login ')])[2]")

    def go_login_tab(self):
        self.wait_for(self.loginTab)
        self.click(self.loginTab)
        self.wait_for(self.registerNowButton)
        self.wait_for(self.forgotPassword)

    def go_to_login_to_application(self, username, password):
        self.send_keys(self.usernameXpath, username)
        self.send_keys(self.passwordXpath, password)
        self.click(self.toggleXpath)
        self.click(self.loginButton)
        self.wait_for(self.bookCover)
        time.sleep(5)

    def logout_from_application(self):
        self.wait_for(self.logout)
        self.click(self.logout)
        self.wait_for(self.logout1)
        self.click(self.logout1)
        self.wait_for(self.loginTab2)
