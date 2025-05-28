import csv
import os
import random
import string
from datetime import datetime

class TestDataLoader:
    """
    Utility class for loading and generating test data.
    """
    
    @staticmethod
    def load_csv_data(file_path):
        """
        Load data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            list: List of dictionaries with CSV data
        """
        data = []
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
        return data
    
    @staticmethod
    def get_employees_data():
        """
        Get employee test data from CSV.
        
        Returns:
            list: List of employee dictionaries
        """
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                'test_data', 'employees.csv')
        return TestDataLoader.load_csv_data(file_path)
    
    @staticmethod
    def get_departments_data():
        """
        Get department test data from CSV.
        
        Returns:
            list: List of department dictionaries
        """
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                'test_data', 'departments.csv')
        return TestDataLoader.load_csv_data(file_path)
    
    @staticmethod
    def get_random_employee():
        """
        Get a random employee from test data.
        
        Returns:
            dict: Random employee data
        """
        employees = TestDataLoader.get_employees_data()
        return random.choice(employees)
    
    @staticmethod
    def get_random_department():
        """
        Get a random department from test data.
        
        Returns:
            dict: Random department data
        """
        departments = TestDataLoader.get_departments_data()
        return random.choice(departments)
    
    @staticmethod
    def generate_random_name():
        """
        Generate a random person name.
        
        Returns:
            str: Random name
        """
        first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", 
                      "Robert", "Lisa", "William", "Elizabeth", "Richard", "Jennifer"]
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", 
                     "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"]
        
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    @staticmethod
    def generate_random_email(name=None):
        """
        Generate a random email based on name or random characters.
        
        Args:
            name (str, optional): Name to base email on
            
        Returns:
            str: Random email
        """
        if name:
            # Convert name to lowercase, replace spaces with dots
            email_base = name.lower().replace(" ", ".")
        else:
            # Generate random string
            chars = string.ascii_lowercase + string.digits
            email_base = ''.join(random.choice(chars) for _ in range(8))
        
        domains = ["example.com", "test.com", "email.com", "domain.com", "company.com"]
        timestamp = datetime.now().strftime("%H%M%S")
        
        return f"{email_base}.{timestamp}@{random.choice(domains)}"
    
    @staticmethod
    def generate_random_salary():
        """
        Generate a random salary between 30000 and 150000.
        
        Returns:
            float: Random salary
        """
        return round(random.uniform(30000, 150000), 2)
    
    @staticmethod
    def generate_random_status():
        """
        Generate a random employee status.
        
        Returns:
            str: 'Active' or 'Inactive'
        """
        return random.choice(["Active", "Inactive"])
    
    @staticmethod
    def generate_random_employee_data(department=None):
        """
        Generate random employee data.
        
        Args:
            department (str, optional): Department name
            
        Returns:
            dict: Random employee data
        """
        name = TestDataLoader.generate_random_name()
        
        if not department:
            department_data = TestDataLoader.get_random_department()
            department = department_data['name']
        
        return {
            "name": name,
            "email": TestDataLoader.generate_random_email(name),
            "department": department,
            "salary": TestDataLoader.generate_random_salary(),
            "status": TestDataLoader.generate_random_status()
        }
    
    @staticmethod
    def generate_random_department_name():
        """
        Generate a random department name.
        
        Returns:
            str: Random department name
        """
        departments = ["Accounting", "Business Development", "Data Science", 
                      "Design", "Engineering", "Finance", "Human Resources", 
                      "Legal", "Marketing", "Operations", "Product Management", 
                      "Quality Assurance", "Research", "Sales", "Support"]
        
        # Add a random suffix to make it unique
        suffix = ''.join(random.choice(string.digits) for _ in range(3))
        return f"{random.choice(departments)}-{suffix}"
