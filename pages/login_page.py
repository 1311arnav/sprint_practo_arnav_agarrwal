from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class LoginPage(BasePage):
    """Login page object for Practo application"""

    # Locators
    EMAIL_INPUT = (By.XPATH, "//input[@id='email'] | //input[@type='email'] | //input[contains(@placeholder, 'Email')]")
    PASSWORD_INPUT = (By.XPATH,
                      "//input[@id='password'] | //input[@type='password'] | //input[contains(@placeholder, 'Password')]")
    LOGIN_BTN = (By.XPATH,
                 "//button[contains(text(), 'Login')] | //button[contains(text(), 'login')] | //button[@type='submit']")
    SIGNUP_LINK = (By.XPATH, "//a[contains(text(), 'Sign up')] | //a[contains(text(), 'Signup')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error')] | //span[contains(@class, 'error')]")

    def enter_email(self, email):
        """Enter email"""
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enter password"""
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click login button"""
        self.click_element(self.LOGIN_BTN)

    def login(self, email, password):
        """Perform login"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def click_signup(self):
        """Click signup link"""
        self.click_element(self.SIGNUP_LINK)

    def get_error_message(self):
        """Get error message if present"""
        return self.get_text(self.ERROR_MESSAGE) if self.is_element_present(self.ERROR_MESSAGE) else None
