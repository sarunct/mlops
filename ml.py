from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define the root route for a basic ML model prediction
@app.route('/')
def predict():
    # ML model
    prediction = {"message": "This is a placeholder for ML model prediction"}
    return jsonify(prediction)

# Health check route
@app.route('/health')
def health_check():
    return jsonify(status="UP")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
