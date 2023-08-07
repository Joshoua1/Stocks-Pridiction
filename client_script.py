import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'feature1': 10,
    'feature2': 20,
    # Add more features as required by your model
}

response = requests.post(url, json=data)
if response.status_code == 200:
    result = response.json()
    print("Prediction:", result['prediction'])
else:
    print("Error:", response.text)
