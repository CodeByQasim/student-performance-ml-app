import requests
import json

tests = [
    {'name': 'Good Student (High study, low phone, good sleep, high attendance)', 'data': {'study_hours': 8, 'phone_hours': 1, 'sleep_hours': 8, 'attendance': 95}},
    {'name': 'Poor Student (Low study, high phone, low sleep, low attendance)', 'data': {'study_hours': 1, 'phone_hours': 8, 'sleep_hours': 4, 'attendance': 30}},
    {'name': 'Average Student', 'data': {'study_hours': 5, 'phone_hours': 4, 'sleep_hours': 7, 'attendance': 70}},
    {'name': 'Excellent Student', 'data': {'study_hours': 10, 'phone_hours': 0, 'sleep_hours': 9, 'attendance': 100}},
]

print("Testing Predictions with Different Student Profiles\n")
print("=" * 70)

for test in tests:
    try:
        res = requests.post('http://localhost:5000/api/predict', json=test['data'])
        data = res.json()
        print(f"\n{test['name']}")
        print(f"  Input: Study={test['data']['study_hours']}h, Phone={test['data']['phone_hours']}h, Sleep={test['data']['sleep_hours']}h, Attendance={test['data']['attendance']}%")
        print(f"  Prediction: {data['prediction']}")
        print(f"  Confidence: {data['confidence']:.1f}%")
        if data.get('insights'):
            print(f"  Insights: {', '.join(data['insights'][:2])}")
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 70)
