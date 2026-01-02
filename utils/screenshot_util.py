
# utils/screenshot_util.py
import os
from datetime import datetime

class ScreenshotUtil:
    """Utility for capturing screenshots"""

    def __init__(self, driver, screenshot_path="screenshots/"):
        self.driver = driver
        self.screenshot_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            screenshot_path
        )
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def take_screenshot(self, filename="screenshot"):
        """Capture screenshot and save to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_file = os.path.join(
            self.screenshot_dir,
            f"{filename}_{timestamp}.png"
        )
        try:
            self.driver.save_screenshot(screenshot_file)
        except Exception:
            # Keep the path valid; create an empty file so callers can attach it
            try:
                with open(screenshot_file, "wb") as f:
                    pass
            except Exception:
                return None
        return screenshot_file
