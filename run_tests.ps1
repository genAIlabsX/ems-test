# Run Selenium Tests for Employee Management System
# PowerShell Script

function Test-ServerRunning {
    try {
        $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000" -Method Head -TimeoutSec 2 -ErrorAction SilentlyContinue
        if ($response.StatusCode -eq 200) {
            return $true
        }
    } catch {
        return $false
    }
    return $false
}

function Start-DjangoServer {
    Write-Host "Starting Django server in a new window..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd ..\ems; python manage.py runserver"
    
    # Wait for server to start
    Write-Host "Waiting for server to start..." -ForegroundColor Yellow
    $maxAttempts = 10
    $attempts = 0
    $serverRunning = $false
    
    while (-not $serverRunning -and $attempts -lt $maxAttempts) {
        $serverRunning = Test-ServerRunning
        if (-not $serverRunning) {
            $attempts++
            Write-Host "Attempt $attempts of $maxAttempts Server not responding yet..." -ForegroundColor Yellow
            Start-Sleep -Seconds 2
        }
    }
    
    if ($serverRunning) {
        Write-Host "Django server is now running!" -ForegroundColor Green
        return $true
    } else {
        Write-Host "Failed to start Django server after $maxAttempts attempts." -ForegroundColor Red
        return $false
    }
}

function Setup-VirtualEnvironment {
    if (-not (Test-Path -Path "venv")) {
        Write-Host "Creating virtual environment..." -ForegroundColor Cyan
        python -m venv venv
        
        Write-Host "Installing dependencies..." -ForegroundColor Cyan
        .\venv\Scripts\python -m pip install -r requirements.txt
    } else {
        Write-Host "Using existing virtual environment" -ForegroundColor Green
    }
}

function Run-SeleniumTests {
    param (
        [string]$TestPath = "selenium_tests\tests",
        [switch]$Parallel = $false,
        [int]$Workers = 2,
        [switch]$Html = $false
    )
    
    # Activate virtual environment
    Write-Host "Activating virtual environment..." -ForegroundColor Cyan
    & .\venv\Scripts\Activate.ps1
    
    # Build command
    $command = "python -m pytest $TestPath -v"
    
    if ($Parallel) {
        $command += " -n $Workers"
    }
    
    if ($Html) {
        $command += " --html=report.html --self-contained-html"
    }
    
    # Run tests
    Write-Host "Running tests with command: $command" -ForegroundColor Cyan
    Invoke-Expression $command
    
    # Deactivate virtual environment
    deactivate
}

# Main script execution
Write-Host "Employee Management System Test Runner" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# Check if server is running
$serverRunning = Test-ServerRunning
if (-not $serverRunning) {
    Write-Host "Django server is not running at http://127.0.0.1:8000" -ForegroundColor Yellow
    
    $startServer = Read-Host "Do you want to start the Django server now? (y/n)"
    if ($startServer -eq "y") {
        $serverStarted = Start-DjangoServer
        if (-not $serverStarted) {
            Write-Host "Cannot continue without Django server running. Exiting..." -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "Please start the Django server manually with:" -ForegroundColor Yellow
        Write-Host "cd ..\ems" -ForegroundColor Yellow
        Write-Host "python manage.py runserver" -ForegroundColor Yellow
        exit 1
    }
} else {
    Write-Host "Django server is running at http://127.0.0.1:8000" -ForegroundColor Green
}

# Setup virtual environment
Setup-VirtualEnvironment

# Run tests
$runParallel = Read-Host "Run tests in parallel? (y/n)"
$generateHtml = Read-Host "Generate HTML report? (y/n)"

$parallelSwitch = $runParallel -eq "y"
$htmlSwitch = $generateHtml -eq "y"

Run-SeleniumTests -Parallel:$parallelSwitch -Html:$htmlSwitch

Write-Host "Tests completed!" -ForegroundColor Green
if ($htmlSwitch) {
    Write-Host "HTML report generated at report.html" -ForegroundColor Green
}
