' UFT Test Script for Employee Management System
' Test Case: View and Filter Employees

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

' Test 1: View All Employees
Reporter.ReportEvent micInfo, "Test Step", "Viewing all employees"
If Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebTable("class:=table").Exist(5) Then
    Reporter.ReportEvent micPass, "View Employees Test", "Employees table is displayed"
Else
    ' Check if "No employees found" message is displayed
    If Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebElement("innertext:=No employees found").Exist(2) Then
        Reporter.ReportEvent micPass, "View Employees Test", "No employees found message is displayed correctly"
    Else
        Reporter.ReportEvent micFail, "View Employees Test", "Neither employees table nor 'No employees found' message is displayed"
    End If
End If

' Test 2: Search Functionality
Reporter.ReportEvent micInfo, "Test Step", "Testing search functionality"
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebEdit("name:=q").Set "John"
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebButton("innertext:=Filter").Click
Wait 2

' Check if any results are found
If Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebTable("class:=table").Exist(5) Then
    Reporter.ReportEvent micInfo, "Search Test", "Search results are displayed for 'John'"
    
    ' Clear search
    Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebEdit("name:=q").Set ""
    Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebButton("innertext:=Filter").Click
    Wait 2
End If

' Test 3: Status Filter
Reporter.ReportEvent micInfo, "Test Step", "Testing status filter"
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebList("name:=status").Select "Active"
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebButton("innertext:=Filter").Click
Wait 2

' Reset filter
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebList("name:=status").Select "-- Status --"
Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebButton("innertext:=Filter").Click
Wait 2

' Test 4: Department Filter
Reporter.ReportEvent micInfo, "Test Step", "Testing department filter"

' First check if any departments exist in the dropdown
Dim departmentDropdown
Set departmentDropdown = Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebList("name:=department")

If departmentDropdown.GetItemsCount > 1 Then ' More than just the "-- Department --" option
    ' Select the second option (first actual department)
    departmentDropdown.Select 2 ' Index 2 (second item)
    Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebButton("innertext:=Filter").Click
    Wait 2
    
    ' Reset filter
    departmentDropdown.Select "-- Department --"
    Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").WebButton("innertext:=Filter").Click
    Wait 2
End If

' Test 5: Export to CSV
Reporter.ReportEvent micInfo, "Test Step", "Testing CSV export functionality"
If Browser("title:=Employees - Employee Management System").Page("title:=Employees - Employee Management System").Link("innertext:=Export to CSV").Exist(2) Then
    Reporter.ReportEvent micPass, "Export CSV Test", "Export to CSV button is present"
    
    ' Note: We won't actually click the button as it would download a file
    ' which is difficult to verify in UFT without additional configuration
Else
    Reporter.ReportEvent micWarning, "Export CSV Test", "Export to CSV button is not present (possibly no employees exist)"
End If

' Close the browser
SystemUtil.CloseProcessByName "chrome.exe"
