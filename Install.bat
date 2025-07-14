@echo off
setlocal

set "required_version=3.12.5"
set "python_url=https://www.python.org/ftp/python/%required_version%/python-%required_version%-amd64.exe"
set "installer_file=python-installer.exe"

echo Checking if Python is installed...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python %required_version%...
    goto install_python
)

for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set "current_version=%%a"
echo Python version found: %current_version%

if not "%current_version%"=="%required_version%" (
    echo Installed version (%current_version%) does not match required (%required_version%). Updating...
    goto install_python
) else (
    echo Required Python version is already installed.
)

goto install_packages

:install_python
echo Downloading Python installer from: %python_url%
curl -o %installer_file% %python_url%
if exist %installer_file% (
    echo Running Python installer...
    start /wait %installer_file% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
) else (
    echo Failed to download Python installer.
    pause
    exit /b 1
)

REM Verify installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python installation failed.
    pause
    exit /b 1
)

echo Python installed successfully.

REM Clean up installer
if exist %installer_file% (
    del /f /q %installer_file%
    echo Installer file deleted: %installer_file%
)

goto install_packages

:install_packages
echo Installing required Python packages...
pip install --upgrade pip
pip install pystyle requests

echo All required packages installed successfully.
pause
exit /b
