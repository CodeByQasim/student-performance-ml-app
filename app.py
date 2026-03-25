from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import logging
import os
from datetime import datetime
import json

# Initialize Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load model
try:
    if os.path.exists("model/model.pkl"):
        model = pickle.load(open("model/model.pkl", "rb"))
        logger.info("[OK] Model loaded successfully")
        logger.info(f"[INFO] Model type: {type(model).__name__}")
        
        # Load grade mapping if available
        grade_mapping = None
        if os.path.exists("model/grades.pkl"):
            grade_mapping = pickle.load(open("model/grades.pkl", "rb"))
            logger.info(f"[INFO] Grade mapping: {grade_mapping}")
    else:
        logger.warning("[WARNING] Model file not found. Please train the model first.")
        model = None
        grade_mapping = None
except Exception as e:
    logger.error(f"[ERROR] Error loading model: {str(e)}")
    model = None
    grade_mapping = None

# Route configurations
@app.route("/")
def home():
    """Serve the main page"""
    try:
        return render_template("index.html")
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}")
        return jsonify({"error": "Unable to load page"}), 500

@app.route("/api/predict", methods=["POST"])
def predict():
    """API endpoint for predictions with validation"""
    try:
        if model is None:
            return jsonify({
                "success": False,
                "error": "Model not available. Please train it first."
            }), 503

        # Get JSON data
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "error": "No data provided"
            }), 400

        # Input validation
        required_fields = ["study_hours", "phone_hours", "sleep_hours", "attendance"]
        errors = {}

        for field in required_fields:
            if field not in data:
                errors[field] = f"{field} is required"
            else:
                try:
                    value = float(data[field])
                    # Validate ranges - attendance is 0-100, others are 0-24
                    if field == "attendance":
                        if value < 0 or value > 100:
                            errors[field] = f"{field} must be between 0 and 100"
                    else:
                        if value < 0 or value > 24:
                            errors[field] = f"{field} must be between 0 and 24"
                except (ValueError, TypeError):
                    errors[field] = f"{field} must be a number"

        if errors:
            return jsonify({
                "success": False,
                "error": "Validation errors",
                "details": errors
            }), 400

        # Prepare features
        try:
            study_hours = float(data["study_hours"])
            phone_hours = float(data["phone_hours"])
            sleep_hours = float(data["sleep_hours"])
            attendance = float(data["attendance"])

            # Create feature array in same order as training
            features = np.array([[study_hours, phone_hours, sleep_hours, attendance]])
            
            logger.info(f"[DEBUG] Input features: {features}")
            logger.info(f"[DEBUG] Model expects: {model.n_features_in_ if hasattr(model, 'n_features_in_') else 'Unknown'} features")
            
            # Make prediction - NO SCALING needed for Random Forest
            prediction_code = model.predict(features)[0]
            probabilities = model.predict_proba(features)[0]
            confidence = float(max(probabilities)) * 100
            
            # Convert numeric prediction to grade name
            grade_name = grade_mapping.get(prediction_code, str(prediction_code)) if grade_mapping else str(prediction_code)

            # Get prediction insights
            insights = get_insights(study_hours, phone_hours, sleep_hours, attendance)

            logger.info(f"[OK] Prediction: {grade_name} (code: {prediction_code}), Confidence: {confidence:.2f}%")

            return jsonify({
                "success": True,
                "prediction": grade_name,
                "confidence": confidence,
                "insights": insights,
                "timestamp": datetime.now().isoformat()
            }), 200

        except ValueError as ve:
            logger.error(f"[ERROR] Value error: {str(ve)}")
            return jsonify({
                "success": False,
                "error": f"Value error: {str(ve)}"
            }), 500
        except Exception as e:
            logger.error(f"[ERROR] Prediction error: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return jsonify({
                "success": False,
                "error": f"Prediction error: {str(e)}"
            }), 500

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Server error"
        }), 500

@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/api/tips", methods=["GET"])
def tips():
    """Get student performance tips"""
    return jsonify({
        "tips": [
            "[GOAL] Maintain consistent study hours (6-8 hours daily)",
            "[PHONE] Limit phone usage to 2-3 hours per day",
            "[SLEEP] Get 7-9 hours of quality sleep",
            "[ATTEND] Attend classes regularly (90%+ attendance)",
            "[GROUP] Form study groups with peers",
            "[TIME] Create a structured study schedule",
            "[BREAK] Take breaks during study sessions"
        ]
    }), 200

def get_insights(study_hours, phone_hours, sleep_hours, attendance):
    """Generate personalized insights based on inputs"""
    insights = []
    
    if study_hours < 4:
        insights.append("[WARNING] Consider increasing study hours for better performance")
    elif study_hours >= 6:
        insights.append("[GOOD] Great study hours! Keep up the consistency")
    
    if phone_hours > 5:
        insights.append("[PHONE] Try reducing phone usage to improve focus")
    elif phone_hours <= 2:
        insights.append("[GOOD] Excellent phone discipline!")
    
    if sleep_hours < 6:
        insights.append("[SLEEP] Aim for 7-9 hours of sleep for optimal performance")
    elif sleep_hours >= 7:
        insights.append("[GOOD] Good sleep schedule supports academic success")
    
    if attendance < 75:
        insights.append("[ATTEND] Increase attendance to better understand concepts")
    elif attendance >= 90:
        insights.append("[GOOD] Excellent attendance! This boosts performance")
    
    return insights

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"Server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("Student Performance Prediction App Starting...")
    logger.info("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)