from selenium.webdriver.common.by import By
from .base_page import BasePage

class DepartmentDeletePage(BasePage):
    """
    Page object for the department delete confirmation page.
    """
    
    # Locators
    CONFIRMATION_TEXT = (By.XPATH, "//p[contains(text(), 'Are you sure you want to delete')]")
    DEPARTMENT_NAME = (By.XPATH, "//p/strong")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-danger') and text()='Confirm']")
    CANCEL_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-secondary') and text()='Cancel']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_department_name(self):
        """
        Get the name of the department to be deleted.
        
        Returns:
            str: Department name
        """
        return self.get_text(self.DEPARTMENT_NAME)
    
    def confirm_delete(self):
        """
        Confirm department deletion.
        
        Returns:
            DepartmentListPage: Department list page
        """
        self.click(self.CONFIRM_DELETE_BUTTON)
        from .department_list_page import DepartmentListPage
        return DepartmentListPage(self.driver)
    
    def cancel_delete(self):
        """
        Cancel department deletion.
        
        Returns:
            DepartmentListPage: Department list page
        """
        self.click(self.CANCEL_BUTTON)
        from .department_list_page import DepartmentListPage
        return DepartmentListPage(self.driver)
    
    def is_on_delete_page(self):
        """
        Check if we are on the delete confirmation page.
        
        Returns:
            bool: True if on delete page
        """
        return self.is_element_present(self.CONFIRMATION_TEXT)
