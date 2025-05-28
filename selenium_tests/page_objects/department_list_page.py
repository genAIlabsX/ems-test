from selenium.webdriver.common.by import By
from .base_page import BasePage

class DepartmentListPage(BasePage):
    """
    Page object for the department list page of the Employee Management System.
    """
    
    # Locators
    PAGE_HEADER = (By.XPATH, "//h2[text()='Departments']")
    ADD_DEPARTMENT_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-primary') and text()='Add New Department']")
    DEPARTMENT_TABLE = (By.XPATH, "//table[contains(@class, 'table')]")
    TABLE_ROWS = (By.XPATH, "//table//tbody//tr")
    NO_DEPARTMENTS_MESSAGE = (By.XPATH, "//td[text()='No departments found']")
    
    # Row-specific locators - to be used with format()
    DEPARTMENT_ROW_BY_NAME = "//table//tbody//tr/td[text()='{}']/.."
    EDIT_BUTTON_IN_ROW = "//table//tbody//tr/td[text()='{}']/../td//a[text()='Edit']"
    DELETE_BUTTON_IN_ROW = "//table//tbody//tr/td[text()='{}']/../td//a[text()='Delete']"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_department_list(self):
        """Open the department list page."""
        self.open("departments/")
        return self
    
    def click_add_new_department(self):
        """
        Click the 'Add New Department' button.
        
        Returns:
            DepartmentFormPage: Department form page object
        """
        self.click(self.ADD_DEPARTMENT_BUTTON)
        from .department_form_page import DepartmentFormPage
        return DepartmentFormPage(self.driver)
    
    def get_department_count(self):
        """
        Get the number of departments in the table.
        
        Returns:
            int: Number of department rows
        """
        if self.is_element_present(self.NO_DEPARTMENTS_MESSAGE, 1):
            return 0
        rows = self.find_elements(self.TABLE_ROWS)
        return len(rows)
    
    def is_department_displayed(self, name):
        """
        Check if a department is displayed in the table.
        
        Args:
            name (str): Department name to check for
            
        Returns:
            bool: True if department is displayed
        """
        department_row_locator = (By.XPATH, self.DEPARTMENT_ROW_BY_NAME.format(name))
        return self.is_element_present(department_row_locator)
    
    def edit_department(self, name):
        """
        Click edit button for a department.
        
        Args:
            name (str): Name of the department to edit
            
        Returns:
            DepartmentFormPage: Department form page object
        """
        edit_button_locator = (By.XPATH, self.EDIT_BUTTON_IN_ROW.format(name))
        self.click(edit_button_locator)
        from .department_form_page import DepartmentFormPage
        return DepartmentFormPage(self.driver)
    
    def delete_department(self, name):
        """
        Click delete button for a department.
        
        Args:
            name (str): Name of the department to delete
            
        Returns:
            DepartmentDeletePage: Department delete page object
        """
        delete_button_locator = (By.XPATH, self.DELETE_BUTTON_IN_ROW.format(name))
        self.click(delete_button_locator)
        from .department_delete_page import DepartmentDeletePage
        return DepartmentDeletePage(self.driver)
    
    def get_department_names(self):
        """
        Get all department names from the table.
        
        Returns:
            list: List of department names
        """
        if self.is_element_present(self.NO_DEPARTMENTS_MESSAGE, 1):
            return []
        
        rows = self.find_elements(self.TABLE_ROWS)
        names = []
        
        for row in rows:
            name_cell = row.find_element(By.XPATH, "./td[1]")
            names.append(name_cell.text)
        
        return names
