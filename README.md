# Employee Management System Test Automation

This project contains automated tests for the Django-based Employee Management System using:
1. Selenium WebDriver with Python
2. UFT (Unified Functional Testing) with VBScript

## Directory Structure

```
ems-test/
├── README.md
├── requirements.txt
├── selenium_tests/
│   ├── page_objects/    # Page Object Model classes
│   ├── test_data/       # Test data files (CSV, JSON)
│   └── tests/           # Test scripts
└── uft_scripts/         # UFT test scripts
```

## Setup Instructions

### Selenium Tests Setup

1. Install Python dependencies:

```powershell
cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems-test"
python -m pip install -r requirements.txt
```

2. Run the Django application:

```powershell
cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems"
python manage.py runserver
```

3. Run the Selenium tests:

```powershell
cd "c:\Users\fikowali\Documents\Workspace\GH Copilot Hackathon\ems-test"
python -m pytest selenium_tests\tests -v
```

### UFT Tests Setup

1. Open UFT One (Unified Functional Testing)
2. Open the script from the uft_scripts folder
3. Configure the application URL in the script
4. Run the test

## Test Scenarios

The automated tests cover the following scenarios:

1. Add New Employee
   - Fill in and submit the employee form
   - Verify form validation
   - Verify successful employee creation

2. View All Employees
   - Verify employee list display
   - Test filtering and search functionality
   - Verify CSV export

3. Form Validation
   - Test required fields validation
   - Test field format validation (email, salary)
   - Test validation error messages

4. Navigation Between Pages
   - Test navigation between employee and department pages
   - Verify links and UI elements

## GitHub Copilot Prompts Used

- Generate automatic test for Django employee management application
- Create Page Object Model for Django employee application
- Write Selenium test for adding a new employee
- Write UFT test script for employee management system

## Challenges Faced

- Setting up the proper environment for both Selenium and UFT tests
- Handling dynamic elements in the Django application
- Coordinating test data between different test scenarios
- Cross-browser compatibility issues
