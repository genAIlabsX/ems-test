# Employee Management System Test Automation Guide

## Overview

This test automation framework provides comprehensive testing for the Django-based Employee Management System using:

1. **Selenium WebDriver with Python** - For browser-based UI testing
2. **UFT (Unified Functional Testing)** - For enterprise-level functional testing

The framework follows the Page Object Model (POM) design pattern, which provides a clear separation between test code and page-specific code, making tests more maintainable and reusable.

## Directory Structure

```
ems-test/
├── README.md                      # Project overview
├── requirements.txt               # Python dependencies
├── run_tests.ps1                  # PowerShell script to run tests
├── run_selenium_tests.ps1         # Alternative script to run Selenium tests
├── ui_actions_catalog.md          # Catalog of all UI actions in the application
├── selenium_tests/
│   ├── conftest.py                # Pytest configuration and fixtures
│   ├── page_objects/              # Page Object Model classes
│   │   ├── base_page.py           # Base class for all page objects
│   │   ├── home_page.py           # Home page object
│   │   ├── employee_list_page.py  # Employee list page object
│   │   ├── employee_form_page.py  # Employee form page object
│   │   ├── employee_delete_page.py # Employee delete page object
│   │   ├── department_list_page.py # Department list page object
│   │   ├── department_form_page.py # Department form page object
│   │   └── department_delete_page.py # Department delete page object
│   ├── test_data/                 # Test data files
│   │   ├── employees.csv          # Test employee data
│   │   ├── departments.csv        # Test department data
│   │   └── test_data_loader.py    # Utility to load and generate test data
│   └── tests/                     # Test scripts
│       ├── base_test.py           # Base class for all test classes
│       ├── test_add_employee.py   # Tests for adding employees
│       ├── test_view_employees.py # Tests for viewing and filtering employees
│       ├── test_form_validation.py # Tests for form validation
│       └── test_navigation.py     # Tests for navigation between pages
└── uft_scripts/                   # UFT test scripts
    ├── AddEmployeeTest.vbs        # Test for adding employees
    ├── ViewEmployeesTest.vbs      # Test for viewing and filtering employees
    ├── FormValidationTest.vbs     # Test for form validation
    └── NavigationTest.vbs         # Test for navigation between pages
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- Micro Focus UFT One (for UFT scripts)
- Django application running at http://127.0.0.1:8000

### Setting Up the Python Environment

1. Navigate to the project directory:

   ```powershell
   cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems-test"
   ```

2. Create a virtual environment and install dependencies:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

### Running the Django Application

Before running tests, make sure the Django application is running:

```powershell
cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems"
python manage.py runserver
```

## Running the Tests

### Using the Automated Script

The easiest way to run the tests is using the provided PowerShell script:

```powershell
cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems-test"
.\run_tests.ps1
```

This script will:
1. Check if the Django server is running
2. Offer to start it if it's not running
3. Set up the virtual environment if needed
4. Run the tests with options for parallel execution and HTML reporting

### Running Specific Tests

To run specific test files:

```powershell
cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems-test"
.\venv\Scripts\Activate.ps1
python -m pytest selenium_tests\tests\test_add_employee.py -v
```

To run tests in parallel (faster execution):

```powershell
python -m pytest selenium_tests\tests -v -n 2
```

To generate an HTML report:

```powershell
python -m pytest selenium_tests\tests -v --html=report.html --self-contained-html
```

### Running UFT Scripts

1. Open UFT One
2. Load the script from the uft_scripts folder (e.g., AddEmployeeTest.vbs)
3. Make sure the Django application is running at http://127.0.0.1:8000
4. Run the script from UFT One

## Test Cases Overview

### 1. Add New Employee Tests

- **test_add_valid_employee**: Verify that a new employee can be added with valid data
- **test_add_employee_missing_required_fields**: Test form validation for required fields
- **test_add_employee_invalid_email**: Test form validation for invalid email format
- **test_add_employee_negative_salary**: Test form validation for negative salary

### 2. View Employees Tests

- **test_view_all_employees**: Verify that the employee list is displayed correctly
- **test_search_employee**: Test searching for employees by name, email, or department
- **test_filter_by_status**: Test filtering employees by active/inactive status
- **test_filter_by_department**: Test filtering employees by department
- **test_export_to_csv**: Test exporting employee data to CSV

### 3. Form Validation Tests

- **test_employee_form_required_fields**: Test validation of required fields in employee form
- **test_employee_form_email_validation**: Test email format validation in employee form
- **test_employee_form_salary_validation**: Test salary validation in employee form
- **test_department_form_required_fields**: Test validation of required fields in department form
- **test_employee_form_unique_email**: Test validation of unique email in employee form
- **test_department_form_unique_name**: Test validation of unique name in department form

### 4. Navigation Tests

- **test_navigation_from_home**: Test navigation from home page to other pages
- **test_navigation_between_employee_pages**: Test navigation between employee-related pages
- **test_navigation_between_department_pages**: Test navigation between department-related pages
- **test_navigation_using_browser_controls**: Test navigation using browser back/forward buttons

## Extending the Framework

### Adding New Page Objects

1. Create a new page object class in the `selenium_tests/page_objects/` directory
2. Extend the `BasePage` class
3. Define locators at the class level
4. Implement page-specific methods
5. Update the `__init__.py` file to import the new class

### Adding New Tests

1. Create a new test class in the `selenium_tests/tests/` directory
2. Extend the `BaseTest` class
3. Implement test methods using the page objects
4. Follow the naming convention: `test_*.py` for files and `test_*` for methods

### Adding New Test Data

1. Add new data in the `selenium_tests/test_data/` directory
2. Update the `test_data_loader.py` file to load and generate the new data

## Best Practices

1. **Maintain Page Objects**: Update page objects when the UI changes
2. **Keep Tests Independent**: Each test should be able to run independently
3. **Use Appropriate Waits**: Use explicit waits instead of implicit waits or sleeps
4. **Handle Test Data Properly**: Use unique test data for each test run
5. **Clean Up After Tests**: Restore the application state after each test
6. **Use Descriptive Test Names**: Test names should describe what they are testing
7. **Add Assertions**: Each test should have at least one assertion

## Troubleshooting

### Common Issues

1. **WebDriver Exception**: Make sure you have the correct version of Chrome and chromedriver
2. **Connection Refused**: Ensure the Django application is running at http://127.0.0.1:8000
3. **Element Not Found**: Check if the locator is correct and the element is present
4. **Test Data Issues**: Ensure test data is unique and meets validation requirements

### Getting Help

If you encounter any issues, please check:
1. The error message in the test output
2. The logs in the Django application console
3. The browser console for JavaScript errors
