# SETUP INSTRUCTIONS - Student Performance ML App

## 🖥️ System Requirements

- Python 3.8 or higher
- pip (Python package manager)
- 2GB RAM minimum
- Modern web browser (Chrome, Firefox, Safari, Edge)

---

## 📦 Installation Method 1: Automated Setup (Recommended)

### Windows Users:
```batch
setup.bat
```

### Mac/Linux Users:
```bash
chmod +x setup.sh
./setup.sh
```

The script will:
1. ✅ Check Python installation
2. ✅ Install all dependencies
3. ✅ Train the ML model
4. ✅ Show you the next steps

---

## 🛠️ Installation Method 2: Manual Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

Wait for all packages to install. You should see:
```
Successfully installed Flask-3.0.0 scikit-learn-1.3.2 pandas-2.1.1 numpy-1.24.3
```

### Step 2: Train the ML Model
```bash
python model/train_model.py
```

Watch for this output:
```
============================================================
🚀 Starting Model Training Pipeline
============================================================
✓ Dataset loaded: 100 rows, 5 columns
✓ Model training completed!
✓ Model, scaler, and encoders saved successfully!
✅ Model Training Completed Successfully!
```

⚠️ **Important:** You MUST train the model before running the app.
The model file (model/model.pkl) is required!

### Step 3: Start the Application
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 4: Open in Browser
```
http://localhost:5000
```

---

## 🐍 Python Virtual Environment Setup (Optional but Recommended)

### Create Virtual Environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal.

### Then install dependencies:
```bash
pip install -r requirements.txt
```

---

## ✅ Verification Checklist

After installation, verify everything works:

### 1. Check Python
```bash
python --version
```
Should output: `Python 3.8.x` or higher

### 2. Check Dependencies
```bash
pip list
```
Should show:
- Flask 3.0.0
- scikit-learn 1.3.2
- pandas 2.1.1
- numpy 1.24.3

### 3. Check Model Files
Navigate to the `model/` folder - you should see:
- `model.pkl`
- `scaler.pkl`
- `encoders.pkl`

### 4. Test the App
Open `http://localhost:5000` and:
- Fill in the form
- Click "Get Prediction"
- See results appear

---

## 🚀 Running the App

### Normal Mode (Development):
```bash
python app.py
```

### Production Mode:
```bash
pip install gunicorn
gunicorn app:app
```

### With Custom Port:
```bash
python app.py --port 8000
```

Then open: `http://localhost:8000`

---

## 🆘 Troubleshooting

### Problem: "Python not found"
```
Solution: 
  1. Install Python 3.8+ from python.org
  2. During installation, CHECK "Add Python to PATH"
  3. Restart terminal/PowerShell
  4. Try again
```

### Problem: "Module not found" (Flask, pandas, etc.)
```
Solution: 
  1. Activate virtual environment (if using one)
  2. Run: pip install -r requirements.txt
  3. Wait for installation to complete
```

### Problem: "Model not found" error
```
Solution:
  1. Run: python model/train_model.py
  2. Wait for "✅ Model Training Completed Successfully!"
  3. Check that model/model.pkl exists
  4. Restart the app
```

### Problem: "Address already in use"
```
Solution:
  1. Use different port: python app.py --port 5001
  2. Or kill the process using port 5000:
     - Windows: netstat -ano | findstr :5000
     - Mac/Linux: lsof -i :5000
```

### Problem: Form submission not working
```
Solution:
  1. Check browser console (F12 → Console tab)
  2. Check that you filled all fields
  3. Check that values are in valid ranges
  4. Look for error message in red box
  5. Check app.log for server errors
```

### Problem: Charts not displaying
```
Solution:
  1. Check that Chart.js CDN is loading (F12 → Network)
  2. Check browser console for JS errors
  3. Try refreshing the page
  4. Try a different browser
```

---

## 📊 Testing the Application

### Test with curl (Command line):
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"study_hours": 6, "phone_hours": 3, "sleep_hours": 8, "attendance": 85}'
```

### Test Health Endpoint:
```bash
curl http://localhost:5000/api/health
```

### Test Tips Endpoint:
```bash
curl http://localhost:5000/api/tips
```

---

## 📝 Environment Variables (Advanced)

Create a `.env` file in the project root:

```
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
MODEL_PATH=model/model.pkl
```

Then load with:
```bash
# Windows
set FLASK_ENV=development
python app.py

# Mac/Linux
export FLASK_ENV=development
python app.py
```

---

## 🧪 Running Tests

### Install pytest:
```bash
pip install pytest
```

### Run all tests:
```bash
pytest tests/ -v
```

### Run specific test:
```bash
pytest tests/test_app.py::TestRoutes::test_health_check -v
```

---

## 📁 Project Structure After Setup

```
student-performance-ml-app/
├── app.py                 ✅ Ready to run
├── config.py
├── requirements.txt
├── setup.bat / setup.sh
├── README.md
├── UPGRADE_SUMMARY.md
├── CHANGES.txt
├── .gitignore
├── app.log               (Generated after first run)
│
├── model/
│   ├── train_model.py
│   ├── model.pkl        (Generated by train_model.py) ✅
│   ├── scaler.pkl       (Generated by train_model.py) ✅
│   └── encoders.pkl     (Generated by train_model.py) ✅
│
├── templates/
│   └── index.html       ✅ Modern UI
│
├── static/
│   ├── style.css        ✅ Professional design
│   └── script.js        ✅ Interactive features
│
├── dataset/
│   └── student_data.csv ✅ Training data
│
├── tests/
│   └── test_app.py      ✅ Unit tests
```

---

## 🎯 Next Steps

1. **Test locally** - Run the app and test all features
2. **Customize** - Change colors, fonts, or add features
3. **Train with data** - Use your own student dataset for better predictions
4. **Deploy** - Deploy to Heroku, AWS, or your own server
5. **Monitor** - Set up logging and error tracking

---

## 📚 Useful Commands Reference

```bash
# Activate virtual environment
Windows:  venv\Scripts\activate
Mac/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train model
python model/train_model.py

# Run app
python app.py

# Run tests
pytest tests/ -v

# Check logs
tail -f app.log  (Mac/Linux)
type app.log     (Windows)

# Kill app (if stuck)
Ctrl + C  (in terminal)

# Upgrade pip
pip install --upgrade pip

# List installed packages
pip list

# Freeze requirements
pip freeze > requirements.txt
```

---

## 🆘 Still Having Issues?

1. **Check app.log** - See what went wrong
2. **Check browser console** - Press F12, click Console
3. **Verify Python version** - `python --version` (need 3.8+)
4. **Verify dependencies** - `pip list`
5. **Re-train model** - `python model/train_model.py`
6. **Restart everything** - Close terminal, restart app

---

## ✅ You're Ready!

Once you see "Running on http://127.0.0.1:5000" in the terminal,
open that URL in your browser and start making predictions! 🎓

---

**Questions?** Check the README.md or UPGRADE_SUMMARY.md files!
