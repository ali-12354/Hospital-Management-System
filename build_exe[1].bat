@echo off
echo ============================================
echo Hospital Management System - Build Script
echo ============================================
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)
echo.

echo Installing PyInstaller (if not already installed)...
python -m pip install pyinstaller
echo.

echo Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo.

echo Building executable...
python -m PyInstaller HospitalManagementSystem.spec
echo.

if exist "dist\HospitalManagementSystem.exe" (
    echo ============================================
    echo BUILD SUCCESSFUL!
    echo ============================================
    echo.
    echo Executable created: dist\HospitalManagementSystem.exe
    echo.
    echo Creating distribution package...
    
    if not exist "dist\Distribution" mkdir "dist\Distribution"
    copy "dist\HospitalManagementSystem.exe" "dist\Distribution\"
    copy ".env" "dist\Distribution\"
    copy "SETUP_GUIDE.md" "dist\Distribution\"
    copy "README_INSTALLATION.txt" "dist\Distribution\"
    copy "xampp_test_inserts.sql" "dist\Distribution\"
    copy "check_table_structure.sql" "dist\Distribution\"
    
    echo.
    echo ============================================
    echo Distribution package ready in: dist\Distribution\
    echo ============================================
    echo.
    echo You can now share the Distribution folder with your group members!
    echo.
) else (
    echo ============================================
    echo BUILD FAILED!
    echo ============================================
    echo Check the output above for errors.
    echo.
)

pause
