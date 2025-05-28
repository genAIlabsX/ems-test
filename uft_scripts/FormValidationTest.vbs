' UFT Test Script for Employee Management System
' Test Case: Form Validation

Option Explicit

' Application URL
Const AppURL = "http://127.0.0.1:8000/"

' ===== Main Test Script =====
' Launch browser and navigate to application
SystemUtil.Run "chrome.exe", AppURL

' Wait for page to load
Wait 3

' Navigate to Employees page
Browser("title:=Employee Management System").Page("title:=Employee Management System").Link("text:=Employees").Click
Wait 2

' Click Add New Employee button
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").Link("text:=Add New Employee").Click
Wait 2

' Test 1: Empty Form Submission
Reporter.ReportEvent micInfo, "Test Step", "Testing empty form submission"

' Submit the form without filling any fields
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebButton("type:=submit").Click
Wait 2

' Check for validation errors
Dim nameError, emailError
nameError = Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebElement("class:=invalid-feedback", "index:=0").Exist(2)
emailError = Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebElement("class:=invalid-feedback", "index:=1").Exist(2)

If nameError And emailError Then
    Reporter.ReportEvent micPass, "Empty Form Test", "Validation errors for required fields are displayed correctly"
Else
    Reporter.ReportEvent micFail, "Empty Form Test", "Validation errors for required fields are not displayed"
End If

' Test 2: Invalid Email Format
Reporter.ReportEvent micInfo, "Test Step", "Testing invalid email format"

' Fill name field
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=name").Set "Test User"

' Fill invalid email
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=email").Set "invalid-email"

' Submit the form
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebButton("type:=submit").Click
Wait 2

' Check for email validation error
If Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebElement("class:=invalid-feedback", "index:=1").Exist(2) Then
    Reporter.ReportEvent micPass, "Invalid Email Test", "Email validation error is displayed correctly"
Else
    Reporter.ReportEvent micFail, "Invalid Email Test", "Email validation error is not displayed"
End If

' Test 3: Negative Salary
Reporter.ReportEvent micInfo, "Test Step", "Testing negative salary validation"

' Set email to valid value
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=email").Set "test.user@example.com"

' Set salary to negative value
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=salary").Set "-1000"

' Select a department (assuming Engineering exists)
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebList("name:=department").Select 1 ' Select first department

' Submit the form
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebButton("type:=submit").Click
Wait 2

' Check for salary validation error
If Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebElement("class:=invalid-feedback").Exist(2) Then
    Reporter.ReportEvent micPass, "Negative Salary Test", "Salary validation error is displayed correctly"
Else
    Reporter.ReportEvent micFail, "Negative Salary Test", "Salary validation error is not displayed"
End If

' Navigate to Departments page to test department form validation
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").Link("text:=Departments").Click
Wait 2

' Click Add New Department button
Browser("title:=Departments - Employee Management System").Page("title:=Departments - Employee Management System").Link("text:=Add New Department").Click
Wait 2

' Test 4: Empty Department Name
Reporter.ReportEvent micInfo, "Test Step", "Testing empty department name validation"

' Submit the form without filling name field
Browser("title:=Add Department - Employee Management System").Page("title:=Add Department - Employee Management System").WebButton("type:=submit").Click
Wait 2

' Check for name validation error
If Browser("title:=Add Department - Employee Management System").Page("title:=Add Department - Employee Management System").WebElement("class:=invalid-feedback").Exist(2) Then
    Reporter.ReportEvent micPass, "Empty Department Name Test", "Department name validation error is displayed correctly"
Else
    Reporter.ReportEvent micFail, "Empty Department Name Test", "Department name validation error is not displayed"
End If

' Close the browser
SystemUtil.CloseProcessByName "chrome.exe"
