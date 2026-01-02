from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class AppointmentsPage(BasePage):
    """My Appointments page object"""

    # Locators
    APPOINTMENT_CARD = (By.XPATH, "//div[contains(@class, 'appointment-card')]")
    RESCHEDULE_BTN = (By.XPATH, "//button[contains(text(), 'Reschedule')]")
    CANCEL_BTN = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    CONFIRM_BTN = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    DATE_PICKER = (By.XPATH, "//input[@type='date']")
    TIME_SLOT = (By.XPATH, "//div[contains(@class, 'time-slot')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'success-message')]")
    CONFIRMATION_MESSAGE = (By.XPATH, "//div[contains(text(), 'Confirmation')]")

    def is_appointments_listed(self):
        """Check if appointments are listed"""
        return self.is_element_present(self.APPOINTMENT_CARD)

    def click_reschedule(self):
        """Click on Reschedule button"""
        self.click_element(self.RESCHEDULE_BTN)

    def select_date(self, date):
        """Select date for rescheduling"""
        self.send_keys(self.DATE_PICKER, date)

    def select_time_slot(self):
        """Select time slot"""
        time_slots = self.driver.find_elements(*self.TIME_SLOT)
        if time_slots:
            time_slots[0].click()

    def click_confirm(self):
        """Click on Confirm button"""
        self.click_element(self.CONFIRM_BTN)

    def click_cancel(self):
        """Click on Cancel button"""
        self.click_element(self.CANCEL_BTN)

    def get_success_message(self):
        """Get success message"""
        return self.get_text(self.SUCCESS_MESSAGE) if self.is_element_present(self.SUCCESS_MESSAGE) else None

    def is_confirmation_message_displayed(self):
        """Check if confirmation message is displayed"""
        return self.is_element_present(self.CONFIRMATION_MESSAGE)
