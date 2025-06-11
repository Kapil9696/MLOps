
from flask import Flask, jsonify

# Create Flask application instance
app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    """Home route that returns a welcome message"""
    return jsonify({
        "message": "Welcome to Simple Flask App!",
        "endpoints": [
            {"url": "/", "description": "Home page"},
            {"url": "/data", "description": "Sample data endpoint"},
            {"url": "/health", "description": "Application health check"}
        ]
    })

# Sample data endpoint
@app.route('/data')
def get_data():
    """Returns sample JSON data"""
    return jsonify({
        "users": [
            {"id": 1, "name": "Kapil", "role": "AI Developer"},
            {"id": 2, "name": "Kapil", "role": "Data Scientist"},
            {"id": 3, "name": "KApil", "role": "ML Engineer"}
        ]
    })

# Health check endpoint
@app.route('/health')
def health_check():
    """Application health status endpoint"""
    return jsonify({"status": "healthy", "version": "1.0.0"})

# Error handler for 404
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)