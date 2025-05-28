import pytest
from selenium_tests.tests.base_test import BaseTest

class TestAddEmployee(BaseTest):
    """
    Tests for adding new employees.
    """
    
    def test_add_valid_employee(self):
        """Test adding a new employee with valid data."""
        # Generate random employee data
        employee_data = self.test_data_loader.generate_random_employee_data()
        
        # Navigate to the employee list page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Click on Add New Employee button
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Verify we're on the create employee page
        assert employee_form_page.is_create_page(), "Not on the create employee page"
        
        # Fill the form and submit
        result_page = employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Verify we were redirected to the employee list page
        assert "employees/" in self.driver.current_url, "Not redirected to employee list page"
        
        # Verify the employee was added successfully
        assert result_page.is_employee_displayed(employee_data['name']), f"Employee {employee_data['name']} not found in list"
    
    def test_add_employee_missing_required_fields(self):
        """Test form validation for required fields."""
        # Navigate to the employee list page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Click on Add New Employee button
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Submit the form without filling any fields
        result_page = employee_form_page.submit_form()
        
        # Verify we're still on the form page
        assert employee_form_page.is_create_page(), "Not on the create employee page"
        
        # Verify validation errors
        validation_errors = result_page.get_validation_errors()
        assert 'name' in validation_errors, "No validation error for name field"
        assert 'email' in validation_errors, "No validation error for email field"
    
    def test_add_employee_invalid_email(self):
        """Test form validation for invalid email."""
        # Generate random employee data with invalid email
        employee_data = self.test_data_loader.generate_random_employee_data()
        employee_data['email'] = "invalid-email"
        
        # Navigate to the employee list page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Click on Add New Employee button
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Fill the form with invalid email and submit
        result_page = employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Verify we're still on the form page
        assert employee_form_page.is_create_page(), "Not on the create employee page"
        
        # Verify validation error for email
        validation_errors = result_page.get_validation_errors()
        assert 'email' in validation_errors, "No validation error for invalid email"
    
    def test_add_employee_negative_salary(self):
        """Test form validation for negative salary."""
        # Generate random employee data with negative salary
        employee_data = self.test_data_loader.generate_random_employee_data()
        employee_data['salary'] = -1000
        
        # Navigate to the employee list page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Click on Add New Employee button
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Fill the form with negative salary and submit
        result_page = employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Verify we're still on the form page
        assert employee_form_page.is_create_page(), "Not on the create employee page"
        
        # Verify validation error for salary
        validation_errors = result_page.get_validation_errors()
        assert 'salary' in validation_errors, "No validation error for negative salary"
