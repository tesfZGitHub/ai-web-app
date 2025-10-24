from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()  # ✅ read JSON from frontend
        text = (data.get('text') if data else '').strip()
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        print(f"Sending request to backend: {BACKEND_URL}/predict")
        
        # Send request to backend
        response = requests.post(
            f"{BACKEND_URL}/predict",
            json={"text": text},
            timeout=30
        )
        
        print(f"Backend response status: {response.status_code}")
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'Backend error: {response.status_code}'}), 503
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return jsonify({'error': 'Cannot connect to AI service'}), 503
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'frontend'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

