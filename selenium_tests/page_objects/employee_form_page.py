from selenium.webdriver.common.by import By
from .base_page import BasePage

class EmployeeFormPage(BasePage):
    """
    Page object for the employee form page of the Employee Management System.
    Used for both create and update operations.
    """
    
    # Locators
    PAGE_HEADER = (By.XPATH, "//h2[contains(text(), 'Employee')]")
    NAME_INPUT = (By.ID, "id_name")
    EMAIL_INPUT = (By.ID, "id_email")
    DEPARTMENT_SELECT = (By.ID, "id_department")
    SALARY_INPUT = (By.ID, "id_salary")
    STATUS_ACTIVE_RADIO = (By.ID, "id_status_active")
    STATUS_INACTIVE_RADIO = (By.ID, "id_status_inactive")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    # Validation error messages
    NAME_ERROR = (By.XPATH, "//input[@id='id_name']/following-sibling::div[@class='invalid-feedback']")
    EMAIL_ERROR = (By.XPATH, "//input[@id='id_email']/following-sibling::div[@class='invalid-feedback']")
    DEPARTMENT_ERROR = (By.XPATH, "//select[@id='id_department']/following-sibling::div[@class='invalid-feedback']")
    SALARY_ERROR = (By.XPATH, "//input[@id='id_salary']/following-sibling::div[@class='invalid-feedback']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_employee_form(self, employee_data):
        """
        Fill the employee form with the given data.
        
        Args:
            employee_data (dict): Employee data with keys:
                                  name, email, department, salary, status
        """
        if 'name' in employee_data:
            self.input_text(self.NAME_INPUT, employee_data['name'])
        
        if 'email' in employee_data:
            self.input_text(self.EMAIL_INPUT, employee_data['email'])
        
        if 'department' in employee_data:
            self.select_option_by_text(self.DEPARTMENT_SELECT, employee_data['department'])
        
        if 'salary' in employee_data:
            self.input_text(self.SALARY_INPUT, str(employee_data['salary']))
        
        if 'status' in employee_data:
            if employee_data['status'].lower() == 'active':
                self.click(self.STATUS_ACTIVE_RADIO)
            else:
                self.click(self.STATUS_INACTIVE_RADIO)
        
        return self
    
    def submit_form(self):
        """
        Submit the employee form.
        
        Returns:
            EmployeeListPage: Employee list page if submission successful
            self: Current page if validation errors
        """
        self.click(self.SUBMIT_BUTTON)
        
        # Check if we were redirected to the employee list page
        if "employees/" in self.get_current_url() and not "/create/" in self.get_current_url() and not "/update/" in self.get_current_url():
            from .employee_list_page import EmployeeListPage
            return EmployeeListPage(self.driver)
        
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
        
        if self.is_element_present(self.EMAIL_ERROR, 1):
            errors['email'] = self.get_text(self.EMAIL_ERROR)
        
        if self.is_element_present(self.DEPARTMENT_ERROR, 1):
            errors['department'] = self.get_text(self.DEPARTMENT_ERROR)
        
        if self.is_element_present(self.SALARY_ERROR, 1):
            errors['salary'] = self.get_text(self.SALARY_ERROR)
        
        return errors
    
    def is_create_page(self):
        """
        Check if this is the create employee page.
        
        Returns:
            bool: True if create page
        """
        header_text = self.get_text(self.PAGE_HEADER)
        return "Add New" in header_text
    
    def is_edit_page(self):
        """
        Check if this is the edit employee page.
        
        Returns:
            bool: True if edit page
        """
        header_text = self.get_text(self.PAGE_HEADER)
        return "Edit" in header_text
    
    def get_current_form_values(self):
        """
        Get the current values in the form.
        
        Returns:
            dict: Current form values
        """
        name = self.find_element(self.NAME_INPUT).get_attribute("value")
        email = self.find_element(self.EMAIL_INPUT).get_attribute("value")
        salary = self.find_element(self.SALARY_INPUT).get_attribute("value")
        
        department_select = self.find_element(self.DEPARTMENT_SELECT)
        selected_option = department_select.find_element(By.XPATH, ".//option[@selected='selected']")
        department = selected_option.text if selected_option else ""
        
        status = "Active" if self.find_element(self.STATUS_ACTIVE_RADIO).is_selected() else "Inactive"
        
        return {
            "name": name,
            "email": email,
            "department": department,
            "salary": salary,
            "status": status
        }
