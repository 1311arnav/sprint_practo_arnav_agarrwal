from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class DoctorProfilePage(BasePage):
    """Doctor profile page object"""

    # Locators
    DOCTOR_NAME = (By.XPATH, "//h1[contains(@class, 'doctor-name')]")
    DOCTOR_PHOTO = (By.XPATH, "//img[contains(@class, 'doctor-photo')]")
    OVERVIEW_TAB = (By.XPATH, "//a[contains(text(), 'Overview')]")
    REVIEWS_TAB = (By.XPATH,
                   "//a[contains(text(), 'Reviews')] | //button[contains(text(), 'Reviews')] | //span[contains(text(), 'Reviews')]")
    LOCATIONS_TAB = (By.XPATH, "//a[contains(text(), 'Locations')]")
    RATING = (By.XPATH, "//div[contains(@class, 'rating')]")
    CLINIC_ADDRESS = (By.XPATH, "//div[contains(@class, 'clinic-address')]")
    BOOK_APPOINTMENT_BTN = (By.XPATH,
                            "//button[contains(text(), 'Book Appointment')] | //button[contains(text(), 'Book')] | //button[@class='book-btn']")

    def is_doctor_name_displayed(self):
        """Check if doctor name is displayed"""
        return self.is_element_present(self.DOCTOR_NAME)

    def is_doctor_photo_displayed(self):
        """Check if doctor photo is displayed"""
        return self.is_element_present(self.DOCTOR_PHOTO)

    def is_overview_tab_present(self):
        """Check if Overview tab is present"""
        return self.is_element_present(self.OVERVIEW_TAB)

    def is_reviews_tab_present(self):
        """Check if Reviews tab is present"""
        return self.is_element_present(self.REVIEWS_TAB)

    def is_locations_tab_present(self):
        """Check if Locations tab is present"""
        return self.is_element_present(self.LOCATIONS_TAB)

    def click_reviews_tab(self):
        """Click on Reviews tab"""
        self.click_element(self.REVIEWS_TAB)

    def click_locations_tab(self):
        """Click on Locations tab"""
        self.click_element(self.LOCATIONS_TAB)

    def is_rating_displayed(self):
        """Check if rating is displayed"""
        return self.is_element_present(self.RATING)

    def is_clinic_address_displayed(self):
        """Check if clinic address is displayed"""
        return self.is_element_present(self.CLINIC_ADDRESS)

    def click_book_appointment(self):
        """Click on Book Appointment button"""
        self.click_element(self.BOOK_APPOINTMENT_BTN)
