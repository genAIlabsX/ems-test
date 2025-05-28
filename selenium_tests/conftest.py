import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    """
    Fixture for setting up the WebDriver for tests.
    
    Returns:
        WebDriver: Chrome WebDriver instance
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome for CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    
    # Set base URL - Django default
    driver.base_url = "http://127.0.0.1:8000"
    
    yield driver
    
    # Cleanup
    driver.quit()
