from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Function to query each API endpoint
def query_api(ip, endpoint):
    url = f"http://{ip}:61208{endpoint}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return str(e)

# Home route that renders the HTML template
@app.route('/')
def index():
    return render_template('index.html')

# API route for querying specific endpoints (for /query)
@app.route('/query', methods=['POST'])
def query_endpoint():
    ip = request.form['ip']
    endpoint = request.form['endpoint']
    data = query_api(ip, endpoint)
    return jsonify(data)

# API route to set a new IP dynamically
@app.route('/set_ip', methods=['POST'])
def set_ip():
    new_ip = request.form['new_ip']
    # Return the new IP to update the JavaScript side
    return jsonify({'ip': new_ip})

# API route to query the API via curl (for /api_curl)
@app.route('/api_curl', methods=['POST'])
def api_curl_query():
    ip = request.form['ip']
    endpoint = request.form['endpoints']
    data = query_api(ip, endpoint)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Bind to all IPs
