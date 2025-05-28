from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    """
    Base class for all page objects in the application.
    Contains common methods used across all pages.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.base_url
    
    def open(self, url_path=""):
        """
        Open a page by appending url_path to the base URL.
        
        Args:
            url_path (str): Path to append to base URL
        """
        self.driver.get(f"{self.base_url}/{url_path}")
    
    def find_element(self, locator, timeout=10):
        """
        Find an element with explicit wait.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
            
        Returns:
            WebElement: Found element
            
        Raises:
            TimeoutException: If element not found within timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        """
        Find elements with explicit wait.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for elements
            
        Returns:
            list: List of found WebElements
            
        Raises:
            TimeoutException: If no elements found within timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def click(self, locator, timeout=10):
        """
        Find element and click with explicit wait.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
            
        Raises:
            TimeoutException: If element not found or not clickable
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def input_text(self, locator, text, timeout=10):
        """
        Find element, clear it, and send keys.
        
        Args:
            locator (tuple): Locator strategy and value
            text (str): Text to input
            timeout (int): Maximum time to wait for element
            
        Raises:
            TimeoutException: If element not found
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def select_option_by_text(self, locator, option_text, timeout=10):
        """
        Select an option from a dropdown by visible text.
        
        Args:
            locator (tuple): Locator strategy and value
            option_text (str): Text of option to select
            timeout (int): Maximum time to wait for element
            
        Raises:
            TimeoutException: If element not found
        """
        from selenium.webdriver.support.ui import Select
        select = Select(self.find_element(locator, timeout))
        select.select_by_visible_text(option_text)
    
    def get_text(self, locator, timeout=10):
        """
        Get text from an element.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
            
        Returns:
            str: Text of element
            
        Raises:
            TimeoutException: If element not found
        """
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_present(self, locator, timeout=5):
        """
        Check if element is present.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
            
        Returns:
            bool: True if element is present, False otherwise
        """
        try:
            self.find_element(locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_element_visible(self, locator, timeout=10):
        """
        Wait for element to be visible.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
            
        Returns:
            WebElement: Visible element
            
        Raises:
            TimeoutException: If element not visible within timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_invisible(self, locator, timeout=10):
        """
        Wait for element to be invisible.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
            
        Returns:
            bool: True if element is invisible
            
        Raises:
            TimeoutException: If element still visible within timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def scroll_to_element(self, locator, timeout=10):
        """
        Scroll to an element.
        
        Args:
            locator (tuple): Locator strategy and value
            timeout (int): Maximum time to wait for element
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_page_title(self):
        """
        Get page title.
        
        Returns:
            str: Page title
        """
        return self.driver.title
    
    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
    
    def go_back(self):
        """Navigate back to the previous page."""
        self.driver.back()
    
    def get_current_url(self):
        """
        Get current URL.
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
