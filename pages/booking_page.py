from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class BookingPage(BasePage):
    """Appointment booking page object"""

    # Locators
    DATE_PICKER = (By.XPATH, "//input[@type='date']")
    TIME_SLOT = (By.XPATH, "//div[contains(@class, 'time-slot')]")
    AVAILABLE_SLOTS = (By.XPATH, "//button[contains(@class, 'available')]")
    BOOK_BTN = (By.XPATH, "//button[contains(text(), 'Book')]")
    CONFIRM_BTN = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'No slots available')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'success')]")

    def select_date(self, date):
        """Select date"""
        self.send_keys(self.DATE_PICKER, date)

    def select_time_slot(self, time_slot):
        """Select time slot"""
        slot_locator = (By.XPATH, f"//button[contains(text(), '{time_slot}')]")
        self.click_element(slot_locator)

    def is_time_slots_available(self):
        """Check if time slots are available"""
        return self.is_element_present(self.AVAILABLE_SLOTS)

    def click_book(self):
        """Click on Book button"""
        self.click_element(self.BOOK_BTN)

    def click_confirm(self):
        """Click on Confirm button"""
        self.click_element(self.CONFIRM_BTN)

    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_present(self.ERROR_MESSAGE)

    def is_success_message_displayed(self):
        """Check if success message is displayed"""
        return self.is_element_present(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        """Get error message"""
        return self.get_text(self.ERROR_MESSAGE) if self.is_element_present(self.ERROR_MESSAGE) else None
