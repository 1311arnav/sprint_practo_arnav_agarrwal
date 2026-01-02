
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader
from utils.logger import get_logger
from utils.screenshot_util import ScreenshotUtil

logger = get_logger("conftest")


@pytest.fixture(scope="session")
def config():
    """Fixture that matches tests' usage: config.get_value(<key>)"""
    return ConfigReader()


@pytest.fixture(scope="function")
def driver(request):
    cfg = ConfigReader()  # reads config/config.properties
    browser = (cfg.get_value("browser") or "").lower()
    base_url = cfg.get_value("base_url")

    logger.info(f"Starting test: {request.node.name}")
    logger.info(f"Browser selected: {browser}")

    if browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--log-level=3")
        driver = webdriver.Edge(
            service=EdgeService("resources/msedgedriver.exe"),
            options=options
        )

    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(base_url)

    yield driver

    logger.info(f"Tearing down test: {request.node.name}")
    driver.quit()


# ====================== Allure reports hookup ======================

import os  # keep imports local/minimal where needed

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            cfg = ConfigReader()
            out_dir = cfg.get_value("screenshot_path") or "screenshots/"

            # ✅ Instantiate and then take the screenshot
            su = ScreenshotUtil(driver, out_dir)
            screenshot_path = su.take_screenshot(item.name)

            logger.error(f"Test failed: {item.name}")
            logger.error(f"Screenshot saved at: {screenshot_path}")

            # Attach to Allure if file exists
            if screenshot_path and os.path.isfile(screenshot_path):
                with open(screenshot_path, "rb") as image:
                    allure.attach(
                        image.read(),
                        name=item.name,
                        attachment_type=allure.attachment_type.PNG
                    )
ALLURE_PATH = r"C:\Users\arnagarw\Downloads\allure-2.36.0\bin\allure.bat"  # adjust if needed


def pytest_unconfigure(config):
    import subprocess, os

    project_root = os.getcwd()
    results_dir = os.path.join(project_root, "reports")
    output_dir = os.path.join(project_root, "allure-results")

    if not os.path.exists(results_dir):
        logger.info("No Allure results found. Skipping.")
        return

    logger.info("Generating Allure HTML...")

    cmd = [
        ALLURE_PATH,
        "generate",
        results_dir,
        "-o",
        output_dir,
        "--clean"
    ]

    result = subprocess.run(cmd, shell=True)

    if result.returncode == 0:
        logger.info(
            "Allure HTML report generated successfully at %s",
            os.path.join(output_dir, "index.html")
        )
    else:
        logger.error("Allure HTML generation failed.")

# commands
# On Terminal : python -m http.server 9999
# On browser  :  http://localhost:9999/allure-reports/index.html