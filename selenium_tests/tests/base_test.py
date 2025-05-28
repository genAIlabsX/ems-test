import pytest
from selenium_tests.page_objects import HomePage
from selenium_tests.test_data import TestDataLoader

class BaseTest:
    """
    Base class for all test classes.
    Contains common setup and utility methods.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Setup method that runs before each test.
        
        Args:
            driver: WebDriver instance from conftest.py
        """
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.test_data_loader = TestDataLoader
        
        # Navigate to the home page
        self.home_page.open_home_page()
        
    def teardown_method(self, method):
        """Teardown method that runs after each test."""
        # Can be overridden in subclasses if needed
        pass
