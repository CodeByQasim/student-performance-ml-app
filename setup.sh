#!/bin/bash
# Student Performance ML App - Automated Setup Script for Linux/Mac

echo ""
echo "======================================================"
echo "  Student Performance ML App - Setup Script"
echo "======================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.8+ using your package manager"
    exit 1
fi

echo "[STEP 1] Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi
echo "[OK] Dependencies installed successfully"

echo ""
echo "[STEP 2] Training ML model..."
python3 model/train_model.py
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to train model"
    exit 1
fi
echo "[OK] Model trained successfully"

echo ""
echo "======================================================"
echo "  Setup Complete!"
echo "======================================================"
echo ""
echo "To start the app, run:"
echo "  python3 app.py"
echo ""
echo "Then open in your browser:"
echo "  http://localhost:5000"
echo ""
