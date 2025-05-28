' UFT Test Script for Employee Management System
' Test Case: Navigation Between Pages

Option Explicit

' Application URL
Const AppURL = "http://127.0.0.1:8000/"

' ===== Main Test Script =====
' Launch browser and navigate to application
SystemUtil.Run "chrome.exe", AppURL

' Wait for page to load
Wait 3

' Test 1: Home Page Navigation
Reporter.ReportEvent micInfo, "Test Step", "Testing navigation from home page"

' Verify we're on the home page
If Browser("title:=Employee Management System").Page("title:=Employee Management System").Link("text:=Home").Exist(5) Then
    Reporter.ReportEvent micPass, "Home Page Test", "Successfully loaded the home page"
Else
    Reporter.ReportEvent micFail, "Home Page Test", "Failed to load the home page"
End If

' Navigate to Employees page
Browser("title:=Employee Management System").Page("title:=Employee Management System").Link("text:=Employees").Click
Wait 2

' Verify we're on the Employees page
If Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebElement("innertext:=Employees").Exist(5) Then
    Reporter.ReportEvent micPass, "Navigation Test", "Successfully navigated to Employees page"
Else
    Reporter.ReportEvent micFail, "Navigation Test", "Failed to navigate to Employees page"
End If

' Navigate to Departments page
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").Link("text:=Departments").Click
Wait 2

' Verify we're on the Departments page
If Browser("title:=Departments - Employee Management System").Page("title:=Departments - Employee Management System").WebElement("innertext:=Departments").Exist(5) Then
    Reporter.ReportEvent micPass, "Navigation Test", "Successfully navigated to Departments page"
Else
    Reporter.ReportEvent micFail, "Navigation Test", "Failed to navigate to Departments page"
End If

' Navigate back to Home page using EMS link
Browser("title:=Departments - Employee Management System").Page("title:=Departments - Employee Management System").Link("text:=EMS").Click
Wait 2

' Test 2: Employee Page Navigation
Reporter.ReportEvent micInfo, "Test Step", "Testing navigation between employee pages"

' Navigate to Employees page
Browser("title:=Employee Management System").Page("title:=Employee Management System").Link("text:=Employees").Click
Wait 2

' Navigate to Add Employee page
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").Link("text:=Add New Employee").Click
Wait 2

' Verify we're on the Add Employee page
If Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebElement("innertext:=Add New Employee").Exist(5) Then
    Reporter.ReportEvent micPass, "Navigation Test", "Successfully navigated to Add Employee page"
Else
    Reporter.ReportEvent micFail, "Navigation Test", "Failed to navigate to Add Employee page"
End If

' Add an employee for testing navigation to edit/delete pages
Dim employeeName
employeeName = "Navigation Test " & Day(Now) & Hour(Now) & Minute(Now)

' Fill employee form with minimum required fields
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=name").Set employeeName
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=email").Set "nav.test" & Day(Now) & Hour(Now) & Minute(Now) & "@example.com"
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebList("name:=department").Select 1 ' First department
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebEdit("name:=salary").Set "50000"
Browser("title:=Add Employee - Employee Management System").Page("title:=Add Employee - Employee Management System").WebButton("type:=submit").Click
Wait 3

' Navigate to Edit Employee page (assuming the employee was added successfully)
' Find the Edit button in the row with the employee name
Dim editLink
Set editLink = Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").Link("text:=Edit", "index:=0")

If editLink.Exist(5) Then
    editLink.Click
    Wait 2
    
    ' Verify we're on the Edit Employee page
    If Browser("title").Exist(5) And Browser("title").GetROProperty("title") = "Edit Employee - Employee Management System" Then
        Reporter.ReportEvent micPass, "Navigation Test", "Successfully navigated to Edit Employee page"
    Else
        Reporter.ReportEvent micFail, "Navigation Test", "Failed to navigate to Edit Employee page"
    End If
    
    ' Navigate back to Employees page
    Browser("title").Page("title").Link("text:=Employees").Click
    Wait 2
End If

' Test 3: Department Page Navigation
Reporter.ReportEvent micInfo, "Test Step", "Testing navigation between department pages"

' Navigate to Departments page
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").Link("text:=Departments").Click
Wait 2

' Navigate to Add Department page
Browser("title:=Departments - Employee Management System").Page("title:=Departments - Employee Management System").Link("text:=Add New Department").Click
Wait 2

' Verify we're on the Add Department page
If Browser("title:=Add Department - Employee Management System").Page("title:=Add Department - Employee Management System").WebElement("innertext:=Add New Department").Exist(5) Then
    Reporter.ReportEvent micPass, "Navigation Test", "Successfully navigated to Add Department page"
Else
    Reporter.ReportEvent micFail, "Navigation Test", "Failed to navigate to Add Department page"
End If

' Test 4: Browser Back Button
Reporter.ReportEvent micInfo, "Test Step", "Testing browser back button navigation"

' Go back to Departments page
Browser("title:=Add Department - Employee Management System").Back
Wait 2

' Verify we're back on the Departments page
If Browser("title:=Departments - Employee Management System").Page("title:=Departments - Employee Management System").WebElement("innertext:=Departments").Exist(5) Then
    Reporter.ReportEvent micPass, "Back Button Test", "Successfully navigated back to Departments page"
Else
    Reporter.ReportEvent micFail, "Back Button Test", "Failed to navigate back to Departments page"
End If

' Close the browser
SystemUtil.CloseProcessByName "chrome.exe"
