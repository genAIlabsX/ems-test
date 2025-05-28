import pytest
from selenium_tests.tests.base_test import BaseTest

class TestNavigation(BaseTest):
    """
    Tests for navigation between pages in the application.
    """
    
    def test_navigation_from_home(self):
        """Test navigation from home page to other pages."""
        # Verify we're on the home page
        assert self.home_page.is_on_home_page(), "Not on home page"
        
        # Navigate to employees page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Verify we're on the employees page
        assert "employees/" in self.driver.current_url, "Not on employees page"
        
        # Navigate back to home
        self.home_page.open_home_page()
        
        # Navigate to departments page
        department_list_page = self.home_page.navigate_to_departments()
        
        # Verify we're on the departments page
        assert "departments/" in self.driver.current_url, "Not on departments page"
    
    def test_navigation_between_employee_pages(self):
        """Test navigation between employee-related pages."""
        # Navigate to the employee list page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Navigate to add employee form
        employee_form_page = employee_list_page.click_add_new_employee()
        
        # Verify we're on the add employee page
        assert "create" in self.driver.current_url, "Not on add employee page"
        
        # Add a new employee
        employee_data = self.test_data_loader.generate_random_employee_data()
        employee_form_page.fill_employee_form(employee_data).submit_form()
        
        # Verify we're back on the employee list page
        assert "employees/" in self.driver.current_url and not "/create/" in self.driver.current_url, "Not redirected to employee list page"
        
        # Navigate to edit employee page
        edit_page = employee_list_page.edit_employee(employee_data['name'])
        
        # Verify we're on the edit employee page
        assert "update" in self.driver.current_url, "Not on edit employee page"
        
        # Navigate to delete employee page
        employee_list_page = self.home_page.navigate_to_employees()
        delete_page = employee_list_page.delete_employee(employee_data['name'])
        
        # Verify we're on the delete confirmation page
        assert "delete" in self.driver.current_url, "Not on delete confirmation page"
    
    def test_navigation_between_department_pages(self):
        """Test navigation between department-related pages."""
        # Navigate to the department list page
        department_list_page = self.home_page.navigate_to_departments()
        
        # Navigate to add department form
        department_form_page = department_list_page.click_add_new_department()
        
        # Verify we're on the add department page
        assert "create" in self.driver.current_url, "Not on add department page"
        
        # Add a new department
        department_name = self.test_data_loader.generate_random_department_name()
        department_form_page.fill_department_form(department_name).submit_form()
        
        # Verify we're back on the department list page
        assert "departments/" in self.driver.current_url and not "/create/" in self.driver.current_url, "Not redirected to department list page"
        
        # Navigate to edit department page
        edit_page = department_list_page.edit_department(department_name)
        
        # Verify we're on the edit department page
        assert "update" in self.driver.current_url, "Not on edit department page"
        
        # Navigate to delete department page
        department_list_page = self.home_page.navigate_to_departments()
        delete_page = department_list_page.delete_department(department_name)
        
        # Verify we're on the delete confirmation page
        assert "delete" in self.driver.current_url, "Not on delete confirmation page"
    
    def test_navigation_using_browser_controls(self):
        """Test navigation using browser back/forward buttons."""
        # Navigate to the employee list page
        employee_list_page = self.home_page.navigate_to_employees()
        
        # Navigate to departments page
        department_list_page = self.home_page.navigate_to_departments()
        
        # Go back to employees page
        self.driver.back()
        
        # Verify we're back on the employees page
        assert "employees/" in self.driver.current_url, "Back button didn't work - not on employees page"
        
        # Go forward to departments page
        self.driver.forward()
        
        # Verify we're back on the departments page
        assert "departments/" in self.driver.current_url, "Forward button didn't work - not on departments page"
