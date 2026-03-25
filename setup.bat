@echo off
REM Student Performance ML App - Automated Setup Script for Windows

echo.
echo ======================================================
echo   Student Performance ML App - Setup Script
echo ======================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    exit /b 1
)

echo [STEP 1] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    exit /b 1
)
echo [OK] Dependencies installed successfully

echo.
echo [STEP 2] Training ML model...
python model/train_model.py
if errorlevel 1 (
    echo [ERROR] Failed to train model
    exit /b 1
)
echo [OK] Model trained successfully

echo.
echo ======================================================
echo   Setup Complete!
echo ======================================================
echo.
echo To start the app, run:
echo   python app.py
echo.
echo Then open in your browser:
echo   http://localhost:5000
echo.
pause
