# Extending the Test Framework

This document provides guidance on how to extend the Employee Management System test automation framework to cover new features and scenarios.

## Adding New Page Objects

When the application gets new pages or significant UI changes, you'll need to create or update page objects.

### Steps to Add a New Page Object:

1. **Create a new file** in the `selenium_tests/page_objects/` directory, following the naming convention `*_page.py`

2. **Import the BasePage class** and other necessary modules:

    ```python
    from selenium.webdriver.common.by import By
    from .base_page import BasePage
    ```

3. **Define your page class** by extending BasePage:

    ```python
    class NewFeaturePage(BasePage):
        """
        Page object for the new feature page.
        """
        
        # Locators - define all elements you'll interact with
        PAGE_HEADER = (By.XPATH, "//h2[text()='New Feature']")
        SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
        
        def __init__(self, driver):
            super().__init__(driver)
        
        # Add methods for page-specific actions
        def perform_action(self, param):
            """
            Perform a specific action on the page.
            
            Args:
                param: Parameter for the action
                
            Returns:
                self or another page object if navigation occurs
            """
            self.input_text(self.SOME_INPUT, param)
            self.click(self.SUBMIT_BUTTON)
            
            # If this action navigates to another page, return that page object
            from .another_page import AnotherPage
            return AnotherPage(self.driver)
    ```

4. **Update the `__init__.py`** file in the page_objects directory to import your new class:

    ```python
    from .new_feature_page import NewFeaturePage
    ```

## Adding New Test Cases

### Steps to Add a New Test Case:

1. **Create a new test file** in the `selenium_tests/tests/` directory, following the naming convention `test_*.py`

2. **Import the BaseTest class** and other necessary modules:

    ```python
    import pytest
    from selenium_tests.tests.base_test import BaseTest
    ```

3. **Define your test class** by extending BaseTest:

    ```python
    class TestNewFeature(BaseTest):
        """
        Tests for the new feature.
        """
        
        def test_new_feature_functionality(self):
            """Test the main functionality of the new feature."""
            # Navigate to the page with the new feature
            home_page = self.home_page
            some_page = home_page.navigate_to_some_page()
            
            # Perform actions and assertions
            result = some_page.perform_action("test_data")
            assert result.is_success_message_displayed(), "Success message not displayed"
    ```

4. **Use test data** from the test_data_loader or create specific test data:

    ```python
    def test_new_feature_with_data(self):
        """Test the new feature with different data sets."""
        # Get test data
        test_data = self.test_data_loader.get_specific_data()
        
        # Navigate and perform test
        new_feature_page = self.home_page.navigate_to_new_feature()
        
        for data_item in test_data:
            result = new_feature_page.perform_action(data_item)
            assert result.is_success_message_displayed(), f"Failed with data: {data_item}"
    ```

## Adding New Test Data

### Steps to Add New Test Data:

1. **Create a new CSV file** (if needed) in the `selenium_tests/test_data/` directory

2. **Update the test_data_loader.py** file to load and process the new data:

    ```python
    @staticmethod
    def get_new_feature_data():
        """
        Get test data for the new feature.
        
        Returns:
            list: List of test data dictionaries
        """
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                'test_data', 'new_feature_data.csv')
        return TestDataLoader.load_csv_data(file_path)
    
    @staticmethod
    def generate_random_new_feature_data():
        """
        Generate random data for testing the new feature.
        
        Returns:
            dict: Random test data
        """
        return {
            "field1": f"Value {random.randint(1000, 9999)}",
            "field2": random.choice(["Option A", "Option B", "Option C"]),
            "field3": random.uniform(1.0, 100.0)
        }
    ```

## Creating UFT Scripts for New Features

### Steps to Create a New UFT Script:

1. **Create a new VBScript file** in the `uft_scripts/` directory

2. **Define the basic structure**:

    ```vbscript
    ' UFT Test Script for Employee Management System
    ' Test Case: New Feature
    
    Option Explicit
    
    ' Application URL
    Const AppURL = "http://127.0.0.1:8000/"
    
    ' Test Data
    Dim TestData1, TestData2
    TestData1 = "Value " & Day(Now) & Hour(Now) & Minute(Now)
    TestData2 = "12345"
    
    ' ===== Main Test Script =====
    ' Launch browser and navigate to application
    SystemUtil.Run "chrome.exe", AppURL
    
    ' Wait for page to load
    Wait 3
    
    ' Navigate to feature page
    Browser("title:=Employee Management System").Page("title:=Employee Management System").Link("text:=Feature").Click
    Wait 2
    
    ' Perform test actions
    Browser("title:=New Feature").Page("title:=New Feature").WebEdit("name:=field1").Set TestData1
    Browser("title:=New Feature").Page("title:=New Feature").WebList("name:=field2").Select "Option A"
    Browser("title:=New Feature").Page("title:=New Feature").WebEdit("name:=field3").Set TestData2
    
    ' Submit the form
    Browser("title:=New Feature").Page("title:=New Feature").WebButton("type:=submit").Click
    Wait 2
    
    ' Verify results
    If Browser("title:=Results").Page("title:=Results").WebElement("innertext:=Success").Exist(5) Then
        Reporter.ReportEvent micPass, "New Feature Test", "Feature worked successfully"
    Else
        Reporter.ReportEvent micFail, "New Feature Test", "Feature failed"
    End If
    
    ' Close the browser
    SystemUtil.CloseProcessByName "chrome.exe"
    ```

## Testing Best Practices

1. **One Test, One Scenario**: Each test should focus on testing one specific scenario or functionality

2. **Independent Tests**: Tests should be independent of each other and can run in any order

3. **Clear Assertions**: Each test should have clear, meaningful assertions

4. **Readable Test Names**: Use descriptive names for test methods that explain what they're testing

5. **Effective Waits**: Use explicit waits instead of fixed sleeps

6. **Error Handling**: Include proper error handling and logging in tests

7. **Test Data Management**: Keep test data separate from test logic

8. **Test Clean-up**: Clean up any test data or state after tests run

## Example: Adding a New Feature Test

Let's say the application gets a new feature for bulk employee import. Here's how to test it:

1. **Create a new page object** (`bulk_import_page.py`):

    ```python
    from selenium.webdriver.common.by import By
    from .base_page import BasePage
    
    class BulkImportPage(BasePage):
        """
        Page object for the bulk employee import page.
        """
        
        # Locators
        PAGE_HEADER = (By.XPATH, "//h2[text()='Bulk Import Employees']")
        FILE_INPUT = (By.ID, "id_import_file")
        SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
        SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
        ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")
        
        def __init__(self, driver):
            super().__init__(driver)
        
        def upload_file(self, file_path):
            """
            Upload a file for bulk import.
            
            Args:
                file_path (str): Path to the file to upload
                
            Returns:
                self: The current page
            """
            self.find_element(self.FILE_INPUT).send_keys(file_path)
            return self
        
        def submit_import(self):
            """
            Submit the import form.
            
            Returns:
                EmployeeListPage: If import succeeds
                self: If there are errors
            """
            self.click(self.SUBMIT_BUTTON)
            
            # Check if we were redirected to the employee list page
            if "employees/" in self.get_current_url() and not "/import/" in self.get_current_url():
                from .employee_list_page import EmployeeListPage
                return EmployeeListPage(self.driver)
            
            # Still on the import page (errors)
            return self
        
        def is_success_message_displayed(self):
            """
            Check if success message is displayed.
            
            Returns:
                bool: True if success message is displayed
            """
            return self.is_element_present(self.SUCCESS_MESSAGE)
        
        def is_error_message_displayed(self):
            """
            Check if error message is displayed.
            
            Returns:
                bool: True if error message is displayed
            """
            return self.is_element_present(self.ERROR_MESSAGE)
        
        def get_error_message(self):
            """
            Get the error message text.
            
            Returns:
                str: Error message text
            """
            if self.is_error_message_displayed():
                return self.get_text(self.ERROR_MESSAGE)
            return ""
    ```

2. **Create test data file** (`bulk_import_valid.csv`):

    ```csv
    name,email,department,salary,status
    John Import,john.import@example.com,Engineering,75000,Active
    Jane Import,jane.import@example.com,Marketing,65000,Active
    ```

3. **Create test data file** (`bulk_import_invalid.csv`):

    ```csv
    name,email,department,salary,status
    Invalid User,not-an-email,Unknown,negative,-1000,Unknown
    ```

4. **Create a test file** (`test_bulk_import.py`):

    ```python
    import os
    import pytest
    from selenium_tests.tests.base_test import BaseTest
    
    class TestBulkImport(BaseTest):
        """
        Tests for the bulk employee import feature.
        """
        
        def setup_method(self, method):
            """Setup method that runs before each test."""
            super().setup_method(method)
            
            # Get paths to test data files
            self.test_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_data')
            self.valid_csv = os.path.join(self.test_data_dir, 'bulk_import_valid.csv')
            self.invalid_csv = os.path.join(self.test_data_dir, 'bulk_import_invalid.csv')
        
        def test_bulk_import_valid_data(self):
            """Test bulk import with valid data."""
            # Navigate to the bulk import page
            employee_list_page = self.home_page.navigate_to_employees()
            bulk_import_page = employee_list_page.navigate_to_bulk_import()
            
            # Upload valid CSV and submit
            result_page = bulk_import_page.upload_file(self.valid_csv).submit_import()
            
            # Verify redirect to employee list page
            assert "employees/" in self.driver.current_url, "Not redirected to employee list page"
            
            # Verify employees were imported
            assert result_page.is_employee_displayed("John Import"), "Imported employee not found"
            assert result_page.is_employee_displayed("Jane Import"), "Imported employee not found"
        
        def test_bulk_import_invalid_data(self):
            """Test bulk import with invalid data."""
            # Navigate to the bulk import page
            employee_list_page = self.home_page.navigate_to_employees()
            bulk_import_page = employee_list_page.navigate_to_bulk_import()
            
            # Upload invalid CSV and submit
            result_page = bulk_import_page.upload_file(self.invalid_csv).submit_import()
            
            # Verify still on import page with error
            assert "/import/" in self.driver.current_url, "Not on import page"
            assert result_page.is_error_message_displayed(), "Error message not displayed"
            
            # Verify error message content
            error_msg = result_page.get_error_message()
            assert "invalid" in error_msg.lower(), "Error message doesn't mention invalid data"
    ```

5. **Update the `employee_list_page.py`** to add navigation to the bulk import page:

    ```python
    def navigate_to_bulk_import(self):
        """
        Navigate to the bulk import page.
        
        Returns:
            BulkImportPage: Bulk import page object
        """
        self.click((By.XPATH, "//a[text()='Bulk Import']"))
        from .bulk_import_page import BulkImportPage
        return BulkImportPage(self.driver)
    ```

By following these patterns, you can easily extend the test framework to cover any new features added to the Employee Management System.
