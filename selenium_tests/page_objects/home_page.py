from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    """
    Page object for the home page of the Employee Management System.
    """
    
    # Locators
    NAVBAR_BRAND = (By.CLASS_NAME, "navbar-brand")
    HOME_NAV_LINK = (By.XPATH, "//a[@class='nav-link' and text()='Home']")
    EMPLOYEES_NAV_LINK = (By.XPATH, "//a[@class='nav-link' and text()='Employees']")
    DEPARTMENTS_NAV_LINK = (By.XPATH, "//a[@class='nav-link' and text()='Departments']")
    FOOTER_TEXT = (By.CLASS_NAME, "text-muted")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_home_page(self):
        """Open the home page."""
        self.open("")
        return self
    
    def navigate_to_employees(self):
        """
        Navigate to the employees page.
        
        Returns:
            EmployeeListPage: Employee list page object
        """
        self.click(self.EMPLOYEES_NAV_LINK)
        from .employee_list_page import EmployeeListPage
        return EmployeeListPage(self.driver)
    
    def navigate_to_departments(self):
        """
        Navigate to the departments page.
        
        Returns:
            DepartmentListPage: Department list page object
        """
        self.click(self.DEPARTMENTS_NAV_LINK)
        from .department_list_page import DepartmentListPage
        return DepartmentListPage(self.driver)
    
    def is_on_home_page(self):
        """
        Check if we are on the home page.
        
        Returns:
            bool: True if on home page
        """
        return self.is_element_present(self.NAVBAR_BRAND) and self.get_current_url() == f"{self.base_url}/"
    
    def get_footer_text(self):
        """
        Get the footer text.
        
        Returns:
            str: Footer text
        """
        return self.get_text(self.FOOTER_TEXT)
