# Practo Test Automation Framework

A comprehensive Selenium-based test automation framework for testing Practo.com functionality with pytest, data-driven testing, and Allure reporting.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Test Cases](#test-cases)
- [Configuration](#configuration)
- [Reporting](#reporting)
- [Utilities](#utilities)

---

## 📖 Project Overview

This framework automates end-to-end testing of Practo.com features including:
- Doctor search and appointment booking
- Provider portal access
- Career portal navigation
- Appointment management
- Surgery/Care services
- Corporate partnerships

**Key Features:**
- ✅ Data-driven testing with Excel support
- ✅ Multiple parametrized test instances
- ✅ Strategic assertions (1 per 2-3 steps)
- ✅ Screenshot capture on test failure
- ✅ Detailed logging with step information
- ✅ Allure reporting integration
- ✅ Module-level function architecture (no class wrappers)

---

## 🏗️ Architecture

### Design Principles
- **Module-level functions**: Tests are standalone functions, not class methods
- **Centralized helpers**: All test data readers in `utils/test_data_reader.py`
- **Fixture injection**: Uses pytest fixtures (`driver`, `config`) instead of class methods
- **Explicit assertions**: Clear, purposeful assertions after logical test steps
- **Graceful error handling**: Optional steps wrapped in try/except, critical steps fail fast


## 📁 Project Structure

```
PractoTestingVS/
├── tests/
│   ├── test_appointment_booking.py      # Appointment booking end-to-end test
│   └── test_individual_features.py      # 6 feature tests (TC_02-TC_06)
│
├── pages/
│   ├── basepage.py                      # Base page object
│   ├── home_page.py
│   ├── doctors_page.py
│   ├── doctor_profile_page.py
│   ├── login_page.py
│   ├── appointments_page.py
│   ├── articles_page.py
│   └── __init__.py
│
├── utils/
│   ├── config_reader.py                 # Config file reader
│   ├── logger.py                        # Logging utility
│   ├── screenshot_util.py               # Screenshot capture
│   ├── excel_reader.py                  # Excel data reader
│   ├── test_data_reader.py              # Centralized test data helpers
│   └── __pycache__/
│
├── config/
│   └── config.properties                # Environment configuration
│
├── testdata/
│   ├── test_data_tc_02.xlsx
│   ├── test_data_tc_03.xlsx
│   ├── test_data_tc_04.xlsx
│   ├── test_data_tc_05.xlsx
│   ├── test_data_tc_06.xlsx
│   └── TestData_Master.xlsx
│
├── logs/                                # Test execution logs
├── screenshots/                         # Failure screenshots
├── allure-results/                      # Allure report data (JSON)
├── reports/                             # Report files
│
├── conftest.py                          # Pytest configuration & fixtures
├── pytest.ini                           # Pytest settings
├── requirements.txt                     # Python dependencies
└── README.md                            # This file
```

---

## 🧪 Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_appointment_booking.py -v
pytest tests/test_individual_features.py -v
```

### Run Specific Test Function
```bash
pytest tests/test_appointment_booking.py::test_doctor_appointment_booking -v
pytest tests/test_individual_features.py::test_tc_02_for_providers_menu -v
```

### Run Specific Parametrized Instance
```bash
# Run only row 2 of appointment booking test
pytest tests/test_appointment_booking.py::test_doctor_appointment_booking[2] -v

# Run only row 3 of TC_02
pytest tests/test_individual_features.py::test_tc_02_for_providers_menu[3] -v
```

### Run Tests with Markers
```bash
# Run only smoke tests
pytest -m smoke -v

# Run all tests with verbose output
pytest -v
```

### Run with Options
```bash
# Show print statements
pytest tests/ -v -s

# Stop on first failure
pytest tests/ -v -x

# Run with detailed logging
pytest tests/ -v -s --log-cli-level=DEBUG
```

---

## 🧬 Test Cases

### Test_Appointment_Booking (`test_doctor_appointment_booking`)
**Purpose:** End-to-end doctor appointment booking flow
**Parametrization:** 3 test instances (rows 2, 3, 4 from TestData_Master.xlsx)
**Steps:**
1. Navigate to home page
2. Login with credentials
3. Search for doctors by location
4. Apply filters (gender, fee, experience, availability)
5. Select time slot and book appointment
6. Verify booking confirmation

**Assertions:** 11 strategic assertions covering:
- Page navigation
- Login success
- Doctor list visibility
- Filter application
- Date/time selection
- Booking confirmation

---

### Test_Individual_Features (`test_individual_features.py`)

#### TC_02: For Providers Menu
**Purpose:** Verify provider portal and free demo form submission
**Parametrization:** 3 instances
**Steps:**
1. Click "For Providers" dropdown
2. Select "Practo Prime"
3. Click "Get free demo"
4. Fill provider form (category, name, mobile, city)
5. Submit form
**Assertions:** 8 assertions on navigation, form fill, and submission

#### TC_03: Careers Search
**Purpose:** Navigate to careers portal and filter by job category
**Parametrization:** 3 instances
**Steps:**
1. Navigate to home page
2. Click Find Doctors
3. Click Fortune
4. Navigate to Careers
5. Search and apply job category filter
6. Verify filter results
**Assertions:** 7 assertions on navigation and filter verification

#### TC_04: My Appointments
**Purpose:** Login and access appointment management
**Parametrization:** 3 instances
**Steps:**
1. Login with credentials
2. Access My Appointments
3. View appointment details
4. Cancel appointment
5. Verify cancellation
**Assertions:** 6 assertions on login, navigation, and cancellation

#### TC_05: Surgeries
**Purpose:** Navigate surgeries/care portal and select services
**Parametrization:** 3 instances
**Steps:**
1. Navigate to home page
2. Click Surgeries tab
3. Select department from test data
4. Select ailment/sub-type
5. Verify navigation
**Assertions:** Assertions on page load and content display

#### TC_06: For Corporates
**Purpose:** Access corporate partnership information
**Parametrization:** 3 instances
**Steps:**
1. Navigate to corporate page
2. Verify corporate benefits/information
3. Interact with corporate features
**Assertions:** Assertions on page content and features

---

## ⚙️ Configuration

### config.properties
Located in `config/config.properties`

```properties
# Browser selection
browser = chrome

# Base URL
base_url = https://www.practo.com

# Login credentials
email = your_email@example.com
password = your_password

# Timeouts
wait_timeout = 15

# File paths
screenshot_path = screenshots/
log_path = logs/
```

### pytest.ini
Located in `pytest.ini`

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    smoke: smoke tests
    regression: regression tests

addopts = --alluredir=allure-results -v
```

---

## 📊 Reporting

### Allure Reporting

**View Allure Report:**
```bash
# Generate and open interactive report
allure serve allure-results

# Generate static HTML report
allure generate allure-results -o allure-report
# Then open: allure-report/index.html
```

**Report Contains:**
- Test execution summary (passed/failed)
- Step-by-step test details
- Failure screenshots
- Test duration and timeline
- Error logs and messages
- Test history trends

### Log Files
Detailed logs saved in `logs/` directory:
- One log file per test run
- Contains step information
- Includes assertion details
- Timestamp and duration info

---

## 🛠️ Utilities

### Logger (`utils/logger.py`)
```python
from utils.logger import get_logger
logger = get_logger("test_name")
logger.info("Step passed")
logger.warning("Warning message")
logger.error("Error occurred")
```

### Screenshot Capture (`utils/screenshot_util.py`)
```python
from utils.screenshot_util import ScreenshotUtil
screenshot_util = ScreenshotUtil(driver)
screenshot_path = screenshot_util.capture_screenshot("test_name")
```

### Test Data Reader (`utils/test_data_reader.py`)
```python
from utils.test_data_reader import get_all_test_rows, get_test_data_by_row

# Get all row numbers for parametrization
rows = get_all_test_rows()

# Get data for specific row
data = get_test_data_by_row(row_number)
print(data.get('Location'))
```

### Config Reader (`utils/config_reader.py`)
```python
from utils.config_reader import ConfigReader
config = ConfigReader()
browser = config.get_value("browser")
base_url = config.get_value("base_url")
```

---

