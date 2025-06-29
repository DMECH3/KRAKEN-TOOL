@echo off
setlocal enabledelayedexpansion

set "required_version=3.12.5"

echo Checking Python version...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing the latest version...
    goto install_python
) else (
    REM Get Python version
    for /f "tokens=2 delims= " %%a in ('python --version 2^>nul') do (
        set "version=%%a"
    )
    echo Detected Python version: !version!

    REM Compare version
    if "!version!" NEQ "%required_version%" (
        echo Updating Python to version %required_version%...
        goto install_python
    ) else (
        echo Python is up to date.
    )
)

REM Install required packages
echo Installing required Python packages...
pip install --upgrade pip
pip install pystyle
pip install scapy
pip install requests
echo All packages installed.
pause
exit /b

:install_python
echo Downloading Python %required_version% installer...
curl -o python-installer.exe https://www.python.org/ftp/python/%required_version%/python-%required_version%-amd64.exe

if not exist python-installer.exe (
    echo Failed to download Python installer.
    pause
    exit /b 1
)

echo Installing Python...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

REM Refresh environment variables
echo Refreshing environment...
set "PATH=%PATH%;%ProgramFiles%\Python%required_version:~0,1%%required_version:~2,2%\Scripts\"

REM Verify installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to install Python. Please install it manually.
    pause
    exit /b 1
) else (
    echo Python %required_version% installed successfully.
    goto :eof
)