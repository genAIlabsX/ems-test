import pytest
from selenium_tests.tests.base_test import BaseTest

class TestFormValidation(BaseTest):
    """
    Tests for form validation in the application.
    """
    
    def test_employee_form_required_fields(self):
        """Test validation of required fields in employee form."""
        # Navigate to the employee form
        employee_list_page = self.home_page.navigate_to_employees()
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Submit the form without filling any fields
        result_page = employee_form_page.submit_form()
        
        # Verify validation errors
        validation_errors = result_page.get_validation_errors()
        assert 'name' in validation_errors, "No validation error for name field"
        assert 'email' in validation_errors, "No validation error for email field"
    
    def test_employee_form_email_validation(self):
        """Test email format validation in employee form."""
        # Navigate to the employee form
        employee_list_page = self.home_page.navigate_to_employees()
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Fill the form with invalid email
        employee_data = self.test_data_loader.generate_random_employee_data()
        employee_data['email'] = "invalid-email"
        
        # Fill the form and submit
        result_page = employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Verify validation errors
        validation_errors = result_page.get_validation_errors()
        assert 'email' in validation_errors, "No validation error for invalid email"
    
    def test_employee_form_salary_validation(self):
        """Test salary validation in employee form."""
        # Navigate to the employee form
        employee_list_page = self.home_page.navigate_to_employees()
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Fill the form with negative salary
        employee_data = self.test_data_loader.generate_random_employee_data()
        employee_data['salary'] = -1000
        
        # Fill the form and submit
        result_page = employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Verify validation errors
        validation_errors = result_page.get_validation_errors()
        assert 'salary' in validation_errors, "No validation error for negative salary"
    
    def test_department_form_required_fields(self):
        """Test validation of required fields in department form."""
        # Navigate to the department form
        department_list_page = self.home_page.navigate_to_departments()
        department_form_page = department_list_page.click_add_new_department()
        
        # Submit the form without filling any fields
        result_page = department_form_page.submit_form()
        
        # Verify validation errors
        validation_errors = result_page.get_validation_errors()
        assert 'name' in validation_errors, "No validation error for name field"
    
    def test_employee_form_unique_email(self):
        """Test validation of unique email in employee form."""
        # First add an employee
        employee_data = self.test_data_loader.generate_random_employee_data()
        
        # Navigate to employee list and add new employee
        employee_list_page = self.home_page.navigate_to_employees()
        employee_form_page = employee_list_page.click_add_new_employee()
        employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Try to add another employee with the same email
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Use a different name but same email
        duplicate_employee_data = self.test_data_loader.generate_random_employee_data()
        duplicate_employee_data['email'] = employee_data['email']
        
        # Fill the form and submit
        result_page = employee_form_page.fill_employee_form(duplicate_employee_data).submit_form()
        
        # Verify we're still on the form page (validation error)
        assert "create" in self.driver.current_url, "No validation error for duplicate email"
    
    def test_department_form_unique_name(self):
        """Test validation of unique name in department form."""
        # First add a department
        department_name = self.test_data_loader.generate_random_department_name()
        
        # Navigate to department list and add new department
        department_list_page = self.home_page.navigate_to_departments()
        department_form_page = department_list_page.click_add_new_department()
        department_form_page.fill_department_form(department_name).submit_form()
        
        # Try to add another department with the same name
        department_form_page = department_list_page.click_add_new_department()
        
        # Fill the form with the same name and submit
        result_page = department_form_page.fill_department_form(department_name).submit_form()
        
        # Verify we're still on the form page (validation error)
        assert "create" in self.driver.current_url, "No validation error for duplicate department name"
