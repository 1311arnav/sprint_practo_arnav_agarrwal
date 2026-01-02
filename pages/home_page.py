from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.basepage import BasePage
import time


class HomePage(BasePage):
    """Home page object for Practo application"""

    # Locators
    LOGIN_SIGNUP_BTN = (By.XPATH,
                        "//button[contains(text(), 'Sign up')] | //button[contains(text(), 'Login')] | //a[contains(text(), 'Sign up')]")
    FIND_DOCTORS_BTN = (By.XPATH, "//a[contains(text(), 'Find Doctors')] | //div[contains(text(), 'Find Doctors')]")
    SEE_ALL_ARTICLES_BTN = (By.XPATH, "//a[contains(text(), 'see all')] | //a[contains(text(), 'See all')]")
    LOCATION_INPUT = (By.XPATH,
                      "//input[@placeholder='Enter city or locality'] | //input[contains(@placeholder, 'city')] | //input[contains(@placeholder, 'location')]")
    DOCTOR_TYPE_DROPDOWN = (By.XPATH,
                            "//input[@placeholder='Select Speciality'] | //input[contains(@placeholder, 'Speciality')] | //input[contains(@placeholder, 'Doctor')]")
    SEARCH_BTN = (By.XPATH,
                  "//button[contains(text(), 'Search')] | //button[@type='submit'] | //button[contains(@class, 'search')]")

    def open_home_page(self, base_url):
        """Open home page and verify navigation"""
        assert base_url, "Base URL should not be empty"
        self.navigate_to_url(base_url)
        time.sleep(2)
        current_url = self.get_current_url()
        assert current_url and "practo" in current_url.lower(), "Should navigate to Practo home page"

    def _click_element_with_fallback(self, primary_locator, fallback_xpath):
        """Click element with fallback XPath"""
        try:
            self.click_element(primary_locator)
        except:
            element = self.driver.find_element(By.XPATH, fallback_xpath)
            element.click()

    def click_login_signup(self):
        """Click on login/signup button"""
        self._click_element_with_fallback(
            self.LOGIN_SIGNUP_BTN,
            "//a[contains(text(), 'Sign up')] | //button[contains(@class, 'signup')]"
        )
        time.sleep(1)

    def click_find_doctors(self):
        """Click on Find Doctors button"""
        self._click_element_with_fallback(
            self.FIND_DOCTORS_BTN,
            "//a[contains(@href, 'search')]"
        )
        time.sleep(1)

    def click_see_all_articles(self):
        """Click on See All Articles button"""
        self._click_element_with_fallback(
            self.SEE_ALL_ARTICLES_BTN,
            "//a[contains(text(), 'articles')]"
        )
        time.sleep(1)

    def _find_input_by_placeholder(self, placeholder_keywords):
        """Find input element by placeholder keywords"""
        try:
            if len(placeholder_keywords) == 1:
                element = self.driver.find_element(By.XPATH,
                                                   f"//input[contains(@placeholder, '{placeholder_keywords[0]}')]")
                return element
        except:
            pass

        all_inputs = self.driver.find_elements(By.TAG_NAME, "input")
        for inp in all_inputs:
            placeholder = inp.get_attribute("placeholder")
            if placeholder and any(kw.lower() in placeholder.lower() for kw in placeholder_keywords):
                return inp

        raise Exception(f"Input element not found for keywords: {placeholder_keywords}")

    def _select_from_dropdown_list(self, input_element, value, arrow_downs=1, wait_before=0.5, wait_after=0.8):
        """
        Generic dropdown/radio button selection logic
        Simulates selecting from a list of options
        """
        assert value, f"Value should not be empty"
        input_element.clear()
        input_element.send_keys(value)
        time.sleep(wait_before)

        # Wait for dropdown/list to appear
        time.sleep(0.3)

        # Press arrow down to navigate through options
        for _ in range(arrow_downs):
            input_element.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)

        # Select the option
        input_element.send_keys(Keys.ENTER)
        time.sleep(wait_after)

    def _select_radio_option(self, label_text):
        """
        Select a radio button by its associated label text
        Practo uses radio buttons for filters
        """
        try:
            # Try to find radio button by label
            radio_xpath = f"//label[contains(text(), '{label_text}')]/preceding-sibling::input[@type='radio'] | //input[@type='radio' and following-sibling::label[contains(text(), '{label_text}')]]"
            radio_button = self.driver.find_element(By.XPATH, radio_xpath)
            radio_button.click()
            time.sleep(0.5)
        except:
            # Try alternative: find by exact match
            alt_xpath = f"//span[contains(text(), '{label_text}')]/ancestor::label/input[@type='radio'] | //input[@type='radio' and @value='{label_text}']"
            radio_button = self.driver.find_element(By.XPATH, alt_xpath)
            radio_button.click()
            time.sleep(0.5)

    def enter_location(self, location):
        """Enter location and select from dropdown list"""
        location_input = self._find_input_by_placeholder(["city", "location"])
        self._select_from_dropdown_list(location_input, location, arrow_downs=2, wait_before=0.5, wait_after=0.8)

    def select_doctor_type(self, doctor_type):
        """Select doctor type from dropdown list"""
        type_input = self._find_input_by_placeholder(["speciality", "doctor"])
        self._select_from_dropdown_list(type_input, doctor_type, arrow_downs=1, wait_before=0.6, wait_after=0.6)

    def click_search(self):
        """Click search button"""
        try:
            self.click_element(self.SEARCH_BTN)
        except:
            search_input = self.driver.find_element(By.TAG_NAME, "input")
            search_input.send_keys(Keys.ENTER)
        time.sleep(2.5)

    def select_fee_filter(self, fee_range):
        """
        Select fee filter - Practo uses radio buttons for filters
        Example: "0–₹500" or "₹500-1000"
        """
        self._select_radio_option(fee_range)

    def select_experience_filter(self, experience):
        """
        Select experience filter - Practo uses radio buttons
        Example: "5+ years of experience"
        """
        self._select_radio_option(experience)

    def select_availability_filter(self, availability):
        """
        Select availability filter - Practo uses radio buttons
        Example: "Today" or "Tomorrow"
        """
        self._select_radio_option(availability)
