from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class DoctorsPage(BasePage):
    """Doctors listing page object"""

    # Locators
    DOCTOR_CARD = (By.XPATH, "//div[contains(@class, 'doctor-card')]")
    NO_DOCTORS_MESSAGE = (By.XPATH, "//div[contains(text(), 'No doctors found')]")

    def is_doctors_displayed(self):
        """Check if doctors are displayed - returns boolean"""
        return self.is_element_present(self.DOCTOR_CARD)

    def get_doctor_count(self):
        """Get count of displayed doctors"""
        doctor_cards = self.driver.find_elements(*self.DOCTOR_CARD)
        return len(doctor_cards)

    def click_first_doctor(self):
        """Click on first doctor card"""
        assert self.is_doctors_displayed(), "Doctors should be displayed before clicking"
        doctor_cards = self.driver.find_elements(*self.DOCTOR_CARD)
        assert len(doctor_cards) > 0, "At least one doctor card should be available"
        doctor_cards[0].click()

    def is_no_doctors_message_displayed(self):
        """Check if 'No doctors found' message is displayed"""
        return self.is_element_present(self.NO_DOCTORS_MESSAGE)
