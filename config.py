# Configuration settings for Student Performance ML App

# Flask Configuration
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# Model Configuration
MODEL_PATH = 'model/model.pkl'
SCALER_PATH = 'model/scaler.pkl'
ENCODERS_PATH = 'model/encoders.pkl'

# Logging Configuration
LOG_FILE = 'app.log'
LOG_LEVEL = 'INFO'

# Input Validation Rules
INPUT_RANGES = {
    'study_hours': (0, 24),
    'phone_hours': (0, 24),
    'sleep_hours': (0, 24),
    'attendance': (0, 100)
}

# Recommendations
RECOMMENDED_VALUES = {
    'study_hours': 6,  # 6-8 hours
    'phone_hours': 2.5,  # 2-3 hours
    'sleep_hours': 8,  # 7-9 hours
    'attendance': 90  # 90%+
}

# API Response Codes
SUCCESS_CODE = 200
BAD_REQUEST_CODE = 400
SERVER_ERROR_CODE = 500
SERVICE_UNAVAILABLE_CODE = 503
