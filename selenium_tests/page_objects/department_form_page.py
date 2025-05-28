from selenium.webdriver.common.by import By
from .base_page import BasePage

class DepartmentFormPage(BasePage):
    """
    Page object for the department form page of the Employee Management System.
    Used for both create and update operations.
    """
    
    # Locators
    PAGE_HEADER = (By.XPATH, "//h2[contains(text(), 'Department')]")
    NAME_INPUT = (By.ID, "id_name")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    # Validation error messages
    NAME_ERROR = (By.XPATH, "//input[@id='id_name']/following-sibling::div[@class='invalid-feedback']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_department_form(self, name):
        """
        Fill the department form with the given name.
        
        Args:
            name (str): Department name
        """
        self.input_text(self.NAME_INPUT, name)
        return self
    
    def submit_form(self):
        """
        Submit the department form.
        
        Returns:
            DepartmentListPage: Department list page if submission successful
            self: Current page if validation errors
        """
        self.click(self.SUBMIT_BUTTON)
        
        # Check if we were redirected to the department list page
        if "departments/" in self.get_current_url() and not "/create/" in self.get_current_url() and not "/update/" in self.get_current_url():
            from .department_list_page import DepartmentListPage
            return DepartmentListPage(self.driver)
        
        # We're still on the form page (validation errors)
        return self
    
    def get_validation_errors(self):
        """
        Get all validation error messages.
        
        Returns:
            dict: Validation errors by field
        """
        errors = {}
        
        if self.is_element_present(self.NAME_ERROR, 1):
            errors['name'] = self.get_text(self.NAME_ERROR)
        
        return errors
    
    def is_create_page(self):
        """
        Check if this is the create department page.
        
        Returns:
            bool: True if create page
        """
        header_text = self.get_text(self.PAGE_HEADER)
        return "Add New" in header_text
    
    def is_edit_page(self):
        """
        Check if this is the edit department page.
        
        Returns:
            bool: True if edit page
        """
        header_text = self.get_text(self.PAGE_HEADER)
        return "Edit" in header_text
    
    def get_current_name(self):
        """
        Get the current department name in the form.
        
        Returns:
            str: Current department name
        """
        return self.find_element(self.NAME_INPUT).get_attribute("value")
