# PowerShell script to run all Selenium tests for the Employee Management System

Write-Host "Starting Employee Management System Tests" -ForegroundColor Cyan

# Check if the Django server is running
$serverRunning = $false
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000" -Method Head -TimeoutSec 5 -ErrorAction SilentlyContinue
    if ($response.StatusCode -eq 200) {
        $serverRunning = $true
        Write-Host "Django server is running at http://127.0.0.1:8000" -ForegroundColor Green
    }
} catch {
    Write-Host "Django server is not running at http://127.0.0.1:8000" -ForegroundColor Yellow
}

if (-not $serverRunning) {
    Write-Host "Please start the Django server before running tests" -ForegroundColor Yellow
    Write-Host "Run the following command in a separate terminal:" -ForegroundColor Yellow
    Write-Host "cd ..\ems" -ForegroundColor Yellow
    Write-Host "python manage.py runserver" -ForegroundColor Yellow
    
    $startServer = Read-Host "Do you want to start the server now? (y/n)"
    if ($startServer -eq "y") {
        Start-Process powershell -ArgumentList "-Command cd ..\ems; python manage.py runserver"
        Write-Host "Waiting for server to start..." -ForegroundColor Cyan
        Start-Sleep -Seconds 5
    } else {
        Write-Host "Exiting test runner" -ForegroundColor Red
        exit
    }
}

# Install dependencies if needed
if (-not (Test-Path -Path ".\venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
    
    Write-Host "Installing dependencies..." -ForegroundColor Cyan
    .\venv\Scripts\python -m pip install -r requirements.txt
} else {
    Write-Host "Using existing virtual environment" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& .\venv\Scripts\Activate.ps1

# Run the tests
Write-Host "Running Selenium tests..." -ForegroundColor Cyan
python -m pytest selenium_tests\tests -v

# Deactivate virtual environment
deactivate

Write-Host "Tests completed!" -ForegroundColor Green
