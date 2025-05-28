# Test automation
Automate the UI testing of the Python Django-based Employee Management System using both Selenium WebDriver and UFT (Unified Functional Testing). The goal is to validate user interactions, form behavior, and data rendering using two different automation tools. Assist in writing test scripts, locators, and reusable functions

## Django Application 
* main folder location: `..\ems`
* tech stack:
    * Python
    * Django
    * SQLite

## Test Scenarios to Automate
1.	Add New Employee
2.	View All Employees
3.	Form Validation
4.	Navigation Between Pages

## Tools & Technologies
* Selenium WebDriver: Open-source browser automation
* UFT (Micro Focus): Enterprise-grade functional testing
* Python/pytest	For Selenium scripting
* VBScriptFor UFT scripting

## Selenium Script Details
Use python for test implementation
1. Page Object Model (POM)
Each web page is represented by a class that encapsulates:
* Web element locators using @FindBy or By
* Page actions (e.g., fillForm(), clickSubmit())
* Assertions (optional)
Example: AddEmployeePage.java
2. Test Class Example: AddEmployeeTest.java
3. Test Data Integration
•	Use employees.csv to drive data-driven tests
•	Load data using a utility class (TestDataLoader.java)

## UFT Script Details
* Use Descriptive Programming or Object Repository
* Automate the same flows as Selenium
* Validate UI elements, form behavior, and navigation
* Use VBScript to write reusable functions
Example: AddEmployeeTest.vbs

## Deliverables
* Selenium test scripts (Python)
* UFT test scripts (VBScript)
* Test data files (CSV, JSON)
* A README.md with:
* Setup and run instructions for both tools
* GitHub Copilot prompts used
* Challenges faced

## Guidelines
* use powershell compatible command lines
* do not use `&&' to connect command lines 
* thorughly analize application code base located in `..\ems` and subfolders
* do not change or add anything in folder `..ems` and it subloders
* catalogue all UI actions in application
* build tests  