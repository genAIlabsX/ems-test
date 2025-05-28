from selenium.webdriver.common.by import By
from .base_page import BasePage

class EmployeeDeletePage(BasePage):
    """
    Page object for the employee delete confirmation page.
    """
    
    # Locators
    CONFIRMATION_TEXT = (By.XPATH, "//p[contains(text(), 'Are you sure you want to delete')]")
    EMPLOYEE_NAME = (By.XPATH, "//p/strong")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-danger') and text()='Confirm']")
    CANCEL_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-secondary') and text()='Cancel']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_employee_name(self):
        """
        Get the name of the employee to be deleted.
        
        Returns:
            str: Employee name
        """
        return self.get_text(self.EMPLOYEE_NAME)
    
    def confirm_delete(self):
        """
        Confirm employee deletion.
        
        Returns:
            EmployeeListPage: Employee list page
        """
        self.click(self.CONFIRM_DELETE_BUTTON)
        from .employee_list_page import EmployeeListPage
        return EmployeeListPage(self.driver)
    
    def cancel_delete(self):
        """
        Cancel employee deletion.
        
        Returns:
            EmployeeListPage: Employee list page
        """
        self.click(self.CANCEL_BUTTON)
        from .employee_list_page import EmployeeListPage
        return EmployeeListPage(self.driver)
    
    def is_on_delete_page(self):
        """
        Check if we are on the delete confirmation page.
        
        Returns:
            bool: True if on delete page
        """
        return self.is_element_present(self.CONFIRMATION_TEXT)
