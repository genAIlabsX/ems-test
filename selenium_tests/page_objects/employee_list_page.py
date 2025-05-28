from selenium.webdriver.common.by import By
from .base_page import BasePage

class EmployeeListPage(BasePage):
    """
    Page object for the employee list page of the Employee Management System.
    """
    
    # Locators
    PAGE_HEADER = (By.XPATH, "//h2[text()='Employees']")
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-primary') and text()='Add New Employee']")
    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")
    FILTER_BUTTON = (By.XPATH, "//button[text()='Filter']")
    STATUS_DROPDOWN = (By.NAME, "status")
    DEPARTMENT_DROPDOWN = (By.NAME, "department")
    EMPLOYEE_TABLE = (By.XPATH, "//table[contains(@class, 'table')]")
    TABLE_ROWS = (By.XPATH, "//table//tbody//tr")
    EXPORT_CSV_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-success') and text()='Export to CSV']")
    NO_EMPLOYEES_MESSAGE = (By.XPATH, "//td[text()='No employees found']")
    
    # Row-specific locators - to be used with format()
    EMPLOYEE_ROW_BY_NAME = "//table//tbody//tr/td[text()='{}']/.."
    EDIT_BUTTON_IN_ROW = "//table//tbody//tr/td[text()='{}']/../td//a[text()='Edit']"
    DELETE_BUTTON_IN_ROW = "//table//tbody//tr/td[text()='{}']/../td//a[text()='Delete']"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_employee_list(self):
        """Open the employee list page."""
        self.open("employees/")
        return self
    
    def click_add_new_employee(self):
        """
        Click the 'Add New Employee' button.
        
        Returns:
            EmployeeFormPage: Employee form page object
        """
        self.click(self.ADD_EMPLOYEE_BUTTON)
        from .employee_form_page import EmployeeFormPage
        return EmployeeFormPage(self.driver)
    
    def search_employee(self, search_text):
        """
        Search for an employee.
        
        Args:
            search_text (str): Text to search for
        """
        self.input_text(self.SEARCH_INPUT, search_text)
        self.click(self.FILTER_BUTTON)
        return self
    
    def filter_by_status(self, status):
        """
        Filter employees by status.
        
        Args:
            status (str): Status to filter by (Active/Inactive)
        """
        self.select_option_by_text(self.STATUS_DROPDOWN, status)
        self.click(self.FILTER_BUTTON)
        return self
    
    def filter_by_department(self, department):
        """
        Filter employees by department.
        
        Args:
            department (str): Department name to filter by
        """
        self.select_option_by_text(self.DEPARTMENT_DROPDOWN, department)
        self.click(self.FILTER_BUTTON)
        return self
    
    def get_employee_count(self):
        """
        Get the number of employees in the table.
        
        Returns:
            int: Number of employee rows
        """
        if self.is_element_present(self.NO_EMPLOYEES_MESSAGE, 1):
            return 0
        rows = self.find_elements(self.TABLE_ROWS)
        return len(rows)
    
    def is_employee_displayed(self, name):
        """
        Check if an employee is displayed in the table.
        
        Args:
            name (str): Employee name to check for
            
        Returns:
            bool: True if employee is displayed
        """
        employee_row_locator = (By.XPATH, self.EMPLOYEE_ROW_BY_NAME.format(name))
        return self.is_element_present(employee_row_locator)
    
    def edit_employee(self, name):
        """
        Click edit button for an employee.
        
        Args:
            name (str): Name of the employee to edit
            
        Returns:
            EmployeeFormPage: Employee form page object
        """
        edit_button_locator = (By.XPATH, self.EDIT_BUTTON_IN_ROW.format(name))
        self.click(edit_button_locator)
        from .employee_form_page import EmployeeFormPage
        return EmployeeFormPage(self.driver)
    
    def delete_employee(self, name):
        """
        Click delete button for an employee.
        
        Args:
            name (str): Name of the employee to delete
            
        Returns:
            EmployeeDeletePage: Employee delete page object
        """
        delete_button_locator = (By.XPATH, self.DELETE_BUTTON_IN_ROW.format(name))
        self.click(delete_button_locator)
        from .employee_delete_page import EmployeeDeletePage
        return EmployeeDeletePage(self.driver)
    
    def export_to_csv(self):
        """Click the Export to CSV button."""
        self.click(self.EXPORT_CSV_BUTTON)
    
    def get_employee_data(self, name):
        """
        Get employee data from the table.
        
        Args:
            name (str): Name of the employee
            
        Returns:
            dict: Employee data (name, email, department, salary, status)
        """
        row_locator = (By.XPATH, self.EMPLOYEE_ROW_BY_NAME.format(name))
        if not self.is_element_present(row_locator):
            return None
        
        row = self.find_element(row_locator)
        cells = row.find_elements(By.TAG_NAME, "td")
        
        return {
            "name": cells[0].text,
            "email": cells[1].text,
            "department": cells[2].text,
            "salary": cells[3].text.replace("$", ""),
            "status": cells[4].text
        }
