' UFT Test Script for Employee Management System
' Test Case: Add New Employee

Option Explicit

' Application URL
Const AppURL = "http://127.0.0.1:8000/"

' Test Data
Dim EmployeeName, EmployeeEmail, EmployeeDepartment, EmployeeSalary
EmployeeName = "John Smith " & Day(Now) & Hour(Now) & Minute(Now) & Second(Now)
EmployeeEmail = "john.smith" & Day(Now) & Hour(Now) & Minute(Now) & Second(Now) & "@example.com"
EmployeeDepartment = "Engineering"
EmployeeSalary = "75000"

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

' Fill the employee form
' Name field
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=name").Set EmployeeName

' Email field
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=email").Set EmployeeEmail

' Department dropdown
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebList("name:=department").Select EmployeeDepartment

' Salary field
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=salary").Set EmployeeSalary

' Active status radio
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebRadioGroup("name:=status").Select "True"

' Submit the form
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebButton("type:=submit").Click
Wait 3

' Verify employee was added successfully
If Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebElement("innertext:=" & EmployeeName).Exist(5) Then
    Reporter.ReportEvent micPass, "Add Employee Test", "Employee '" & EmployeeName & "' was added successfully"
Else
    Reporter.ReportEvent micFail, "Add Employee Test", "Employee '" & EmployeeName & "' was not found in the list"
End If

' Close the browser
SystemUtil.CloseProcessByName "chrome.exe"
