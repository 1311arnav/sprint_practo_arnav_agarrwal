from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class BasePage:
    """Base class for all page objects with core interaction methods"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    def click_element(self, locator):
        """Click on element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Enter text in element with clear first"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from element"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def is_element_present(self, locator):
        """Check if element is present - returns boolean"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def is_element_visible(self, locator):
        """Check if element is visible - returns boolean"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_page_title(self):
        """Get current page title"""
        return self.driver.title

    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url

    def navigate_to_url(self, url):
        """Navigate to specified URL"""
        self.driver.get(url)
